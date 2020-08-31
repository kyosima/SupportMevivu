from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs

login_blp = Blueprint('login_blp', __name__)

@login_blp.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login_blp.getLogin'))


@login_blp.route('/login', methods=['GET'])
def getLogin():
    if 'username' in session:
        username = session['username']
        sql = "select levels from Users where userName='{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        level = rows[0]
        if level == 1:
            return render_template('admin/index.html', username=username)
        if level == 2:
            return render_template('Supporter/indexSupporter.html', username=username)
        if level == 3:
            return render_template('Customer/indexCustomer.html', username=username)

    else:
        title = 'Đăng nhập'
        return render_template('admin/login.html', title=title)


@login_blp.route('/login', methods=['POST'])
def postLogin():
    try:
        errors = []
        _username = request.form.get('inputUsername', None)
        _password = request.form.get('inputPassword', None)

        sql = "select passWord from Users where levels ='1' and userName = '{0}'".format(_username)
        curs.execute(sql)
        rows = curs.fetchone()

        sql1 = "select passWord from Users where levels ='2' and userName = '{0}'".format(_username)
        curs.execute(sql1)
        rows1 = curs.fetchone()

        sql2 = "select passWord from Users where levels ='3' and userName = '{0}'".format(_username)
        curs.execute(sql2)
        rows2 = curs.fetchone()
        if rows:
            hashpassword_admin = rows[0]
            if check_password_hash(hashpassword_admin, _password):
                session['username'] = _username

                return redirect(url_for('index_blp.index'))
            else:
                errors = 'Wrong username or password!'
                return render_template('admin/login.html', errors=errors)
        elif rows1:
            hashpassword_supporter = rows1[0]
            if check_password_hash(hashpassword_supporter, _password):
                session['username'] = _username
                return redirect(url_for('index_blp.index'))
            else:
                errors = 'Wrong username or password!'
                return render_template('admin/login.html', errors=errors)
        elif rows2:
            hashpassword_customer = rows2[0]
            if check_password_hash(hashpassword_customer, _password):
                session['username'] = _username
                return 'Tài khoản customer '
            else:
                errors = 'Wrong username or password!'
                return render_template('admin/login.html', errors=errors)

    except Exception as e:
        raise (e)