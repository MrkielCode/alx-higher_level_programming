#!/usr/bin/python3
"""
class representaion of a state class that
create a state stable

"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(mymetadata)


class State(Base):
    """
    class representaion of state class
    with instance of the class
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
