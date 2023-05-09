#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class DBStorage:
    """Represents a database storage engine
    Attributes:
        __engine (sqlalchemy.Engine): The SQLAlchemy engine
        __session (sqlalchemy.Session): The SQLAlchemy session
        """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session all objects of the given class.
        If cls is None, queries all types of objects.
        Return:
            Dict. of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls:
            if type(cls) == str:
                results = self.__session.query(eval(cls)).all()
        else:
            results = self.__session.query(State).all()
            results.extend(self.__session.query(City).all())
            results.extend(self.__session.query(User).all())
            results.extend(self.__session.query(Place).all())
#            results.extend(self.__session.query(Review).all())
#            results.extend(self.__session.query(Amenity).all())

        return {f"{type(obj).__name__}.{obj.id}": obj for obj in results}

    def new(self, obj):
        """Add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Close the working SQLAlchemy session"""
        self.__session.close()
