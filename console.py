#!/usr/bin/python3

"""
is the console that will be manage
by developer
"""
from models import storage
import json
from cmd import Cmd
import sys
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place


class HBNBCommand(Cmd):
    """contains the entry point of the command interpreter"""
    if sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)' + '\n'
    clases = ("BaseModel", "User", "Amenity",
              "City", "State", "Place", "Review")

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
                elif inp == "User":
                    new_inst = User()
                elif inp == "Amenity":
                    new_inst = Amenity()
                elif inp == "Place":
                    new_inst = Place()
                elif inp == "City":
                    new_inst = City()
                elif inp == "State":
                    new_inst = State()
                elif inp == "Review":
                    new_inst = Review()
                print(new_inst.id)
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
                print("** class doesn\'t exist **")
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
                        storage.save()
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
        if len(input) == 0:
            print([str(v) for v in storage.all().values()])

        elif input not in self.clases:
            print('** class doesn\'t exist **')
        else:
            print([str(v) for k, v in storage.all().items() if input in k])

    def do_update(self, args):
        """ This will update the json file"""
        args = args.split()

        if len(args) != 0:
            if args[0] in self.clases:
                if len(args) == 1:
                    print('** instance id missing **')
                else:
                    key = args[0] + '.' + args[1]
                    if key in storage.all():
                        if len(args) > 2:
                            if len(args) <= 3:
                                print('** value missing **')
                            else:
                                setattr(
                                    storage.all()[key],
                                    args[2],
                                    args[3][1:-1])
                                storage.all()[key].save()
                        else:
                            print('** attribute name missing **')
                    else:
                        print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
