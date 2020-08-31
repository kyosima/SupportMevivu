from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs, conn

register_blp = Blueprint('register_blp', __name__)

@register_blp.route('/register', methods=['GET'])
def getRegister():
    if 'username' in session:
        title = 'Đăng ký'
        username = session['username']
        sql = "select levels from Users where userName='{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        if rows[0] == 1:
            return render_template('admin/index.html', title=title)
        elif rows[0] == 2:
            return render_template('Supporter/indexSupporter.html', title=title)
        elif rows[0] == 3:
            return render_template('Customer/indexCustomer.html',title=title)


    else:
        return render_template('admin/register.html')


@register_blp.route('/register', methods=['POST'])
def postRegister():
    try:
        errors = []
        _firstname = request.form.get('inputFirstname', None)
        _lastname = request.form.get('inputLastname', None)
        _username = request.form.get('inputUsername', None)
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        _hashpassword = generate_password_hash(_password)
        sql0 = "select count(*) from Users where userName = '{0}'".format(_username)
        curs.execute(sql0)
        rows = curs.fetchone()
        if rows and rows[0] > 0:
            errors = 'Username already exits!'
            return render_template('admin/register.html', errors=errors)
        elif _firstname and _lastname and _username and _email and _password:
            sql1 = "insert into Users(firstName, lastName, userName, email, passWord) values ('{0}', '{1}', '{2}', " \
                   "'{3}', '{4}')".format(
                _firstname, _lastname, _username, _email, _hashpassword)
            curs.execute(sql1)
            conn.commit()

            return redirect(url_for('login_blp.getLogin'))
    except Exception as e:
        raise (e)