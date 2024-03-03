#!/usr/bin/python3
"""This module defines a HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class defines a HBNBCommand."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User
        "Amenity": Amenity
        "Place": Place
        "Review": Review
        "State": State
        "City" City
    }

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

    def do_create(self, line):
        """Creates a new instance"""
        args = line.split(" ")
        if args == ['']:
            result = "** class name missing **"
        elif args[0] not in self.classes:
            result = "** class doesn't exist **"
        else:
            base = self.classes[args[0]]()
            base.save()
            result = base.id
        print(result)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split(" ")
        if args == ['']:
            result = "** class name missing **"
        elif args[0] not in self.classes:
            result = "** class doesn't exist **"
        elif len(args) != 2:
            result = "** instance id missing **"
        else:
            result = "** no instance found **"
            for k, v in storage.all().items():
                if k == f"{args[0]}.{args[1]}":
                    result = v
                    break
        print(result)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split(" ")
        if args == ['']:
            result = "** class name missing **"
        elif args[0] not in self.classes:
            result = "** class doesn't exist **"
        elif len(args) != 2:
            result = "** instance id missing **"
        else:
            result = "** no instance found **"
            for k, v in storage.all().items():
                if k == f"{args[0]}.{args[1]}":
                    del storage.all()[k]
                    storage.save()
                    return
        print(result)

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = line.split(" ")
        if args == ['']:
            result = [str(v) for v in storage.all().values()]
        elif args[0] not in self.classes:
            result = "** class doesn't exist **"
        else:
            result = [str(v) for k, v in storage.all().items() if k.split(".")[0] == args[0]]
        print(result)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = line.split(" ")
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
