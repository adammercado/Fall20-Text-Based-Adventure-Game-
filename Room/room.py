import json
from Inventory.inventory import Inventory
from Item.item import Item
from TextParser.textParser import TextParser
from Feature.feature import Feature


class Room:
    """Represents a room in the game

    Attributes
    ----------
        name : str
            name of room
        long_desc : str
            long description displayed on first visit
        short_desc : str
            short description displayed upon repeat visit
        prior_visit : boolean
            status if room has been visited before
        connections : list(str)
            list of names of adjacent rooms
        inventory : Inventory
            contains item objects in room
        feature_list : list(Feature)
            list of features in room
        parser : TextParser
            used to parse item name inputs
    Methods
    -------
        __init__(name, long_desc, short_desc, prior_visit,
                 connections, items, features, load)
            default constructor creates instances using parameters
        from_file_name(file_name)
            method calls constructor using parameters from JSON file
        convert_room_to_json
            returns list of strings representing room attributes
        get_connection(num):
            returns name of adjjacent room at index
        get_feature():
            returns list of features in room
        examine(feature):
            searches for feature in room and displays description
        get_desc():
            print descriptions based on status of prior_visit
        get_long_desc():
            print long_desc
        get_short_desc():
            print short_desc
        room_add_item(item):
            add item to room inventory
        room_drop_item(item):
            drop item from room inventory
        toggle_visit():
            toggle prior_visit from False to True
    """
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

        for obj in self.feature_list:
            json_features.append(obj.convert_feature_to_json())

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
        for obj in self.feature_list:
            if feature == obj.name:
                obj.get_desc()
                break

    def get_desc(self):
        if self.prior_visit:
            print(self.short_desc)
        else:
            print(self.long_desc)

    def get_long_desc(self):
        print(self.long_desc)

    def get_short_desc(self):
        print(self.short_desc)

    def room_add_item(self, item):
        self.inventory.add_item(item)

    def room_drop_item(self, item, player_inventory):
        for obj in self.inventory.get_inventory_list():
            if obj.name.lower() == item:
                if obj.is_obtainable():
                    player_inventory.add_item(obj)
                    self.inventory.remove_item(obj)

    def toggle_visit(self):
        if not self.prior_visit:
            self.prior_visit = True
