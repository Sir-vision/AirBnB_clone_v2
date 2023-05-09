#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer


class Review(BaseModel, Base):
    """
    The Review class represents a review information
    It inherits from BaseModel and Base
    Attributes:
         __tablename__ (str): The name of the MySQL table to store Reviews
         places_id (sqlalchemy.String): The id of the place (max 60 characters)
         user_id (sqlalchemy.String): The id of the user (max 60 characters)
         text (sqlalchemy.String): The review text (max 1024 characters)
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
