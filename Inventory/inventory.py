from Item.item import Item


"""
Methods:
    display_backpack_menu()
    show()
    grab()
    drop() 
"""

class Inventory:
    def __init__(self):
        self.inventory = []

# Show commands iterates through the list and prints the contents
    def displayInventory(self):
        for item in self.inventory:
            print(item.name)

# Add items to the backpack by appending list
    def addItem(self, itemObj):
        self.inventory.append(itemObj)

# Remove items from the backpack using "drop" command.
    def removeItem(self, itemName):
        for i, o in enumerate(self.inventory):
            if o.name == itemName:
                del self.inventory[i]
                break
                      
