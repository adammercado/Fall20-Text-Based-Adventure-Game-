import json
from Inventory.inventory import Inventory
from Item.item import Item


class Room:
    def __init__(self, name, longDesc, shortDesc, priorVisit, connections, items):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc
        self.priorVisit = bool(priorVisit == "true")
        self.connections = connections

        self.inventory = Inventory()
        directory = "./GameData/Items"

        for item in items:
            itemName = item.lower()
            itemPath = "{0}/{1}.json".format(directory, itemName) 
            curItem = Item.createItemFromFile(itemPath)
            self.inventory.addItem(curItem)

        self.inventory.displayInventory()

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

    def convertRoomToJson(self):
        jsonInventory = []

        for item in self.inventory.getInventoryList():
           jsonInventory.append(item.name)

        roomData = {
            "name": self.name,
            "longDesc": self.longDesc,
            "shortDesc": self.shortDesc,
            "priorVisit": self.priorVisit,
            "connections": self.connections,
            "inventory": jsonInventory
        }

        return roomData

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

