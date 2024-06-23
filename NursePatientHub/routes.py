from NursePatientHub import app, bcrypt, db
from flask import render_template, url_for, request, redirect, flash
# from NursePatientHub.models import User, Patient, Nurse, Employer, Application
from NursePatientHub.forms import Registration, Login
from flask_login import login_user, UserMixin, LoginManager, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    User_id = db.Column(db.Integer, primary_key=True,unique=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    userType = db.Column(db.CHAR(1), nullable=False)
   
class Nurse(db.Model):
    __tablename__ = "Nurses"
    Nurse_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    specialist = db.Column(db.String(50))
    degree = db.Column(db.String(50))
    employemnt_status = db.Column(db.String(50))

class Patient(db.Model):
    __tablename__ = 'Patients'
    Patient_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    nurse_id = db.Column(db.Integer, db.ForeignKey("Nurses.Nurse_id", ondelete="CASCADE", onupdate="CASCADE"))
    diagnosis = db.Column(db.String(50))

class Employer(db.Model):
    __tablename__ = "Employers"
    Employer_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    application = db.relationship("Application", back_populates="employer", cascade="all, delete, save-update")
    organization_name = db.Column(db.String(50))

class Application(db.Model):
    __tablename__ = 'Applications'
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Employers.Employer_id", ondelete="CASCADE", onupdate="CASCADE"))
    employer = db.relationship("Employer", back_populates="application")
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    organization_name = db.Column(db.String(50))
    organization_address = db.Column(db.String(200))
    referred_by = db.Column(db.String(50))
    position = db.Column(db.String(100))
    education_requirements = db.Column(db.String(200))
    # special_skills = db.Column(db.String(200))
    experience_years = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    currency = db.Column(db.String(60))



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
    if request.method == 'POST':
        if form.validate_on_submit():
            email = User.query.filter(User.email == form.email.data).first()
            if email:
                flash("email already exists! try to login")
                return redirect(url_for('login'))
            # from NursePatientHub import db
            hasshed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(password=hasshed_password, username=form.username.data,
                email=form.email.data, userType=form.userType.data)
            db.session.add(new_user)
            db.session.commit()
            if form.userType.data == 'N':
                n = Nurse()
                n.user_id = new_user.User_id
                db.session.add(n)
                db.session.commit()
            elif form.userType.data == 'P':
                patient = Patient()
                patient.user_id = new_user.User_id
                db.session.add(patient)
                db.session.commit()
            else:
                emp = Employer()
                emp.user_id = new_user.User_id
                db.session.add(emp)
                db.session.commit()
            return render_template('dashBoard.html')
    return render_template('signUp.html', form=form)

@app.route('/login', methods=["POST", "GET"])
def login():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('ok ok')
            user = User.query.filter(User.email == form.email.data).first()
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('dashBoard'))
    return render_template("login.html", form=form)

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

@app.route('/healthTeaching', methods=["GET", "POST"])
def healthTeaching():
    # if request.method == 'POST':
    return render_template('healthTeaching.html')

    
@app.route('/about', methods=["GET"])
def about():
    # if request.method == 'POST':
    return render_template('about.html')