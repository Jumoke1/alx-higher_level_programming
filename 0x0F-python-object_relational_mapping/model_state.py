#!/usr/bin/python
"""Defines a state model class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declaratie_base()


class state(Base):
    """Represent a state for mysql database
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name
    """

    __tablename__ = "states"
    id = Column (Integer primary_key = True)
    name = Column (String(128) nullable = false)
