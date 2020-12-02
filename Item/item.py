import json


class Item:
    """Represents an object in the game

    Attributes
    ----------
        name : str
            name of item
        description: str
            description of item
        obtainable: boolean
            if an object is able to be picked up
    Methods
    -------
        __init__(name, description, obtainable)
            default constructor creates instances using parameters
        create_item_from_file(file_name)
            loads data from JSON file and passes into default constructor
        convert_item_to_json()
            returns object containing item data to write to JSON
        toggle_obtainable()
            toggles obtainable attribute
        is_obtainable()
            returns boolean value of obtainable attribute
        get_description()
            prints item description
        get_item_data()
            prints item name and obtainable attribute
    """

    # Constructor
    def __init__(self, name, description, obtainable):
        self.name = name
        self.description = description
        self.obtainable = obtainable

    def create_item_from_file(file_name):
        with open(file_name, encoding="utf-8") as infile:
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

    def toggle_obtainable(self):
        if self.obtainable:
            self.obtainable = False
        else:
            self.obtainable = True

    def is_obtainable(self):
        return self.obtainable

    def get_description(self):
        print("\n{}".format(self.description))

    def get_item_data(self):
        print("{}".format(self.name))
