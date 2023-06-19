#!/usr/bin/python3
"""
all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3], argv[4]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
