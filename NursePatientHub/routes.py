from NursePatientHub import app, bcrypt, db
from flask import render_template, url_for, request, redirect, flash, session
from NursePatientHub.models import User, Patient, Nurse, Employer
from NursePatientHub.models import Application, HealthTeaching, NotAnswered
from NursePatientHub.forms import Registration, Login
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
@app.route('/NPH', strict_slashes=False)
def home():
    return render_template('home.html')

@app.route('/signUp',strict_slashes=False, methods=["POST", "GET"])
def signUp():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = Registration()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.validata_email(form.email):
                flash("email already taken! try to login")
                return redirect(url_for('login'))
            hasshed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(password=hasshed_password, username=form.username.data,
                email=form.email.data, userType=form.userType.data)
            db.session.add(new_user)
            db.session.commit()
            if form.userType.data == 'N':
                n = Nurse()
                n.user_id = new_user.id
                db.session.add(n)
                db.session.commit()
            elif form.userType.data == 'P':
                patient = Patient()
                patient.user_id = new_user.id
                db.session.add(patient)
                db.session.commit()
            else:
                emp = Employer()
                emp.user_id = new_user.id
                db.session.add(emp)
                db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
    return render_template('signUp.html', form=form)

@app.route('/login', methods=["POST", "GET"])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    next_page = request.args.get('next')
                    return redirect(next_page) if next_page else redirect(url_for('home'))
                else:
                    flash('password is wrong! try again')
                    return redirect(url_for('login'))
            else:
                flash("email can't be found!")
    return render_template("login.html", form=form)


@app.route('/jobs', strict_slashes=False, methods=['GET'])
def jobs():
    apls = Application.query.all()
    return render_template('jobs.html', apls=apls)
    
@app.route('/applications', methods=["GET", "POST"])
@login_required
def applications():
    if request.method == "GET":
        if current_user.userType == 'P' or current_user.userType == 'N':
            flash("only employers have access to this page !")
            return redirect(url_for('jobs'))
    elif request.method == 'POST':
        new_application = Application(
        country=request.form["country"], city=request.form["city"],
        organization_name=request.form["organizationName"],
        organization_address=request.form["organizationAddress"],
        referred_by=request.form["employerName"], position=request.form["position"],
        education_requirements=request.form["education"],
        experience_years=request.form["experienceYears"],
        salary=request.form["salary"], currency=request.form["currency"], employer_id=current_user.type_E.id)
        db.session.add(new_application)
        db.session.commit()
        current_user.applications = new_application
        flash("application added successfully")
        return redirect(url_for('jobs'))
    return render_template('applications.html')


@app.route('/healthTeaching', methods=["GET", "POST"])
def healthTeaching():
    if request.method == 'POST':
        if current_user.userType == 'N':
            print(request.form['ht-title'])
            still_question = NotAnswered.query.filter_by(question=request.form['ht-title']).first()
            parchor = HealthTeaching(
                question=still_question.question, answer=request.form['ht-content'],
                nurse_id=current_user.type_N.id, patient_id=still_question.patient_id)
            db.session.delete(still_question)
            db.session.add(parchor)
            db.session.commit()
        else:
            question = NotAnswered(question=request.form["patient-q"])
            question.patient_id = current_user.type_P.id
            db.session.add(question)
            db.session.commit()
    all_parchors = HealthTeaching.query.all()
    still_to_answer = NotAnswered.query.all()
    return render_template('healthTeaching.html', all_parchors=all_parchors, still=still_to_answer)

@app.route('/logout', strict_slashes=False)
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('home'))

# @app.route('/about', methods=["GET"])
# def about():
#     # if request.method == 'POST':
#     return render_template('about.html')