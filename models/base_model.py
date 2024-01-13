#!/usr/bin/python3
"""Make base module for other classes """

from datetime import datetime
import uuid


class BaseModel:
    """This is the parent class/model"""

    def __init__(self):
        """initialize the BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Display the string representation of the BaseModel class"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """update class"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """convert object to JSON"""
        dc = self.__dict__
        dc['__class__'] = 'BaseModel'
        dc['created_at'] = dc['created_at'].isoformat()
        dc['updated_at'] = dc['updated_at'].isoformat()
        return dc
