from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs, conn, app
import os
from werkzeug.utils import secure_filename

requirements_blp = Blueprint('requirements_blp', __name__)


@requirements_blp.route('/requirements', methods=['get'])
def requirements():
    if 'username' in session:
        title = 'Tất cả yêu cầu'
        pagetitle = 'Tất cả yêu cầu'
        username = session['username']
        sql = "select levels from Users where userName = '{0}'".format(username)
        curs.execute(sql)
        rows = curs.fetchone()
        level = rows[0]
        # sql1 = "select * from Requirements"
        # curs.execute(sql1)
        # infos = curs.fetchall()
        sql2 = "select * from Users as usold left join Requirements as re on usold.id = re.Users_idSupporter join " \
               "Users as usnew on usnew.id = re.Users_idCustomer"
        curs.execute(sql2)
        ofSupporters = curs.fetchall()
        if level == 1:
            return render_template('admin/requirements.html', ofSupporters=ofSupporters, title=title,
                                   pagetitle=pagetitle, username=username)
        else:
            return '404 Not Found - Bạn không có quyền truy cập vào trang này'
    else:
        return redirect(url_for('login_blp.getLogin'))


@requirements_blp.route('/requirements_on', methods=['get'])
def getRequirements_on():
    if 'username' in session:
        title = "Danh sách yêu cầu chưa xử lý"
        pagetitle = 'Danh sách yêu cầu chưa xử lý'
        username = session['username']
        sql0 = "select levels from Users where userName='{0}'".format(username)
        curs.execute(sql0)
        level = curs.fetchone()
        sql1 = "select * from Users as usold left join Requirements as re on usold.id = re.Users_idSupporter join " \
               "Users as usnew on usnew.id = re.Users_idCustomer where re.status='1'"
        curs.execute(sql1)
        requirements_on = curs.fetchall()
        if level[0] == 1:
            return render_template('admin/requirements_on.html', title=title, pagetitle=pagetitle, username=username,
                                   requirements_on=requirements_on)
        else:
            return '404 Not Found - Bạn không có quyền truy cập vào web này'


@requirements_blp.route('/requirements_done', methods=['get'])
def getRequirements_done():
    if 'username' in session:
        title = "Danh sách yêu cầu đã xử lý"
        pagetitle = 'Danh sách yêu cầu đã xử lý'
        username = session['username']
        sql0 = "select levels from Users where userName='{0}'".format(username)
        curs.execute(sql0)
        level = curs.fetchone()
        sql1 = "select * from Users as usold left join Requirements as re on usold.id = re.Users_idSupporter join " \
               "Users as usnew on usnew.id = re.Users_idCustomer where re.status='2'"
        curs.execute(sql1)
        ofSupporters = curs.fetchall()
        if level[0] == 1:
            return render_template('admin/requirements_done.html', title=title, pagetitle=pagetitle, username=username,
                                   ofSupporters=ofSupporters)
        else:
            return '404 Not Found - Bạn không có quyền truy cập vào web này'

@requirements_blp.route('/requirements_detail/<id>', methods=['get'])
def getRequirementDetail(id):
    if 'username' in session:
        title = 'Chi tiết yêu cầu'
        pagetitle = 'Chi tiết yêu cầu'
        username = session['username']
        sql1 = "select usold.firstName, usold.lastName, re.* , usnew.firstName, usnew.lastName from Users as usold left join Requirements as re on usold.id = re.Users_idSupporter join " \
               "Users as usnew on usnew.id = re.Users_idCustomer where re.id='{0}'".format(id)
        curs.execute(sql1)
        rows = curs.fetchone()
        print(rows)
        sql0 = "select levels from Users where userName='{0}'".format(username)
        curs.execute(sql0)
        level = curs.fetchone()
        if level[0] == 1:
            return render_template('admin/requirement_detail.html', rows=rows)
