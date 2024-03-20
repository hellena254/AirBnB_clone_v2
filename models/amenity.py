#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """ The Amenity class, contains information about amenities """
    __tablename__ = 'amenities'  # Table name in the database

    name = Column(String(128), nullable=False)  # Name column, cannot be null

    # Relationship with Place class, many-to-many
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        viewonly=False
    )
