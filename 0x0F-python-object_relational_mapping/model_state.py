#!/usr/bin/python3
"""model_state - contains the class definition of a State
and an instance Base = declarative_base()
state class inherits from Base , links to MySQL table 'states',
has columns id and name
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """defines a state class for creating a table in a
    database using sqlalchemy
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
