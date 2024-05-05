#!/usr/bin/python3

"""File hosts a user class"""

from base_model import BaseModel

class User(BaseModel):
    "Represents a user"
    
    def __init__(self, *args, **kwargs):
        """Initializes a user"""
        super().__init__(*args, **kwargs)
        
if __name__ == '__main__':
    print("-- Create a new User --")
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"
    my_user.save()
    print(my_user)

    print("-- Create a new User 2 --")
    my_user2 = User()
    my_user2.first_name = "John"
    my_user2.email = "airbnb2@mail.com"
    my_user2.password = "root"
    my_user2.save()
    print(my_user2)