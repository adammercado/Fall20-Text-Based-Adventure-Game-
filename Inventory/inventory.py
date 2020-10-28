from Item.item import Item
import sys
import random


"""
Methods:
    display_backpack_menu()
    show()
    grab()
    drop() 
"""

class Inventory:
    backpack_list = ["Tome", "Walking Stick"]

# These are the commands that can be used to look at and manipulate objects in the backpack

# Show commands iterates through the list and prints the contents
    def show(self):
        for (i, item) in enumerate(backpack_list):
            print(i, item)
        print()

# Add items to the backpack by appending list
    def grab(self):
        item = input("Name: ")
        backpack_list.append(item)
        print(item + " was added to your backpack.\n")

# Remove items from the backpack using "drop" command.
    def drop(self):
        number = int(input("Which Item Number do you want to drop?: "))
        orig_inp = backpack_list[number]
        del backpack_list[number]
        print("'{}' was deleted.\n".format(orig_inp))
