#!/usr/bin/python3

"""
is the console to developer
"""
from cmd import Cmd
import sys
from models.base_model import BaseModel
import json
from models import storage


class HBNBCommand(Cmd):
    """contains the entry point of the command interpreter"""
    if sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)' + '\n'

    def do_quit(self, input):
        """ Is the function it will exit the program """
        return True

    def emptyline(self):
        """This function doesnt do anything"""
        pass

    def do_EOF(self, input):
        """ Is the function it will exit the program """
        print()
        return True

    def help_quit(self):
        """ Is for help to thought the console"""
        print("To exit put the commands: quit or CTRL + D")

    def do_create(self, input):
        """
        create objects
        """
        if len(input) > 1:
            if input == "BaseModel":
                new = BaseModel()
                storage.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
