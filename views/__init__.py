from flaskext.mysql import MySQL
from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'chiakhoa'

mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'malouda15'
app.config['MYSQL_DATABASE_DB'] = 'support_mevivu'

conn = mysql.connect()
curs = conn.cursor()

from views.index import index_blp
from views.login import login_blp
from views.profile import profile_blp
from views.register import register_blp

app.register_blueprint(index_blp)
app.register_blueprint(login_blp)
app.register_blueprint(profile_blp)
app.register_blueprint(register_blp)

