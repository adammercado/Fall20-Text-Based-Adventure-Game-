from Item.item import Item
from copy import deepcopy

"""
Methods:
    __init__(): default constructor initializes empty list
    displayInventory(): prints name and descrption of each item in inventory list
    getInventoryList(): returns list attribute (used for json)
    addItem(itemObj): receives an object of Item class and appends to list
    removeItem(itemName): locates item with matching name in list and deletes from list - UNTESTED
"""

class Inventory:
    def __init__(self):
        self.inventory = []

    # Iterate through list and print name and description of each item object 
    def displayInventory(self):
        if not self.inventory:
            print("THE INVENTORY IS EMPTY")
        else:
            print('\n')
            print("ITEMS IN INVENTORY")
            for item in self.inventory:
                print(item.name)
                print(item.description)
                print('\n')

    def getInventoryList(self):
        return self.inventory

    def checkInventory(self, itemName):
        for item in self.inventory:
            if itemName == item.name.lower():
                return True

        return False

    # Add items to inventory by appending object to list
    def addItem(self, itemObj):
        self.inventory.append(itemObj)

    # Remove items 
    def removeItem(self, item):
        for i, obj in enumerate(self.inventory):
            if obj == item:
                print("match found in delete inventory")
                del self.inventory[i]
                break
