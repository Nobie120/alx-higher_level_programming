#!/usr/bin/python3
"""
Contains aa class defination of a state and
Base instance
"""
import sqlalchemy
from relationship_city import Base, City
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(Base):
    """State representation"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
