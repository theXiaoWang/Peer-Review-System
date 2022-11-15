import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'e14f29145e30d50e7274d2b642c9c41b84770c445db565a1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # This is a temporary sqllite databse, can be changed to MySQL if needed to.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
# This is email server setup for auto send email function for Reporting Issues, please do not modify this.(Xiao W)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from app import routes