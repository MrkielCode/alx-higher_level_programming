#!/usr/bin/python3
"""
This class script a insert a state
in database using ORM

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and inserting a state
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)

    query = session.query(State).filter(
        State.name.like("Louisiana")).order_by(State.id).first()
    if query is None:
        print("Not found")
    else:
        print("{}".format(query.id))
    session.close()
