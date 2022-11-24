#!/usr/bin/python3
""""
new engine
"""


from sqlalchemy import create_engine
from models.base_model import Base
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """"
    i still dont know why m building this class tbh...
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        creating self engine
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict = {}
        if cls is None:
            for c in self.all_classes:
                c = eval(c)
                for instance in self.__session.query(c).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    dict[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                dict[key] = instance
        return dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):

        self.__session.commit()

    def delete(self, obj=None):

        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        dbsession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(dbsession)
        self.__session = Session()
