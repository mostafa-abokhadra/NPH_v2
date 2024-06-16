#!/usr/bin/python3
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine(f"mysql+mysqldb://{'database_admin'}:{'NPH_db_admin'}@localhost/{'NPH'}", pool_pre_ping=True)
base = declarative_base()

class Base:
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)

class Nurse(Base, base):
    __tablename__ = "Nurses"
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    specialist = Column(String(50))
    degree = Column(String(50))
    employemnt_status = Column(String(50))
    homeCarePatient = relationship("Patient", back_populates="nurse", cascade="all, delete, save-update")

class Patient(Base, base):
    __tablename__ = 'Patients'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    third_name = Column(String(50), nullable=False)
    fourth_name = Column(String(50), nullable=False)
    nurse_id = Column(Integer, ForeignKey("Nurses.id", ondelete="CASCADE", onupdate="CASCADE"))
    nurse = relationship("Nurse", back_populates="homeCarePatient")

base.metadata.create_all(bind=engine)