#!/usr/bin/python3
"""
To create a state table and its instance

"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(mymetadata)

class State(Base):
    """
    class of each with instance of the table state

    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
