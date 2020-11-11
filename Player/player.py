import sys
import json
import os
from pathlib import Path
from TextParser.textParser import TextParser
from Room.room import Room
from Inventory.inventory import Inventory
from Item.item import Item

class Player:
    playerName = ""
    inventory = Inventory()

    def initializePlayer(self):
        self.playerName = input("Enter a name: ")

    def playerTake(self, item):
        print("Command: Take " + item)
        print("You grabbed the " + item + "!")

        if item == "key":
            item1 = Item(item, "Use to open something...")
            self.inventory.addItem(item1)
        if item == "hammer":
            item2 = Item(item, "use to smash something...")
            self.inventory.addItem(item2)

        #print the items to verify the inventory is being updated
        self.inventory.displayInventory()

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







