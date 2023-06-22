#!/usr/bin/python3
""" Select the first item in the table """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from sys import argv

if __name__ == "__main__"
    engine = create_egine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           rgv[2], argv[3], pool_pre_ping=True))

    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
