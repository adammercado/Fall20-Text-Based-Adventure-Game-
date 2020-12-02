from Item.item import Item


class Inventory:
    """Represents a collection of Item objects

    Attributes
    ----------
        inventory : list(str)
            list of Item object instances

    Methods
    -------
        __init__(items)
            default constructor initializes list attribute
            by constructing Item objects using parameter list
        convert_inventory_to_json()
            returns list of items in inventory to write to JSON
        display_inventory()
            print information about Item objects in list
        get_inventory_list()
            return inventory as list type
        check_inventory(item_name)
            return boolean based on if item_name is in list or not
        add_item(item)
            Appends item to list
        remove_item(item)
            Removes item if found in list
    """
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
            print("The inventory is empty.")
        else:
            print("\n----- Inventory -----")
            for i, item in enumerate(self.inventory):
                if i != len(self.inventory) - 1:
                    print("\n")

                item.get_item_data()
            print('---------------------')

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

    def remove_item_by_name(self, item):
        for i, obj in enumerate(self.inventory):
            if obj.name.lower() == item.lower():
                del self.inventory[i]
                break
