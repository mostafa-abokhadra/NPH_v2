#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from database.create_engine import engine, base

class Base(base):
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
