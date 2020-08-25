from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'chiakhoa'

app.config["IMAGE_UPLOADS"] = "/Users/kyosima/PycharmProjects/SupportMevivu/static/img"

mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'malouda15'
app.config['MYSQL_DATABASE_DB'] = 'support_mevivu'


conn = mysql.connect()
curs = conn.cursor()

from views.admin.index import index_blp
from views.admin.login import login_blp
from views.admin.profile import profile_blp
from views.admin.register import register_blp

app.register_blueprint(index_blp)
app.register_blueprint(login_blp)
app.register_blueprint(profile_blp)
app.register_blueprint(register_blp)

