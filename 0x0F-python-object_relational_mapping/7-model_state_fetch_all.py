#!/usr/bin/python3
"""This script list all the state in the datatbase using sqlalchemy"""
from sqlalchemy import creat _engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.args[1], sys.args[2], sys.args[3])
    Session = sessionmaker(bind=engine)
    session = Session()

   for state in session.query(State).order_by(State.id):
   print('{0}: {1}'.format(instance.id, instance.name))
