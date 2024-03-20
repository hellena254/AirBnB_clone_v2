#!/usr/bin/python3
"""Engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

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
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """Query objects fro current db session"""
        obj_dict = dict()
        classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_typ in classes:
                query = self.__session.query(class_typ)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    obj_dict[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                obj_dict[obj_key] = obj
        return obj_dict


    def new(self, obj):
        """Add the object to the current databse session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as exception:
                self.__session.rollback()
                raise exception


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
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """close function"""
        self.__session.close()
