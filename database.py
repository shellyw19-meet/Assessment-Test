from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_applicant(name, age, subject):
	applicant_object = applicants(
		name = name,
		age = age,
		subject = subject)
	session.add(applicant_object)
	session.commit()

def get_all_applicants():
	applicants = session.query(applicants).all()
	return applicants


# I have a problem with 20th line, UnboundLocalError
