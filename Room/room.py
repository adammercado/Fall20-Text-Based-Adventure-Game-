import json
from Inventory.inventory import Inventory
from Item.item import Item
from TextParser.textParser import TextParser
from Feature.feature import Feature


class Room:
    parser = TextParser()

    def __init__(self, name, long_desc, short_desc, prior_visit,
                 connections, items, features, load):
        self.name = name
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.prior_visit = bool(prior_visit == "true")
        self.connections = connections
        self.inventory = Inventory(None)
        self.feature_list = []

        directory = "./GameData/Items"

        for item in items:
            if item is not None and not load:
                item_name = self.parser.convert_spaces(item.lower())
                item_path = directory + "/{}.json".format(item_name)
                cur_item = Item.create_item_from_file(item_path)
                self.inventory.add_item(cur_item)
            elif item is not None and load:
                self.inventory = Inventory(items)

        for obj in features:
            if obj:
                cur = Feature(obj["name"], obj["desc"],
                              obj["is_interactive"], obj["interactions"])
                self.feature_list.append(cur)

    # Constructor using file name
    def from_file_name(file_name):
        with open(file_name, encoding="utf-8") as infile:
            data = json.load(infile)

            name = data["name"]
            long_desc = data["long_desc"]
            short_desc = data["short_desc"]
            prior_visit = data["prior_visit"]
            connections = data["connections"]
            items = data["items"]
            features = data["features"]

        return Room(name, long_desc, short_desc, prior_visit,
                    connections, items, features, False)

    def convert_room_to_json(self):
        json_inventory = self.inventory.convert_inventory_to_json()
        json_features = []

        # for item in self.inventory.getInventoryList():
        #   json_inventory.append(item.name)

        for obj in self.feature_list:
            json_features.append(obj.convert_feature_to_json())

        # print(json_features)

        room_data = {
            "name": self.name,
            "long_desc": self.long_desc,
            "short_desc": self.short_desc,
            "prior_visit": self.prior_visit,
            "connections": self.connections,
            "inventory": json_inventory,
            "feature_list": json_features
        }

        return room_data

    def get_connection(self, num):
        return self.connections[num]

    def get_features(self):
        for obj in self.feature_list:
            obj.get_feature_info()

    def examine(self, feature):
        print("feature is: " + feature)
        for obj in self.feature_list:
            if feature == obj.name:
                obj.get_desc()
                break

    # Test method called when saving room data to json
    def get_long_desc(self):
        print(self.name)
        print(self.long_desc)

    # Test method called when loading room data from json
    def get_short_desc(self):
        print(self.name)
        print(self.short_desc)

    def room_add_item(self, item):
        self.inventory.add_item(item)

    def room_drop_item(self, item, player_inventory):
        for obj in self.inventory.get_inventory_list():
            print(obj.name)
            print(item)
            if obj.name.lower() == item:
                if obj.is_obtainable():
                    print("dropping item")
                    player_inventory.add_item(obj)
                    self.inventory.remove_item(obj)
        # for obj in self.inventory.get_inventory_list():
        #     if obj.name.lower() == item:
        #         if obj.is_obtainable():
        #
        #             self.inventory.remove_item(obj)
        #             return
        #
        # return False
