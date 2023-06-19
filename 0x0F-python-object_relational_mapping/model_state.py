#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, Sequence('states_id'), primary_key=True)
    name = Column(String(128), nullable=False)
