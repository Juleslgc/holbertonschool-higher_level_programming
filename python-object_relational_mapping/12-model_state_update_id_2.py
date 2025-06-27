#!/usr/bin/python3
"""
Updates the name of the State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa.
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).first()

    if states:
        states.name = "New Mexico"
        session.commit()

    session.close()
