#!/usr/bin/python3
"""
This scripts deletes all the that contains 
lettera State objectsfound from the 
database `hbtn_0e_6_usa`.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.contains("a")).all()
    if result is not None:
        for state in result:
            session.delete(state)
    session.commit()
    session.close()
