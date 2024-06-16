#!/usr/bin/python3
from sqlalchemy import Integer, Column, String, ForeignKey
from models.base import Base

class Patient(Base):
    __tablename__ = 'Patients'
    third_name = Column(string(50), nullable=False)
    fourth_name = Column(string(50), nullable=False)
    responsible_nurse = Column(Integer, ForeignKey("Nurses.id", ondelete="CASCADE", onupdate="CASCADE"))
