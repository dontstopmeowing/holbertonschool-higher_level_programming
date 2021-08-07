#!/usr/bin/python3
"""
contains the class State
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Representation of a city"""
    __tablename__ = "cities"
    id = Column('id', Integer, nullable=False,
                autoincrement=True, unique=True, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey(
        'states.id'), nullable=False)
