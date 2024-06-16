#!/usr/bin/python3
from database.creating_engine import engine
Base.metadata.create_all(bind=engine)
