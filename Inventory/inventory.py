from Item.item import Item

"""
Methods:
    __init__(): default constructor initializes empty list
    displayInventory(): prints name and description of each item
    getInventoryList(): returns list attribute (used for json)
    addItem(itemObj): receives an object of Item class and appends to list
    removeItem(itemName): locates item in list and deletes
"""


class Inventory:
    def __init__(self, items):
        self.inventory = []

        if items is not None:
            for obj in items:
                cur_item = Item(obj["name"], obj["description"],
                                obj["obtainable"])
                self.add_item(cur_item)

    def convert_inventory_to_json(self):
        inventory_data = []

        for item in self.inventory:
            cur = item.convert_item_to_json()
            inventory_data.append(cur)

        return inventory_data

    # Iterate through list and print name and description of each item object
    def display_inventory(self):
        if not self.inventory:
            print("THE INVENTORY IS EMPTY")
        else:
            print('\n')
            print("ITEMS IN INVENTORY")
            for item in self.inventory:
                print(item.name)
                print(item.description)
                print('\n')

    def get_inventory_list(self):
        return self.inventory

    def check_inventory(self, item_name):
        for item in self.inventory:
            if item_name == item.name.lower():
                return True

        return False

    # Add items to inventory by appending object to list
    def add_item(self, item):
        self.inventory.append(item)

    # Remove items
    def remove_item(self, item):
        for i, obj in enumerate(self.inventory):
            if obj == item:
                del self.inventory[i]
                break
