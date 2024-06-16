#!/usr/bin/python3
from models.__init__ import engine
from models.base import Base
from models.patient import Patient
from models.nurse import Nurse

Base.metadata.create_all(bind=engine)
