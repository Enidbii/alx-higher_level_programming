#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_id = session.query(State).filter_by(id=2).first()
    new_id.name = 'New Mexico'
    session.commit()
