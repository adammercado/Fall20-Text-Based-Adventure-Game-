import json
from Inventory.inventory import Inventory
from Item.item import Item
from TextParser.textParser import TextParser
from Feature.feature import Feature


class Room:
    parser = TextParser()

    def __init__(self, name, longDesc, shortDesc, priorVisit, connections, items, features):
        self.name = name
        self.longDesc = longDesc
        self.shortDesc = shortDesc
        self.priorVisit = bool(priorVisit == "true")
        self.connections = connections
        self.inventory = Inventory()
        self.featureList = []

        directory = "./GameData/Items"

        for item in items:
            if item != None:
                itemName = self.parser.convertSpaces(item.lower())
                itemPath = directory + "/{}.json".format(itemName) 
                curItem = Item.createItemFromFile(itemPath)

                self.inventory.addItem(curItem)

        for obj in features:
            if obj:
                cur = Feature(obj["name"], obj["desc"], obj["isInteractive"], obj["interactions"])
                self.featureList.append(cur)

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
            features = data["features"]

        return Room(name, longDesc, shortDesc, priorVisit, connections, items, features)

    def convertRoomToJson(self):
        jsonInventory = []
        jsonFeatures = []

        for item in self.inventory.getInventoryList():
           jsonInventory.append(item.name)

        for obj in self.featureList:
           jsonFeatures.append(obj.convertFeatureToJson())

        print(jsonFeatures)

        roomData = {
            "name": self.name,
            "longDesc": self.longDesc,
            "shortDesc": self.shortDesc,
            "priorVisit": self.priorVisit,
            "connections": self.connections,
            "inventory": jsonInventory,
            "featureList": jsonFeatures
        }

        return roomData

    def getConnection(self, num):
        return self.connections[num]

    def getFeatures(self):
        for obj in self.featureList:
           obj.getInfo()

    def examine(self, feature):
        print("feature is: " + feature)
        for obj in self.featureList:
            if feature == obj.name:
                obj.getDesc()
                break

    # Test method called when saving room data to json
    def getData(self):
        print(self.name)
        print(self.longDesc)

    # Test method called when loading room data from json
    def getLoadData(self):
        print(self.name)
        print(self.shortDesc)

    def roomAddItem(self, item):
        self.inventory.addItem(item)

    def roomDropItem(self, item):
        for obj in self.inventory.getInventoryList():
            print(obj.name)
            if obj.name.lower() == item and obj.isObtainable():
                print("Match found in room inventory")
                self.inventory.removeItem(obj)
