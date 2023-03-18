#!/usr/bin/python3
"""9-model_state_filter_a.py -  lists all State objects
that contain the letter 'a' from the database hbtn_0e_6_usa
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
    query = session.query(State).filter(State.name.like('%a%'))
    query = query.order_by(State.id)
    for entry in query:
        print("{}: {}".format(entry.id, entry.name))
