#!/usr/bin/python3
from models import User
from models import Nurse
from models import Patient
from models import Employer
from models import engine
from sqlalchemy.orm import sessionmaker, aliased
Patient_als = aliased(Patient, flat=True) """ this solve the problem of joining overlabing tables that inherit from 
                                                the same class
                                                nurse = session.query(Nurse.firstName, Patient_als.firstName)
                                                .join(Patient_als, Nurse.Nurse_id == Patient_als.nurse_id).all()
                                                """

Session = sessionmaker(bind=engine,  expire_on_commit=False)
session = Session()

# nurse = Nurse(firstName="mostafa", lastName="abokhadra", email="mvxizk@gmail.com", password="mostafa-pass")
# session.add(nurse)
# session.commit()

# n = session.query(Nurse).filter(Nurse.firstName == "mostafa", Nurse.lastName == "abokhadra").first()

# p = Patient(firstName="ahmed", lastName="osama", email="ahmedosama@gmail.com", password="ahemdosama-pass")
# p.nurse_id = n.Nurse_id
# session.add(p)
# session.commit()

# p = Patient(firstName="momen", lastName="sameh", email="momensamed@gmail.com", password="momensameh-pass")
# p.nurse_id = n.Nurse_id
# session.add(p)
# session.commit()

# p = Patient(firstName="hoda", lastName="bakr", email="hodabadr@gmail.com", password="hodabakr-pass")
# p.nurse_id = n.Nurse_id

# session.add(p)
# session.commit()

nurse = session.query(Nurse.firstName, Patient_als.firstName).join(Patient_als, Nurse.Nurse_id == Patient_als.nurse_id).all()
print(nurse)
