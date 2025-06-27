#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa.
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

    states = session.query(State).order_by(asc(State.id)).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
