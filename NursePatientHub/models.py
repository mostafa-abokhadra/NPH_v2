from NursePatientHub import db, app, login_manager
from flask_login import UserMixin
# from flask_sqlalchemy import SQLAlchemy

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True,unique=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    userType = db.Column(db.CHAR(1), nullable=False)
    type_N = db.relationship('Nurse', backref='type_N', uselist=False, cascade='all, delete, save-update')
    type_P = db.relationship('Patient', backref='type_P', uselist=False, cascade='all, delete, save-update')
    type_E = db.relationship('Employer', backref='type_E', uselist=False, cascade='all, delete, save-update')

class Nurse(db.Model):
    __tablename__ = "Nurses"
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="CASCADE", onupdate="CASCADE"))
    # specialist = db.Column(db.String(50))
    # degree = db.Column(db.String(50))
    # employemnt_status = db.Column(db.String(50))

class Patient(db.Model):
    __tablename__ = 'Patients'
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="CASCADE", onupdate="CASCADE"))
    nurse_id = db.Column(db.Integer, db.ForeignKey("Nurses.id", onupdate="CASCADE"))
    # diagnosis = db.Column(db.String(50))

class Employer(db.Model):
    __tablename__ = "Employers"
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="CASCADE", onupdate="CASCADE"))
    applications = db.relationship("Application", backref='employer', cascade="all, delete, save-update")
    # organization_name = db.Column(db.String(50))

class Application(db.Model):
    __tablename__ = 'Applications'
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("Employers.user_id", ondelete="CASCADE", onupdate="CASCADE"))
    employer_id = db.Column(db.Integer, db.ForeignKey("Employers.id", ondelete="CASCADE", onupdate="CASCADE"))

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

    # def __repr__(self):
    #     return "position: {}\nsalary: {}\nreferred By: {}\n".format(
    #         self.position, self.salary, self.referred_by)
            
# with app.app_context():
#     db.create_all()