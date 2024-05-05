#!/usr/bin/python3

"""
Host details of class Place. Extends the BaseModel class
"""

from base_model import BaseModel

class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialise the instance for Place"""
        super().__init__(*args, **kwargs)
