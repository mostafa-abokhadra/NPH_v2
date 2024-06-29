#!/usr/bin/python3
"""starting point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://avnadmin:AVNS_dkQO0y4LKX_S1PM1VvO@nph-mbukhadra-nph.f.aivencloud.com:22413/NPH'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database_admin:NPH_db_admin@localhost/NPH'
app.config.from_object(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# api = Api(app)

from NursePatientHub import routes