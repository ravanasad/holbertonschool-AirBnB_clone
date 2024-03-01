import cmd
"""This module defines a HBNBCommand class."""


class HBNBCommand(cmd.Cmd):
    """This class defines a HBNBCommand."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the program."""
        return True

    def do_EOF(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Does nothing on an empty line."""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
