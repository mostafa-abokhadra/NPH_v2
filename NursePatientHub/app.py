#!/usr/bin/python3
"""starting point"""
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_restful import Api, Resource, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database_admin:NPH_db_admin@localhost/NPH'
db = SQLAlchemy(app)

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
@app.route('/NPH', strict_slashes=False)
def home():
    return render_template('home.html')

def check_validity(req):
    check_email_exist = db.query(User).filter_by(email == req["email"]).first()
    if (check_email):
        flash("email already exists!")
        redircet(url_for('login'))


@app.route('/signUp', methods=["POST", "GET"])
def signUp():
    if request.method == 'POST':
        check_validity(request.form)
    return render_template('signUp.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)