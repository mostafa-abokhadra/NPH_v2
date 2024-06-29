#!/usr/bin/python3
"""starting point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}:{}/{}".format(
    os.environ.get('AVNADMIN'), os.environ.get('AVN_PASSWORD'),
    os.environ.get('AVNHOST'), os.environ.get('AVNPORT'),
    os.environ.get('AVNDB'))
app.config.from_object(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# api = Api(app)

from NursePatientHub import routes