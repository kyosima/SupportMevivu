from flask import render_template, url_for, session, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from views import curs, conn, app
import os
from werkzeug.utils import secure_filename

listSupperter_blp = Blueprint('listSupporter_blp', __name__)

@listSupperter_blp.route('/listSupporter', methods = ['get'])
def getListSupporter():
    if 'username' in session:
        pagetitle = 'Danh sách kỹ thuật viên'
        title = 'Danh sách kỹ thuật viên'
        return render_template('admin/listSupporter.html', pagetitle=pagetitle, title=title)
    else:
        return redirect(url_for('login_blp.getLogin'))
