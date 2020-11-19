import json
from TextParser.textParser import TextParser
from Inventory.inventory import Inventory
from Item.item import Item

class Player:
    parser = TextParser()

    def __init__(self, items):
        self.name = "Boy"
        self.inventory = Inventory(None)
        #directory = "./GameData/Items"
        """
        for item in items:
            if item != None:
                itemName = self.parser.convertSpaces(item.lower())
                itemPath = "{0}/{1}.json".format(directory, itemName) 
                curItem = Item.createItemFromFile(itemPath)

                self.inventory.addItem(curItem)
        """

        if items != None:
            for data in items:
                if data != None:
                    curItem = Item(data["name"], data["description"], data["obtainable"])
                    self.inventory.addItem(curItem)

    def convertPlayerToJson(self):
        playerInventory = self.inventory.convertInventoryToJson()
        
        #for item in self.inventory.getInventoryList():
        #    playerInventory.append(item.name)

        playerData = {
            "name": self.name,
            "inventory": playerInventory
        }

        return playerData 

    def playerAddItem(self, item):
        self.inventory.addItem(item)
        print("{} grabbed the {} and placed it in his inventory.".format(self.name, item.name))

    def playerDropItem(self, item):
        for obj in self.inventory.getInventoryList():
            if obj.name.lower() == item:
                if obj.isObtainable():
                    self.inventory.removeItem(obj)
                    print("{} dropped the {}.".format(self.name, obj.name))

