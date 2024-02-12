#!/usr/bin/python3
"""
User class model that inherits from Base Model class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a user created with atrributes of BaseModel
    Args:
        email: (str)
        password: (str)
        first_name: (str)
        last_name: (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
