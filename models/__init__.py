#!/usr/bin/python3
"""
Creating a unique File storage instance for Hbnb
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
