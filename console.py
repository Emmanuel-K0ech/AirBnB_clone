#!/usr/bin/python3
"""This is a custom console for the AirBnB project"""
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """This is a class implementing a shell environment for a specific use"""

    prompt = "(hbnb) "

    def emptyline(self):
        """called when empty line is entered"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """End Of File - exit program"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        obj_bm = None

        if not args:
            print("** class name missing **")
        elif args != 'BaseModel':
            print("** class doesn't exist **")
        else:
            obj_bm = BaseModel()
            storage.save()
            print(obj_bm.id)

    def do_show(self, args):
        """
        Shows string representation of an instance
        based on the class name an id of the instance
        """
        pass#for now


"""To run the file as the main program"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
