import sys
import json
import os
from pathlib import Path
from TextParser.textParser import TextParser
from Room.room import Room
from Inventory.inventory import Inventory
from Item.item import Item

"""
Methods:
    startGame()
    saveGame()
    loadGame()
    getInput()

    -- TEMPORARY ATTRIBUTES TO BE REPLACED/CHANGED--
    playerName

    -- TEMPORARY METHODS TO BE REPLACED/CHANGED --
    playerLook()
    playerMove()
    playerUse()
    playerTake() - currently creates an object with the input name and adds it to Game's inventory with a temporary description; GAME WILL NOT HAVE AN INVENTORY LATER ON - this is just for testing
    playerPlace()
    playerGame()
"""


class Game:
    parser = TextParser()
    playerName = ""
    location = None
    inventory = Inventory()
    rooms = []

    def startGame(self):
        directory = "./GameData/RoomTypes"

        # Iterate through each .json file in directory of room types, pass into constructor using file name
        for fileName in os.listdir(directory):
            if fileName.endswith(".json"):
                roomPath = directory + "/" + fileName
                curRoom = Room.fromFileName(roomPath)

                if curRoom.name == "Serene Forest - South":
                    self.location = curRoom

                self.rooms.append(curRoom)

            else:
                continue

        self.playerName = input("Enter a name: ")
        self.playGame()

    def saveGame(self):
        jsonCurLocation = json.dumps(self.location.__dict__)
        jsonRoomsList = json.dumps([obj.__dict__ for obj in self.rooms])
        jsonInventory = json.dumps([obj.__dict__ for obj in self.inventory.getInventoryList()])

        data = {
            "name": self.playerName,
            "location": jsonCurLocation,
            "inventory": jsonInventory,
            "rooms": jsonRoomsList
        }

        with open("./Saves/gameSave.json", "w") as outfile:
            json.dump(data, outfile, indent=4)

        print("Game saved successfully.")

    def loadGame(self):
        saveFile = Path("./Saves/gameSave.json")

        if saveFile.is_file():
            with open("./Saves/gameSave.json") as infile:
                data = json.load(infile)

                self.playerName = data["name"]
                # Receive json list of strings representing inventory and rooms
                tempLocation = json.loads(data["location"])
                tempInventoryList = json.loads(data["inventory"])
                tempRoomList = json.loads(data["rooms"])

                print("TEST - Player Name is " + self.playerName)

                self.location = Room(tempLocation['name'], tempLocation['longDesc'], tempLocation['shortDesc'], tempLocation['priorVisit'], tempLocation['connections'])

                # Convert inventory list received from json back into item objects
                for item in tempInventoryList:
                    curItem = Item(item['name'], item['description'])
                    self.inventory.addItem(curItem)

                # Convert room list received from json back into room objects
                for room in tempRoomList:
                    # Re-create Room objects using list of strings using default constructor
                    curRoom = Room(room['name'], room['longDesc'], room['shortDesc'], room['priorVisit'], room['connections'])
                    self.rooms.append(curRoom)

            self.playGame()
        else:
            print("No save file found. Creating a new game...")
            self.startGame()


    # Tokenize input and pass into class method
    def playGame(self):
        while 1:
            print("Current location: " + self.location.name)

            args = input("Enter an action: ").lower().split()
            self.getInput(args)

    # Receive tokenized input as list and pass to parser to determine command
    def getInput(self, args):
        parsedText = self.parser.parse(args)

        if len(parsedText) == 0:
            print("Not a valid action.")

        elif parsedText[0] == "quit":
            print("Exiting gameplay")
            sys.exit()

        elif parsedText[0] == "look":
            direction = ""

            if len(parsedText) == 2:
                direction = parsedText[1]

            self.playerLook(direction)

        elif parsedText[0] == "move":
            direction = ""

            if len(parsedText) == 2:
                direction = parsedText[1]
                self.playerMove(direction)
            else:
                print("You must enter a cardinal direction to move in.")

        elif parsedText[0] == "use":
            self.playerUse("item")

        elif parsedText[0] == "take":
            self.playerTake(parsedText[1])

        elif parsedText[0] == "place":
            self.playerPlace(parsedText[1])
            
        elif parsedText[0] == "savegame":
            self.saveGame()

        elif parsedText[0] == "loadgame":
            self.loadGame()

        elif parsedText[0] == "inventory":
            self.inventory.displayInventory()

        elif parsedText[0] == "help":
            print("Display help menu here")

# PLACEHOLDER METHODS

    def playerLook(self, direction):
        if len(direction) == 0:
            print("Command: Look")
        else:
            print("Command: Look " + direction)

    def playerMove(self, direction):
        print("Command: Move " + direction)
        newRoom = ""
        num = -1

        if direction == "north":
            num = 0 
        elif direction == "south":
            num = 1
        elif direction == "east":
            num = 2
        elif direction == "west":
            num = 3

        newRoom = self.location.getConnection(num)

        if newRoom == None:
            print("There is no exit in that direction.")
        else:
            for i, room in enumerate(self.rooms):
                if room.name == newRoom:
                    self.location = room
                    print("New location: ")
                    self.location.getLoadData()

                    if self.location.name == "Lake Lunaria":
                        print("You have reached the last room. Exiting game.")
                        sys.exit()
                    else:
                        break

    def playerUse(self, item):
        print("Command: Use <" + item + ">")

    # Create an instance (aka object) of Item class using string received in user input
    # Add to Game inventory, display inventory, then save to json
    # GAME WILL NOT HAVE INVENTORY LATER - THIS IS FOR TESTING
    def playerTake(self, item):
        print("Command: Take " + item)
        print("You grabbed the " + item + "!")
        
        #if level == janitors closet
        if item == "key":
            item1 = Item(item, "Use to open something...")
            self.inventory.addItem(item1)
        if item == "hammer":
            item2 = Item(item, "use to smash something...")
            self.inventory.addItem(item2)       
 
        #print the items in the inventory currently to verify
        self.inventory.displayInventory()

    def playerPlace(self, item):
        print("Command: Place " + item)
        print("in playerPlace")
        if item == "key":
            self.inventory.removeItem("key")
            print("The key was dropped.")
        if item == "hammer":
            self.inventory.removeItem("hammer")
            print("The hammer was dropped.")

        #print the items in the inventory currently to verify
        self.inventory.displayInventory()

    def playerGame(self):
        print("Command: Game Status")

