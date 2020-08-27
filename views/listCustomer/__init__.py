from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs, conn, app
import os
from werkzeug.utils import secure_filename

listCustomer_blp = Blueprint('listCustomer_blp', __name__)


@listCustomer_blp.route('/listCustomer', methods=['get'])
def getListCustomer():
    if 'username' in session:
        username = session['username']
        pagetitle = 'Danh sách khách hàng'
        title = 'Danh sách khách hàng'
        sql0 = "select * from Users where levels ='3'"
        curs.execute(sql0)
        rows = curs.fetchall()
        return render_template('admin/listCustomer.html', pagetitle=pagetitle, title=title, rows=rows)
    else:
        return redirect(url_for('login_blp.getLogin'))


@listCustomer_blp.route('/editCustomer/<id>', methods=['get'])
def getEditCustomer(id):
    if 'username' in session:
        username = session['username']
        pagetittle = 'Thay đổi thông tin Khách hàng'
        title = 'Thay đổi thông tin Khách hàng'
        sql0 = "select * from Users where id='{0}'".format(id)
        curs.execute(sql0)
        rows = curs.fetchone()
        username = rows[1]
        email = rows[2]
        firstname = rows[6]
        lastname = rows[7]
        phone = rows[8]
        levels = rows[9]
        birthday = rows[11]
        return render_template('admin/editCustomer.html', pagetittle=pagetittle, title=title, username=username,
                               email=email, firstname=firstname, lastname=lastname, levels=levels,phone=phone, birthday=birthday)
@listCustomer_blp.route('/editCustomer/<id>', methods=['post'])
def postEditCustomer(id):
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
            username = rows[1]
            email = rows[2]
            firstname = rows[6]
            lastname = rows[7]
            phone = rows[8]
            levels = rows[9]
            birthday = rows[11]
            return redirect(url_for('listCustomer_blp.getListCustomer'))
    except Exception as e:
        raise (e)
