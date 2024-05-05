#!/usr/bin/python3

""" console """

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNH console"""
    prompt = '(hbnb)'
    
    def do_EOF(self, arg):
        """command to exit the console"""
        return True
    
    def emptyline(self):
        """command to overwrite an emptyline method"""
        return False
    
    def do_quit(self):
        """Quit command to exit the program"""
        return True
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
