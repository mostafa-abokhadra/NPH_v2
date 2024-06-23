from NursePatientHub import db, app
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    User_id = db.Column(db.Integer, primary_key=True,unique=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    userType = db.Column(db.CHAR(1), nullable=False)
   
class Nurse(User, db.Model):
    __tablename__ = "Nurses"
    Nurse_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    specialist = db.Column(db.String(50))
    degree = db.Column(db.String(50))
    employemnt_status = db.Column(db.String(50))

class Patient(User, db.Model):
    __tablename__ = 'Patients'
    Patient_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    nurse_id = db.Column(db.Integer, db.ForeignKey("Nurses.Nurse_id", ondelete="CASCADE", onupdate="CASCADE"))
    diagnosis = db.Column(db.String(50))

class Employer(User, db.Model):
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

# with app.app_context():
#     db.create_all()