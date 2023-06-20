#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).join(City).order_by(City.id).all()

    for state in all_states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
