#!/usr/bin/python3
"""
Prints the State objects with the name passed
as argument from the database hbtn_0e_6_usa.
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()

    place = sys.argv[4]
    states = session.query(State).filter(State.name == place).all()

    for state in states:
        print(f"{state.id}")

    session.close()
