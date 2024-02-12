#!/usr/bin/python3
"""
Module for the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Handles The reviews given by users
    Args:
        place_id: (str) -> Place.id
        user_id: (str) -> User.id
        text: (str)
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
