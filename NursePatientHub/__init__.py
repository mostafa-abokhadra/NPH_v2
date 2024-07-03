#!/usr/bin/python3
"""starting point"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pymysql
from flask_session import Session
from redis import Redis

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)

if not os.environ.get('DATABASE_URL'):
    raise ValueError("Missing required environment variables for database connection")

# if not all([ os.environ.get('AVNADMIN'), os.environ.get('AVN_PASSWORD'),
#     os.environ.get('AVNHOST'), os.environ.get('AVNPORT'),
#     os.environ.get('AVNDB')]):
#     raise ValueError("Missing required environment variables for database connection")
pymysql.install_as_MySQLdb()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}:{}/{}".format(
#     os.environ.get('AVNADMIN'), os.environ.get('AVN_PASSWORD'),
#     os.environ.get('AVNHOST'), os.environ.get('AVNPORT'),
#     os.environ.get('AVNDB'))
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'session:'
redis_client = Redis(
    host=os.environ.get('REDIS_HOST'),
    port=os.environ.get('REDIS_PORT'),
    password=os.environ.get('REDIS_PASSWORD'))
app.config['SESSION_REDIS'] = redis_client
Session(app)
app.config.from_object(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
from NursePatientHub import routes