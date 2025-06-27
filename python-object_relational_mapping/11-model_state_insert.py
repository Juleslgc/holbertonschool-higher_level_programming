#!/usr/bin/python3
"""
Adds the State objects 'Louisiana' to the database hbtn_0e_6_usa.
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

    new_data = State(name="Louisiana")
    session.add(new_data)
    session.commit()

    print(new_data.id)

    session.close()
