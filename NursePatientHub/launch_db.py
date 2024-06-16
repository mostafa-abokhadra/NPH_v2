#!/usr/bin/python3
from db import Nurse
from db import Patient
from db import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine,  expire_on_commit=False)
session = Session()