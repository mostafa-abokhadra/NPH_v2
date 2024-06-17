#!/usr/bin/python3
"""starting point"""
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_restful import Api, Resource, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database_admin:NPH_db_admin@localhost/NPH'
ndb = SQLAlchemy(app)

class User(ndb.Model):
    __tablename__ = 'Users'
    User_id = ndb.Column(ndb.Integer, nullable=False, primary_key=True)
    firstName = ndb.Column(ndb.String(50), nullable=False)
    lastName = ndb.Column(ndb.String(50), nullable=False)
    email = ndb.Column(ndb.String(100), nullable=False)
    password = ndb.Column(ndb.String(20), nullable=False)
   
class Nurse(User, ndb.Model):
    __tablename__ = "Nurses"
    Nurse_id = ndb.Column(ndb.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = ndb.Column(ndb.Integer, ndb.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    specialist = ndb.Column(ndb.String(50))
    degree = ndb.Column(ndb.String(50))
    employemnt_status = ndb.Column(ndb.String(50))

class Patient(User, ndb.Model):
    __tablename__ = 'Patients'
    Patient_id = ndb.Column(ndb.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = ndb.Column(ndb.Integer, ndb.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    nurse_id = ndb.Column(ndb.Integer, ndb.ForeignKey("Nurses.Nurse_id", ondelete="CASCADE", onupdate="CASCADE"))
    diagnosis = ndb.Column(ndb.String(50))

class Employer(User, ndb.Model):
    __tablename__ = "Employers"
    Employer_id = ndb.Column(ndb.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = ndb.Column(ndb.Integer, ndb.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    application = ndb.relationship("Application", back_populates="employer", cascade="all, delete, save-update")
    organization_name = ndb.Column(ndb.String(50))

class Application(ndb.Model):
    __tablename__ = 'Applications'
    id = ndb.Column(ndb.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = ndb.Column(ndb.Integer, ndb.ForeignKey("Employers.Employer_id", ondelete="CASCADE", onupdate="CASCADE"))
    employer = ndb.relationship("Employer", back_populates="application")
    country = ndb.Column(ndb.String(50))
    city = ndb.Column(ndb.String(50))
    organization_name = ndb.Column(ndb.String(50))
    organization_address = ndb.Column(ndb.String(200))
    referred_by = ndb.Column(ndb.String(50))
    position = ndb.Column(ndb.String(100))
    education_requirements = ndb.Column(ndb.String(200))
    special_skills = ndb.Column(ndb.String(200))
    experience_years = ndb.Column(ndb.String(50))

# with app.app_context():
#     ndb.create_all()

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
@app.route('/NPH', strict_slashes=False)
def home():
    return render_template('home.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")


def check_email_validity(req):
    check_email_exists = User.query.filter(User.email == req["email"]).first()
    if (check_email_exists == None):
        return 1

def check_pass_validity(req):
    if len(req["password"]) < 8:
        return 1

@app.route('/signUp', methods=["POST", "GET"])
def signUp():
    if request.method == 'POST':
        if not check_email_validity(request.form):
            flash("email already exists!")
            return redirect(url_for('login'))
        elif check_pass_validity(request.form):
            flash("password can't be less than 8 characters")
            return redirect(url_for('signUp'))
        
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run(debug=True)