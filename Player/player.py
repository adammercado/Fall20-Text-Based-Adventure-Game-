import json
from TextParser.textParser import TextParser
from Inventory.inventory import Inventory
from Item.item import Item


class Player:
    parser = TextParser()

    def __init__(self, items):
        self.name = "Boy"
        self.inventory = Inventory(None)

        if items is not None:
            for data in items:
                if data is not None:
                    cur_item = Item(data["name"], data["description"],
                                    data["obtainable"])
                    self.inventory.add_item(cur_item)

    def convert_player_to_json(self):
        player_inventory = self.inventory.convert_inventory_to_json()

        player_data = {
            "name": self.name,
            "inventory": player_inventory
        }

        return player_data

    def player_add_item(self, item):
        self.inventory.add_item(item)
        print("{} grabbed the {} and placed it in his inventory."
              .format(self.name, item.name))

    def player_drop_item(self, item, room_inventory):
        for obj in self.inventory.get_inventory_list():
            if obj.name.lower() == item:
                room_inventory.add_item(obj)
                self.inventory.remove_item(obj)
                print("{} dropped the {}.".format(self.name, obj.name))
