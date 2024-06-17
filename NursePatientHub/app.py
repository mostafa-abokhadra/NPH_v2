#!/usr/bin/python3
"""starting point"""
from flask import Flask, render_template, url_for, request, redirect
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

@app.route('/signUp', methods=["POST", "GET"])
def signUp():
    if request.method == 'POST':
        newuser = request.form
        return redirect(url_for('homewoutsignup'))
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run(debug=True)