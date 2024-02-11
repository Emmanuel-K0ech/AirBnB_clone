#!/usr/bin/python3
"""
This is a unique File storage instance for the AirBnB Clone
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
