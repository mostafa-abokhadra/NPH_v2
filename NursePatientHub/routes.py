from NursePatientHub import app, bcrypt
from flask import render_template, url_for, request, redirect, flash
from NursePatientHub.models import User, Patient, Nurse, Employer, Application
from NursePatientHub.forms import Registration, Login
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
@app.route('/NPH', strict_slashes=False)
def home():
    return render_template('home.html')

@app.route('/dashBoard', strict_slashes=False, methods=["POST", "GET"])
@login_required
def dashBoard():
    return render_template('dashBoard.html')

@app.route('/signUp',strict_slashes=False, methods=["POST", "GET"])
def signUp():
    form = Registration()
    if form.validate_on_submit():
        email = User.query.filter(User.email == form.email.data).first()
        if email:
            flash("email already exists! try to login")
            return redirect(url_for('login'))
        from NursePatientHub import db
        hasshed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(password=hasshed_password, username=form.username.data,
            email=form.email.data, userType=form.userType.data)
        # new_user = User(username="mostafa", email="mostaf@gmail.com", userType='N', password="messimessi")
        if form.userType.data == 'N':
            nurse = Nurse()
            nurse.user_id = new_user.User_id
            db.session.add(new_user)
            db.session.add(nurse)
        elif form.userType.data == 'P':
            patient = Patient()
            patient.user_id = new_user.User_id
            db.session.add(new_user)
            db.session.add(patient)
        else:
            emp = Employer()
            emp.user_id = new_user.User_id
            db.session.add(new_user)
            db.session.add(emp)
        with app.app_context():
            print("asldfjklasjd;ljsdfa;sldj;sjdalfk;sldajf")
            db.session.commit()
        return render_template('dashBoard.html')
    return render_template('signUp.html', form=form)

@app.route('/login', methods=["POST", "GET"])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashBoard'))
    return render_template("login.html")

@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.html'))

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