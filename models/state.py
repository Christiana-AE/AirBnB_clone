#!/usr/bin/python3

"""
Host details of class State. Extends the BaseModel class
"""

from base_model import BaseModel

class State(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialise the instance for State"""
        super().__init__(*args, **kwargs)