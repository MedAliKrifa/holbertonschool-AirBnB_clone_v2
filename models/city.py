#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable = False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable = False)
    places = relationship("Place",  backref="cities")

    def __init__(self, *args, **kwargs):
        """
            Init for inherited
        """
        super().__init__(*args, **kwargs)