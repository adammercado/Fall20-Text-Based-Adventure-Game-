import json
from Inventory.inventory import inventory
from Item.item import Item


class Room:
    def __init__(self, name, longDesc, shortDesc, priorVisit, connections, items):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc
        self.priorVisit = bool(priorVisit == "true")
        self.connections = connections

        self.inventory = Inventory()

        for item in items:
             


    # Constructor using file name
    def fromFileName(fileName):

        with open(fileName) as infile:
            data = json.load(infile)

            name = data["name"]
            longDesc = data["longDesc"]
            shortDesc = data["shortDesc"]
            priorVisit = data["priorVisit"]
            connections = data["connections"]
            items = data["items"]

        return Room(name, longDesc, shortDesc, priorVisit, connections, items)

    def getConnection(self, num):
        return self.connections[num]

    # Test method called when saving room data to json
    def getData(self):
        print(self.name)
        print(self.longDesc)

    # Test method called when loading room data from json
    def getLoadData(self):
        print(self.name)
        print(self.shortDesc)

