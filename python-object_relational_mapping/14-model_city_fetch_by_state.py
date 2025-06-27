#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
from model_state import Base, State
from model_city import City
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

    cities_states = session.query(City, State).join(State).all()

    for city, state in cities_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
