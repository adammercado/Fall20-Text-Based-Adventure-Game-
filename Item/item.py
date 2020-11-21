import json


class Item:
    """The item class is used to represent the objects
      that can be acquired during gameplay.

      Attribute(s):
      - Name (string)
      - Description (string)
      
      Method(s):
    """
   
    # Constructor
    def __init__(self, name, description, obtainable):
        self.name = name
        self.description = description
        self.obtainable = obtainable

    def create_item_from_file(self, file_name):
        with open(file_name) as infile:
            data = json.load(infile)

            name = data["name"]
            description = data["description"]
            obtainable = data["obtainable"]

        return Item(name, description, obtainable)

    def convert_item_to_json(self):
        item_data = {
            "name": self.name,
            "description": self.description,
            "obtainable": self.obtainable
        }

        return item_data

    def is_obtainable(self):
        return self.obtainable

    def get_description(self):
        print(self.description)
