#!/usr/bin/python3
from sqlachemy import Column, Integer, String
from models.Base import Base
from sqlalchemy.orm import relationship, backref
from models.Patient import Patient

class Nurse(Base):
    __tablename__ = "Nurses"
    specialist = Column(String(50))
    degree = Column(string(50))
    employemnt_status = Column(String(50), nullable=False)
    homeCarePatient = relationship("Patient", backref="Nurse", uselist=False, cascade="all, delete, save-update")
