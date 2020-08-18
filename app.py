from flask import Flask, render_template, url_for, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'key'


mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'malouda15'
app.config['MYSQL_DATABASE_DB'] = 'support_mevivu'



conn = mysql.connect()
curs = conn.cursor()

print('Connect success!')

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=3)

@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username = username)
    else:
        return redirect(url_for('getLogin'))

@app.route('/profile',methods=['get'])
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


        return render_template('profile.html', username = username, email = email, createdDate = createdDate, firstname = firstname, lastname = lastname, phone = phone,role=role)
    else:
        return redirect(url_for('getLogin'))

@app.route('/editProfile', methods=['get'])
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
        return render_template('editProfile.html', email=email, username=username, password=password, firstname=firstname, lastname=lastname, phone=phone, role=role)
    else:
        return redirect(url_for('getLogin'))

@app.route('/editProfile', methods=['post'])
def postEditProfile():
    try:
        username = session['username']
        _firstname = request.form.get('inputFirstname', None)
        _lastname = request.form.get('inputLastname', None)
        _email = request.form.get('inputEmail', None)
        _phone = request.form.get('inputPhone', None)
        _role = request.form.get('inputRole', None)
        _password = request.form.get('inputPassword', None)
        hashpassword = generate_password_hash(_password)


        sql = "update Users set firstName = '{0}', lastName='{1}', email='{2}', phone='{3}', profession ='{4}', passWord ='{5}' where userName = '{6}'".format(_firstname, _lastname,_email, _phone, _role,hashpassword, username)
        curs.execute(sql)
        conn.commit()

        return redirect(url_for('getProfile'))
    except Exception as e:
        raise (e)



@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('getLogin'))

@app.route('/login', methods=['GET'])
def getLogin():
    if 'username' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def postLogin():
    try:
        errors = []
        _username = request.form.get('inputUsername', None)
        _password = request.form.get('inputPassword', None)

        sql = "select passWord from Users where userName = '{0}'".format(_username)
        curs.execute(sql)
        rows = curs.fetchone()

        if rows :
            hashpassword = rows[0]
            if check_password_hash(hashpassword, _password):
                session['username'] = _username
                return redirect(url_for('index'))
            else:
                errors = 'Wrong username or password!'
                return render_template('login.html', errors = errors)
    except Exception as e:
        raise (e)

@app.route('/register', methods=['GET'])
def getRegister():
    if 'username' in session:
        return render_template('index.html')
    else:
        return render_template('register.html')

@app.route('/register', methods=['POST'])
def postRegister():
    try:
        errors = []
        _firstname = request.form.get('inputFirstname', None)
        _lastname = request.form.get('inputLastname', None)
        _username = request.form.get('inputUsername', None)
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        _hashpassword = generate_password_hash(_password)
        sql0 = "select count(*) from Users where username = '{0}'".format(_username)
        curs.execute(sql0)
        rows = curs.fetchone()
        if rows and rows[0] > 0:
            errors = 'Username already exits!'
            return render_template('register.html', errors = errors)
        elif _firstname and _lastname and _username and _email and _password:
            sql1 = "insert into Users(firstName, lastName, userName, email, passWord) values ('{0}', '{1}', '{2}', '{3}', '{4}')".format(_firstname, _lastname, _username, _email, _hashpassword)
            curs.execute(sql1)
            conn.commit()

            return redirect(url_for('getLogin'))
    except Exception as e:
        raise (e)





if __name__ == '__main__':
    app.run()
