#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True)
)


"""
Represents the many to many relationship table between Place and Amenity records.
"""


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
    amenity_ids = []
    reviews = relationship('Review', cascade="all, delete, delete-orphan", backref='place'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, backref='place_amenities')
    else:
        @property
        def amenities(self):
            """Returns the amenities"""
            from models import storage
            amenities_place = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_place.append(value)
            return amenities_place

        @amenities.setter
        def amenities(self, value):
            """Adds an amenity"""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Returns the reviews"""
            from models import storage
            reviews_place = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_place.append(value)
            return reviews_place
