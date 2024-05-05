#!/usr/bin/python3

"""File hosts a user class"""

from base_model import BaseModel

class User(BaseModel):
    "Represents a user"
    
    def __init__(self, *args, **kwargs):
        """Initializes a user"""
        super().__init__(*args, **kwargs)
