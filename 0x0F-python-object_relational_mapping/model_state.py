#!/usr/bin/python3
"""
To create a state table and its instance

"""
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

mymetadata = MetaData()
Base = declarative_base(mymetadata)


class State(Base):
    """
    instance of the table state
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
