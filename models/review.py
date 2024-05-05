#!/usr/bin/python3

"""
Host details of class Review. Extends the BaseModel class
"""

from base_model import BaseModel

class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialise the instance for Review"""
        super().__init__(*args, **kwargs)
