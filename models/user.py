#!/usr/bin/python3
"""User script"""

from datetime import datetime
from models.base_model import BaseModel
from models.__init__ import storage


class User(BaseModel):
    """ define airbnb users """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def save(self):
        """ """
        storage.new(self)
        storage.save()
