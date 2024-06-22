#!/usr/bin/python3
"""starting point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)
# api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database_admin:NPH_db_admin@localhost/NPH'
ndb = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from NursePatientHub import routes