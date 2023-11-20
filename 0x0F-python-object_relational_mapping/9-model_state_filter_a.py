#!/usr/bin/python3
"""
This class script a state that contain "a"
in database using ORM

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and listing the state
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in query:
        print("{}: {}".format(state.id, state.name))
    session.close()
