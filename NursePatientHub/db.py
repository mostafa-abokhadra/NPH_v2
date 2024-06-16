#!/usr/bin/python3
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('mysql+mysqldb://{database_admin}:{NPH_admin}@localhost/{NPH}', pool_pre_ping=True)
base = declarative_base()

class Base(base):
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)

class Nurse(Base):
    __tablename__ = "Nurses"
    specialist = Column(String(50))
    degree = Column(string(50))
    employemnt_status = Column(String(50), nullable=False)
    homeCarePatient = relationship("Patient", backref="Nurse", uselist=False, cascade="all, delete, save-update")

class Patient(Base):
    __tablename__ = 'Patients'
    third_name = Column(string(50), nullable=False)
    fourth_name = Column(string(50), nullable=False)
    responsible_nurse = Column(Integer, ForeignKey("Nurses.id", ondelete="CASCADE", onupdate="CASCADE"))

Base.metadata.create_all(bind=engine)