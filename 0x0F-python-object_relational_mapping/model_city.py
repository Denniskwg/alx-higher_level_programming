#!/usr/bin/python3
"""model_state - contains the class definition of a City
and an instance Base = declarative_base()
state class inherits from Base , links to MySQL table 'states',
has columns id and name
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """defines a city class for creating a table in a
    database using sqlalchemy
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
