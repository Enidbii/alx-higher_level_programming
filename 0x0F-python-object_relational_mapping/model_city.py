#!/usr/bin/python3
"""
contains the class definition of a city  and an instance
Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy import ForeignKey


class City(Base):
    """ state definition """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
