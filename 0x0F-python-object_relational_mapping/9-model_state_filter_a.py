#!/usr/bin/python3
""" Lists all State objects that contain the letter a from the database """
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    states = session.query(State).filter(State.name.like("%a%")).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
