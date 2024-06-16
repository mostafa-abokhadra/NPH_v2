#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://{database_admin}:{NPH_admin}@localhost/{NPH}', pool_pre_ping=True)
base = declarative_base()
