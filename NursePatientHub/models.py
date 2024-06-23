from NursePatientHub import ndb, app
from flask_login import UserMixin

class User(ndb.Model, UserMixin):
    __tablename__ = 'Users'
    User_id = ndb.Column(ndb.Integer, nullable=False, primary_key=True,unique=True, autoincrement=True)
    username = ndb.Column(ndb.String(20), nullable=False)
    email = ndb.Column(ndb.String(50), nullable=False, unique=True)
    password = ndb.Column(ndb.String(60), nullable=False)
    userType = ndb.Column(ndb.CHAR(1), nullable=False)
   
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
    # special_skills = ndb.Column(ndb.String(200))
    experience_years = ndb.Column(ndb.String(50))
    salary = ndb.Column(ndb.Integer)
    currency = ndb.Column(ndb.String(60))

with app.app_context():
    ndb.create_all()