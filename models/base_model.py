#!/usr/bin/python3
"""
Module for the Base Class
Public instance attributes:
    id
    created_at
    updated_at
Public instance methods
    save(self): updates the 'updated_at' attribute
    to_dict(self) - returns a dictionary
_str_ method to print
"""


from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """This is the base model of the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializes new instances of BaseModel class
        Args:
            *args: positional arguments
            **kwargs: Dictionary representation of an instance
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        'update_at with current datetime
        """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing key/value args of
        _dict_ for an instance
        """
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
