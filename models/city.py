#!/usr/bin/python3

"""
Host details of class City. Extends the BaseModel class
"""

from base_model import BaseModel


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialise the instance for City"""
        super().__init__(*args, **kwargs)
