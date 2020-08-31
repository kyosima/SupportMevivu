from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs, conn, app
import os
from werkzeug.utils import secure_filename

listSupperter_blp = Blueprint('listSupporter_blp', __name__)


@listSupperter_blp.route('/listSupporter', methods=['get'])
def getListSupporter():
    if 'username' in session:
        username = session['username']
        pagetitle = 'Danh sách kỹ thuật viên'
        title = 'Danh sách kỹ thuật viên'
        custombutton = 'Thêm kỹ thuật viên'
        sql0 = "select * from Users where levels ='2'"
        curs.execute(sql0)
        rows = curs.fetchall()
        avatar = session['avatar']
        sql1 = "select levels from Users where userName = '{0}'".format(username)
        curs.execute(sql1)
        level = curs.fetchone()
        if level[0] == 1:
            return render_template('admin/listSupporter.html', pagetitle=pagetitle, title=title, rows=rows, custombutton=custombutton, avatar=avatar, username=username)
        else:
            return "404 - Not Found. Bạn không được phép truy cập vào trang này!"
    else:
        return redirect(url_for('login_blp.getLogin'))


@listSupperter_blp.route('/editSupporter/<id>', methods=['get'])
def getEditSupporter(id):
    if 'username' in session:
        username = session['username']
        pagetittle = 'Thay đổi thông tin Kỹ thuật viên'
        title = 'Thay đổi thông tin Kỹ thuật viên'
        sql0 = "select * from Users where id='{0}'".format(id)
        curs.execute(sql0)
        rows = curs.fetchone()
        usernamesp = rows[1]
        email = rows[2]
        firstname = rows[6]
        lastname = rows[7]
        phone = rows[8]
        levels = rows[9]
        birthday = rows[11]
        avatar = session['avatar']
        sql1 = "select levels from Users where userName = '{0}'".format(username)
        curs.execute(sql1)
        level = curs.fetchone()
        if level[0] == 1:
            return render_template('admin/editSupporter.html', avatar=avatar, usernamesp=usernamesp, pagetittle=pagetittle, title=title, username=username,
                               email=email, firstname=firstname, lastname=lastname, levels=levels, phone=phone, birthday=birthday)
        else:
            return "404- Not Found. Bạn không có quyền đăng nhập vào trang này"
@listSupperter_blp.route('/editSupporter/<id>', methods=['post'])
def postEditSupporter(id):
    try:
        if 'username' in session:
            pagetitle = 'Thông tin Kỹ thuật viên'
            _inputfirstname = request.form.get('inputFirstname',None)
            _inputlastname = request.form.get('inputLastname',None)
            _inputemail = request.form.get('inputEmail',None)
            _inputphone = request.form.get('inputPhone',None)
            _inputlevels = request.form.get('inputLevels',None)
            _inputbirthday = request.form.get('inputBirthday', None)
            sql0 = "Update Users set firstName = '{0}', lastName = '{1}', email = '{2}', phone = '{3}', levels = '{4}', birthDay='{5}' where id='{6}'".format(_inputfirstname, _inputlastname, _inputemail, _inputphone, _inputlevels,_inputbirthday, id)
            curs.execute(sql0)
            conn.commit()
            sql1 = "select * from Users where id='{0}'".format(id)
            curs.execute(sql1)
            rows = curs.fetchone()
            return redirect(url_for('listSupporter_blp.getListSupporter'))
    except Exception as e:
        raise (e)
@listSupperter_blp.route('/addSupporter', methods=['get'])
def getaddSupporter():
    if 'username' in session:
        pagetitle = 'Thêm kỹ thuật viên'
        title = 'Thêm kỹ thuật viên'
        username = session['username']
        avatar = session['avatar']
        sql = "select levels from Users where userName='{0}'".format(username)
        curs.execute(sql)
        level = curs.fetchone()
        if level[0] == 1:
            return render_template('admin/addSupporter.html', pagetitle=pagetitle, title=title, username=username, avatar=avatar)
        else:
            return '404 - Not Found. Bạn không có quyền truy cập vào trang này'
    else:
        return redirect(url_for('login_blp.getLogin'))

@listSupperter_blp.route('/addSupporter', methods=['POST'])
def postaddSupporter():
    try:
        username = request.form.get('inputUsername', None)
        firstname = request.form.get('inputFirstname', None)
        lastname = request.form.get('inputLastname', None)
        email = request.form.get('inputEmail', None)
        phone = request.form.get('inputPhone', None)
        levels = request.form.get('inputLevels', None)
        birthday = request.form.get('inputBirthday', None)
        password = request.form.get('inputPassword', None)
        hashpassword = generate_password_hash(password)
        sql0 = "select count(*) from Users where userName = '{0}'".format(username)
        curs.execute(sql0)
        rows = curs.fetchone()
        if rows and rows[0] > 0:
            pagetitle = 'Thêm kỹ thuật viên'
            errors = 'Tên đăng nhập đã tồn tại!'
            return render_template('admin/addSupporter.html', errors=errors, pagetitle=pagetitle)
        elif username and email and password:
            sql1 = "insert into Users(firstName, lastName, userName, email, passWord,phone, levels, birthDay) values ('{0}', '{1}', '{2}', " \
                   "'{3}', '{4}','{5}','{6}','{7}')".format(firstname, lastname, username, email, hashpassword, phone, levels, birthday)
            curs.execute(sql1)
            conn.commit()
            return redirect(url_for('listSupporter_blp.getListSupporter'))
    except Exception as e:
        raise (e)
