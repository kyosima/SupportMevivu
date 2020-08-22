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
        return render_template('index.html')
    else:
        return render_template('login.html')


@login_blp.route('/login', methods=['POST'])
def postLogin():
    try:
        errors = []
        _username = request.form.get('inputUsername', None)
        _password = request.form.get('inputPassword', None)

        sql = "select passWord from Users where userName = '{0}'".format(_username)
        curs.execute(sql)
        rows = curs.fetchone()

        if rows:
            hashpassword = rows[0]
            if check_password_hash(hashpassword, _password):
                session['username'] = _username
                return redirect(url_for('index_blp.index'))
            else:
                errors = 'Wrong username or password!'
                return render_template('login.html', errors=errors)
    except Exception as e:
        raise (e)