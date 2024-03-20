#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


# Define the association table for many-to-many relationship
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)



class Place(BaseModel, Base):
    """ A place class """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
#    amenity_ids = []
    reviews = relationship('Review', cascade="all, delete, delete-orphan", backref='place')

    # For DBStorage
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        viewonly=False
    )

    # For FileStorage
    @property
    def amenities(self):
        """Getter attribute for amenities"""
        amenities_list = []
        for amenity_id in self.amenity_ids:
            amenity = models.storage.get(Amenity, amenity_id)
            if amenity:
                amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities(self, amenity):
        """Setter attribute for amenities"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
