#!/usr/bin/python3
"""This module defines a HBNBCommand class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines a HBNBCommand."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exits the program."""
        print()
        return True

    def emptyline(self):
        """shouldn’t execute anything."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
