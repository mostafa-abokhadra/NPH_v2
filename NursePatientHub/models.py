#!/usr/bin/python3
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine(f"mysql+mysqldb://{'database_admin'}:{'NPH_db_admin'}@localhost/{'NPH'}", pool_pre_ping=True)
base = declarative_base()

class User(base):
    __tablename__ = 'Users'
    id = Column(Integer, nullable=False, primary_key=True)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(20), nullable=False)
   
class Nurse(User, base):
    __tablename__ = "Nurses"
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE", onupdate="CASCADE"))
    specialist = Column(String(50))
    degree = Column(String(50))
    employemnt_status = Column(String(50))

class Patient(account, base):
    __tablename__ = 'Patients'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE", onupdate="CASCADE"))
    nurse_id = Column(Integer, ForeignKey("Nurses.id", ondelete="CASCADE", onupdate="CASCADE"))
    diagnosis = Column(String(50))

class Employer(User, base):
    __tablename__ = "Employers"
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE", onupdate="CASCADE"))
    organization_name = Column(String(50))

class Application(base):
    __tablename__ = 'Applications'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("Employers.id", ondelete="CASCADE", onupdate="CASCADE"))
    country = Column(String(50))
    city = Column(String(50))
    organization_name = Column(String(50))
    organization_address = Column(String(200))
    referred_by = Column(String(50))
    position = Colum(String(100))
    education_requirements(String(200))
    special_skills = Column(String(200))
    experience_years = Column(String(50))


base.metadata.create_all(bind=engine)