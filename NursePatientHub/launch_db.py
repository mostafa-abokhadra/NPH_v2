#!/usr/bin/python3
engine = __import__('models/database.create_engine').engine
from models.base import Base
from models.patient import Patient
from models.nurse import Nurse

Base.metadata.create_all(bind=engine)
