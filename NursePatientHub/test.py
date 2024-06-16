#!/usr/bin/python3
from db import Nurse
from db import Patient
from db import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine,  expire_on_commit=False)
session = Session()

n = session.query(Nurse).filter(Nurse.id).first()


p = Patient()
p.firstName = "ali"
p.lastName = "ahmed"
p.third_name= "osama"
p.fourth_name="yehia"
p.nurse = n

session.add(p)
session.commit()
