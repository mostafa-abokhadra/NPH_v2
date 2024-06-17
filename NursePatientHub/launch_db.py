#!/usr/bin/python3
from models import User
from models import Nurse
from models import Patient
from models import Employer
from models import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine,  expire_on_commit=False)
session = Session()

nurse = Nurse(firstName="mostafa", lastName="abokhadra", email="mvxizk@gmail.com", password="mostafa-pass")
session.add(nurse)
session.commit()