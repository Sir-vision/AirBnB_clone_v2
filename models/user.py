#!/usr/bin/python3
"""User Module for AirBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Users
        email (sqlalchemy.String): The user's email address (max 128 characters)
        password (sqlalchemy.String): The user's password (max 128 characters)
        first_name (sqlalchemy.String): The user's first name (max 128 characters)
        last_name (sqlalchemy.String): The user's last name (max 128 characters)
        places (sqlalchemy.orm.relationship): A list of places associated with the user
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")
