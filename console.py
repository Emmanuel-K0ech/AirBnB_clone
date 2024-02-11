import cmd
"""This is a custom console for the AirBnB project"""


class HBNBCommand(cmd.Cmd):
    """This is a class implementing a shell environment for a specific use"""

    intro = "Welcome to my cmd, type 'help' for more commands. \n"
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """End Of File exit"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True


"""To run the file as the main program"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
