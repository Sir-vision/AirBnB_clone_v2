#!/usr/bin/python3
""" Place Module for the AirBnB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """
    The Place class represents a place
    It inherits from BaseModel and Base
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Places
        city_id (sqlalchemy.String): The id of the city
        user_id (sqlalchemy.String): The id of the user who owns the place
        name (sqlalchemy.String): The name of the place
        description (sqlalchemy.String): A brief description of the place
        number_rooms (sqlalchemy.String): The number of bedrooms in the place
        number_bathrooms (sqlalchemy.Integer): The number of bathrooms
        max_guest (sqlalchemy.Integer): The max number of guests allowed
        price_by_night (sqlalchemy.Integer): The price per night
        latitude (sqlalchemy.Float): The latitude coordinate of the place
        longitude (sqlalchemy.Float): The longitude coordinate of the place
        amenity_ids: A list of amenity ids associated with the place
        reviews: A list of all reviews associated with the place
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(60), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
#        amenities = relationship('Amenity', secondary='place_amenity',
#                                  viewonly=False)
    else:
        @property
        def reviews(self):
            """
            Gets a list of all reviews associated with the place
            Returns:
                A list of Review objects associated with this Place
            """
            from models import storage, Review

            reviews = []
            for review in storage.all(Review).values():
                if review.places_id == self.id:
                    reviews.append(review)
            return reviews

#        @property
#        def amenities(self):
            """
            Gets a list of all amenities associated with the place
            Returns:
                A list of amenity objects associated with this Place
            """
#            from models import storage, Amenity

#            amenities = []
#            for amenity in storage.all(Amenity).values():
#                if amenity.id == self.amenity_id:
#                    amenities.append(amenity)
#            return amenities
            
            

#        @amenities.setter
#        def amenities(self, amenity):
            """
            Setter method for the 'amenities' attribute of the 'Place' class.
            Args:
                amenity (Amenity): An instance of the 'Amenity' class to be added
                to the 'amenity_ids' relationship.
            Returns:
                None: If the argument is not an instance of the 'Amenity' class.
            """
#            if isinstance(amenity, Amenity):
#                self.amenity_ids.append(amenity)

# an instance of SQLAlchemy Table for creating the relationship
# Many-To-Many between Place and Amenity
#place_amenity = Table('place_amenity', Base.metadata,
#                      Column('place_id', String(60), ForeignKey('places.id'),
#                             primary_key=True, nullable=False),
#                      Column('amenity_id', String(60),
#                             ForeignKey('amenities.id'),
#                             primary_key=True, nullable=False)
#                      )
