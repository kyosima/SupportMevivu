from datetime import timedelta

from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import app,curs

index_blp  = Blueprint('index_blp', __name__)

@index_blp.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

@index_blp.route('/', methods=['GET'])
def index():
    if 'username' in session:
        username = session['username']
        title = 'Admin'
        sql = "select * from Users where userName = '{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        avatar = rows[10]
        firstname = rows[6]
        lastname = rows[7]
        pagetitle = "Tổng quan"
        return render_template('admin/index.html', username=username, title = title, avatar=avatar, firstname=firstname, lastname=lastname, pagetitle=pagetitle)
    else:
        return redirect(url_for('login_blp.getLogin'))