#!/usr/bin/python3
"""starting point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database_admin:NPH_db_admin@localhost/NPH'
app.config.from_object(__name__)
ndb = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# api = Api(app)

from NursePatientHub import routes