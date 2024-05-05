#!/usr/bin/python3

"""
Host details of class Amenity. Extends the BaseModel class
"""

from base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialise the instance for Amenity"""
        super().__init__(*args, **kwargs)
