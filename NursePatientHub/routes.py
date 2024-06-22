from NursePatientHub import app
from flask import render_template, url_for, request, redirect, flash
from NursePatientHub.models import User, Patient, Nurse, Employer, Application
from forms import Registration, Login
from control import check_name_validity, check_email_exists, check_pass_validity

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
@app.route('/NPH', strict_slashes=False)
def home():
    return render_template('home.html')

@app.route('/signUp', methods=["POST", "GET"])
def signUp():
    if request.method == 'POST':
        if check_name_validity(request.form) == 1:
            flash("full name can't be less than 10 or greater than 20 character !")
            return redirect(url_for('signUp'))
        elif check_name_validity(request.form) == 2:
            flash("name can't contain special character")
            return redirect(url_for('signUp'))
        elif check_email_exists(request.form["email"]):
            flash("email already exists! try to login")
            return redirect(url_for('login'))
        elif check_pass_validity(request.form) == 1:
            flash("password can't be less than 8 characters")
            return redirect(url_for('signUp'))
        elif check_pass_validity(request.form) == 2:
            flash("confirm the pass correctly !")
            return redirect(url_for('signUp'))
        else:
            new_user = User(firstName=request.form["firstName"], lastName=request.form["lastName"],
                            email=request.form["email"], password=request.form["password"], userType='S')
            ndb.session.add(new_user)
            ndb.session.commit()
            flash("Welcome {}".format(new_user.firstName))  
            return redirect(url_for("userBase"))
    else:
        return render_template('signUp.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    loginForm = Login()
    if forms.validate_on_submit():
    # if request.method == 'POST':
        if (check_email_exists(request.form["email"])):
            user = User.query.filter(User.password == request.form["password"],User.email == request.form["email"]).first()
            if  user == None:
                flash("password is wrong! try again")
                return redirect(url_for("login"))
            else:
                flash("Welcome {}".format(user.firstName))
                return redirect(url_for('userBase'))
        else:
            flash("can't find email! try again")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route('/userType', strict_slashes=False, methods=["POST", "GET"])
def userType():
    if request.method == "POST":
        print("==========")
        print("it's post")
        print("==========")
    return render_template('userType.html')

@app.route('/jobs', strict_slashes=False, methods=['post', 'GET'])
def jobs():
    return render_template('jobs.html')
    
@app.route('/applications', methods=["GET", "POST"])
def applications():
    if request.method == 'POST':
        print(request.form)
    return render_template('applications.html')

@app.route('/userBase', strict_slashes=False)
def userBase():
    return render_template('userBase.html')
