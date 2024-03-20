#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """ The Amenity class, contains information about amenities """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # Relationship with Place class, many-to-many
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        viewonly=False
    )
