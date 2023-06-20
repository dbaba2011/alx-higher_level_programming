#!/usr/bin/python3
"""
This script join states and city table together
and display the result State objects
from the database `hbtn_0e_6_usa`.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_results = session.query(City, State).join(State)

    for city, state in all_results.all():
        print(f"{state.name}: {city.id} {city.name}")
