from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database_admin:NPH_db_admin@localhost/NPH'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'Users'
    User_id = db.Column(db.Integer, nullable=False, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = Column(String(20), nullable=False)
   
class Nurse(User, db.Model):
    __tablename__ = "Nurses"
    Nurse_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    specialist = db.Column(db.String(50))
    degree = db.Column(db.String(50))
    employemnt_status = db.Column(db.String(50))

class Patient(User, db.Model):
    __tablename__ = 'Patients'
    Patient_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    nurse_id = db.Column(db.Integer, ForeignKey("Nurses.Nurse_id", ondelete="CASCADE", onupdate="CASCADE"))
    diagnosis = db.Column(db.String(50))

class Employer(User, db.Model):
    __tablename__ = "Employers"
    Employer_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey("Users.User_id", ondelete="CASCADE", onupdate="CASCADE"))
    application = relationship("Application", back_populates="employer", cascade="all, delete, save-update")
    organization_name = db.Column(db.String(50))

class Application(db.Model):
    __tablename__ = 'Applications'
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey("Employers.Employer_id", ondelete="CASCADE", onupdate="CASCADE"))
    employer = relationship("Employer", back_populates="application")
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    organization_name = Column(String(50))
    organization_address = db.Column(db.String(200))
    referred_by = db.Column(db.String(50))
    position = db.Column(db.String(100))
    education_requirements = db.Column(db.String(200))
    special_skills = db.Column(db.String(200))
    experience_years = db.Column(db.String(50))

my_db.create_all()