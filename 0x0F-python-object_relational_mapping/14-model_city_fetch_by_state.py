#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

import sqlalchemy
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities_print = session.query(City).join(State).order_by('cities.id')
    for city in cities_print:
        print("{}: ({}) {}".state.name, cities.id, cities.name)

    session.close()
