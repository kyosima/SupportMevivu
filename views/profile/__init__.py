from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs, conn, app
import os
from werkzeug.utils import secure_filename

profile_blp = Blueprint('profile_blp', __name__)


@profile_blp.route('/editPassword', methods=['GET'])
def getEditpassword():
    if 'username' in session:
        username = session['username']
        sql = "select * from Users where userName='{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()

        firstname = rows[6]
        lastname = rows[7]

        avatar = rows[10]

        pagetitle = 'Thông tin'
        title = 'Thông tin'
        return render_template('admin/editPassword.html', firstname=firstname, lastname=lastname, avatar=avatar,
                               pagetitle=pagetitle, title=title)
    else:
        return redirect(url_for('login_blp.getLogin'))


@profile_blp.route('/editPassword', methods=['POST'])
def postEditpassword():
    try:
        username = session['username']
        _currentpassword = request.form.get('inputCurrentPass')
        _newpassword = request.form.get('inputPassword')
        newhashpassword = generate_password_hash(_newpassword)
        sql = "select passWord from Users where userName = '{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        hashpasword = rows[0]
        if check_password_hash(hashpasword, _currentpassword):
            sql1 = "update Users set passWord ='{0}' where userName = '{1}'".format(newhashpassword, username)
            curs.execute(sql1)
            conn.commit()
            return redirect(url_for('profile_blp.getProfile'))
        else:
            errors = 'Wrong Current Password'
            return render_template('admin/editPassword.html', errors=errors)
    except Exception as e:
        raise (e)


@profile_blp.route('/profile', methods=['get'])
def getProfile():
    if 'username' in session:
        username = session['username']
        sql = "select * from Users where userName='{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        email = rows[2]
        createdDate = rows[5]
        firstname = rows[6]
        lastname = rows[7]
        phone = rows[8]
        role = rows[9]
        avatar = rows[10]
        birthday = rows[11]
        pagetitle = 'Thông tin'
        title = 'Thông tin'
        if role == 1:
            level = 'Admin'
        elif role == 2:
            level = 'Kỹ thuật viên'
        elif role == 3:
            level = 'Khách hàng'
        return render_template('admin/profile.html', title=title, pagetitle=pagetitle, username=username, email=email,
                               createdDate=createdDate,
                               firstname=firstname, lastname=lastname,role=level, phone=phone, avatar=avatar,
                               birthday=birthday)
    else:
        return redirect(url_for('login_blp.getLogin'))


@profile_blp.route('/editProfile', methods=['get'])
def getEditProfile():
    if 'username' in session:
        username = session['username']
        sql = "select * from Users where userName='{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        email = rows[2]
        password = rows[3]
        createdDate = rows[5]
        firstname = rows[6]
        lastname = rows[7]
        phone = rows[8]
        role = rows[9]
        avatar = rows[10]
        birthday = rows[11]
        pagetitle = 'Thay đổi thông tin'

        return render_template('admin/editProfile.html', pagetitle=pagetitle, email=email, username=username,
                               password=password,
                               firstname=firstname, lastname=lastname, phone=phone, role=role, birthday=birthday,
                               avatar=avatar)
    else:
        return redirect(url_for('profile_blp.getLogin'))


@profile_blp.route('/editProfile', methods=['post'])
def postEditProfile():
    try:
        if request.form['submit'] == 'SaveAvatar':
            if request.files:
                username = session['username']

                _avatar = request.files["image"]
                filename = secure_filename(_avatar.filename)
                _avatar.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                sql = "update Users set avatar='{0}' where userName = '{1}'".format(filename, username)
                curs.execute(sql)
                conn.commit()
                return redirect(url_for('profile_blp.getProfile'))

        elif request.form['submit'] == 'SaveProfile':
            username = session['username']
            _firstname = request.form.get('inputFirstname', None)
            _lastname = request.form.get('inputLastname', None)
            _email = request.form.get('inputEmail', None)
            _phone = request.form.get('inputPhone', None)
            _role = request.form.get('inputRole', None)
            _avatar1 = request.form.get('inputAvatar', None)

            _birthday = request.form.get('inputBirthday', None)
            sql0 = "select passWord from Users where userName='{0}'".format(username)
            curs.execute(sql0)
            rows = curs.fetchone()
            hashedpassword = rows[0]
            sql = "update Users set firstName = '{0}', lastName='{1}', email='{2}', phone='{3}', levels ='{4}'," \
                  "birthDay='{5}' where userName = '{6}'".format(
                _firstname, _lastname, _email, _phone, _role, _birthday, username)
            curs.execute(sql)
            conn.commit()
            return redirect(url_for('profile_blp.getProfile'))


    except Exception as e:
        raise (e)
