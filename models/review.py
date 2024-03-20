#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship



class Review(BaseModel, Base):
    """ The review class, contains text, place ID, and user ID """
    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
