from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs, conn, app
import os
from werkzeug.utils import secure_filename

requirements_blp = Blueprint('requirements_blp', __name__)

@requirements_blp.route('/requirements', methods = ['get'])
def requirements():
    if 'username' in session:
        title = 'Tất cả yêu cầu'
        pagetitle = 'Tất cả yêu cầu'
        username = session['username']
        sql = "select levels from Users where userName = '{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        level = rows[0]
        sql1 = "select * from Requirements"
        curs.execute(sql1)
        infos = curs.fetchall()
        sql2 = "select firstName, lastName from Users inner join Requirements on Users.id = Requirements.Users_id"
        curs.execute(sql2)
        ofSupporters = curs.fetchone()
        print(ofSupporters)


        if level == 1:
            return render_template('admin/requirements.html',ofSupporters=ofSupporters, title=title, pagetitle=pagetitle, infos=infos, username=username)
        else:
            return '404 Not Found - Bạn không có quyền truy cập vào trang này'
    else:
        return redirect(url_for('login_blp.getLogin'))