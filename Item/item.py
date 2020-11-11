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
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def createItemFromFile(fileName):
        with open(fileName) as infile:
            data = json.load(infile)

            name = data["name"]
            description = data["description"]

        return Item(name, description)
