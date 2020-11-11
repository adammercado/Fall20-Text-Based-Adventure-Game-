import json
from TextParser.textParser import TextParser
from Inventory.inventory import Inventory
from Item.item import Item

class Player:
    parser = TextParser()

    def __init__(self, items):
        self.name = "Boy"
        self.inventory = Inventory()
        directory = "./GameData/Items"

        for item in items:
            if item != None:
                itemName = self.parser.convertSpaces(item.lower())
                itemPath = "{0}/{1}.json".format(directory, itemName) 
                curItem = Item.createItemFromFile(itemPath)

                self.inventory.addItem(curItem)

    def convertPlayerToJson(self):
        playerInventory = []
        
        for item in self.inventory.getInventoryList():
            playerInventory.append(item.name)

        playerData = {
            "name": self.name,
            "inventory": playerInventory
        }

        return playerData 

    def playerAddItem(self, item):
        self.inventory.addItem(item)
        print("{0} grabbed the {1}!".format(self.name, item.name))
        #self.inventory.displayInventory()

    def playerPlace(self, item):
        print("Command: Place " + item)
        print("in PlayerPlace")

        if item == "key":
            self.inventory.removeItem("key")
            print("The key was dropped.")
        if item == "hammer":
            self.inventory.removeItem("hammer")
            print("The hammer was dropped.")

        #print items in inventory to verify they are being dropped
        self.inventory.displayInventory()

