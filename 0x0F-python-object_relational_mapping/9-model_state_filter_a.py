#!/usr/bin/python3
"""
Script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = session.query(State).filter(State.name.like('%a%'))
        for row in result:
            print("{:d}: {:s}".format(row.id, row.name))
    except Exception:
        print("Nothing")
    finally:
        session.close()
