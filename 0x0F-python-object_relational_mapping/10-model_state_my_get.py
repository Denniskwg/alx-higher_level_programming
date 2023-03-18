#!/usr/bin/python3
"""10-model_state_my_get.py -  lists the State object
with the name passed as argument from the database hbtn_0e_6_usa
username, password and database name will be passed as arguments to the script
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name == sys.argv[4])
    if query.count() == 0:
        print("Not found")
    else:
        for state in query:
            print(state.id)
