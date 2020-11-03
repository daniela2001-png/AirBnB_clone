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
    clases = ("BaseModel")

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

    def do_create(self, inp):
        """ Creates a new instance of BaseModel, saves it and prints the id """
        if len(inp.split()) == 1:
            if inp in self.clases:
                new_inst = 0
                if inp == 'BaseModel':
                    new_inst = BaseModel()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, input):
        """
        show the string representation of a instance
        form the class name and id
        """
        if len(input) != 0:
            if input.split()[0] in self.clases:
                if len(input.split()) >= 2:
                    key = input.split()[0] + "." + input.split()[1]
                    if key in storage.all():
                        a = storage.all()
                        print(a[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, input):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        ex: destroy BaseModel 3645237654
        """
        if len(input) != 0:
            if input.split()[0] in self.clases:
                if len(input.split()) >= 2:
                    key = input.split()[0] + "." + input.split()[1]
                    if key in storage.all():
                        a = storage.all()
                        del a[key]
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, input):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all"""
        if len(kika) == 0:
            print([str(v) for v in storage.all().values()])

        elif kika not in self.clases:
            print('** class doesn\'t exist **')
        else:
            print([str(v) for k, v in storage.all().items() if kika in k])

    def do_update(self, input):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        if len(input) != 0:
            if input.split()[0] in self.clases:
                if len(input.split()) >= 2:
                    key = input.split()[0] + "." + input.split()[1]
                    if key in storage.all():
                        if len(input.split()) > 2:
                            if len(input.split()) <= 3:
                                print("** value missing **")
                            else:
                                a = storage.all()
                                my_dict = a[key].__dict__
                                lista = input.split()
                                value_1 = lista[3][1:-1]
                                key_1 = lista[2]
                                my_dict[key_1] = value_1
                                storage.save()
                                # print(a[key])
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
