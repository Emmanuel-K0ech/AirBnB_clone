#!/usr/bin/python3
"""
Module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class city represents the various cities
    Args:
        state_id: (str) -> State.id
        name: (str)
    """
    state_id: str = ""
    name: str = ""
