#!/usr/bin/python3
"""14-model_city_fetch_by_state -  prints all City objects from the database
hbtn_0e_14_usa
username, password and database name will be passed as arguments to the script
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City)\
        .filter(State.id == City.state_id)
    for i in query:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
