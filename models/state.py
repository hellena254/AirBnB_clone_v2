#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ The State class, contains information about states """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship(
        "City",
        cascade="all, delete",
        backref="state"
    )

    # For FileStorage
    @property
    def cities(self):
        """Getter attribute for cities"""
        from models import storage
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
