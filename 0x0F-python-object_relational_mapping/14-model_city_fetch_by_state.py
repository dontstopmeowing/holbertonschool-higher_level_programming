#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = session.query(City, State).filter(City.state_id == State.id)
        for city, state in result:
            print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))
    except Exception:
        print("Encountered a general SQLAlchemyError. Call 911 immediately!")
    finally:
        session.close()
