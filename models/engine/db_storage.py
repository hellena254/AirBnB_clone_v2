#!/usr/bin/python3
"""Engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """DBStorage class for managing database storage"""
    __engine = None
    __session = None


    def __init__(self):
        """Initializing DBStorage instance"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB))
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """Query objects fro current db session"""
        obj_dict = dict()
        classes = (User, State, City, Amenity, Place, Review)
        for cls in classes:
            if i is None or i is classes[cls] or i is cls:
                objects = self.__session.query(classes[cls]).all()
                for obj in objects:
                    keys = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[keys] = obj
        return (obj_dict)


    def new(self, obj):
        """Add the object to the current databse session"""
        self.__session.add(obj)


    def save(self):
        """Commit all changes to the current db session"""
        self.__session.commit()


    def delete(self, obj=None):
        """Delete the object from the current db session"""
        if obj is not None:
            self.__session.delete(obj)


    def reload(self):
        """Create all tables in the database and recreate the current database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """close function"""
        self.__session.close()
