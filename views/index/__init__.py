from datetime import timedelta

from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import app,curs

index_blp  = Blueprint('index_blp', __name__)


@index_blp.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)

@index_blp.route('/', methods=['GET'])
def index():
    if 'username' in session:
        username = session['username']
        title = 'Admin'
        sql = "select * from Users where userName = '{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        ava = rows[10]
        fname = rows[6]
        lname = rows[7]
        pagetitle = "Tổng quan"
        session['avatar'] = ava
        session['firstname'] = fname
        session['lastname'] = lname
        avatar = session['avatar']
        firstname = session['firstname']
        lastname = session['lastname']
        sql1 = "select count(id) from Users where levels = '2'"
        curs.execute(sql1)
        row_sp = curs.fetchone()
        sql2 = "select count(id) from Users where levels = '3'"
        curs.execute(sql2)
        row_customer = curs.fetchone()
        sql3 = "select levels from Users where userName = '{0}'".format(username)
        curs.execute(sql3)
        row_lv = curs.fetchone()
        level = row_lv[0]
        if level == 1:
            return render_template('admin/index.html', username=username, title = title, avatar=avatar, firstname=firstname, lastname=lastname, pagetitle=pagetitle, ava= ava, sp = row_sp[0], customer = row_customer[0])
        if level == 2:
            return render_template('Supporter/indexSupporter.html', username=username, title = title, avatar=avatar, firstname=firstname, lastname=lastname, pagetitle=pagetitle, ava= ava, sp = row_sp[0], customer = row_customer[0])
    else:
        return redirect(url_for('login_blp.getLogin'))