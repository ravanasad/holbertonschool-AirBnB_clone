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

    def do_help(self, arg):
        """Prints help for the given command."""
        cmd.Cmd.do_help(self, arg)

    def help_quit(self):
        """Prints help for the quit command."""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """Prints help for the EOF command."""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """Does nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
