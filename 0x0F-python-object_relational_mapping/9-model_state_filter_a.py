#!/usr/bin/python3

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
    p = '%a%'
    s = session.query(State).filter(State.name.like(p)).order_by(State.id)
    for state in s:
        print("{}: {}".format(state.id, state.name))

    session.close()
