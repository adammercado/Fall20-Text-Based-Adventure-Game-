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
                print(roomPath)
                curRoom = Room.fromFileName(roomPath)

                if curRoom.name == "Janitor's Closet":
                    self.location = curRoom

                self.rooms.append(curRoom)

            else:
                continue

        self.playerName = input("Enter a name: ")
        self.saveGame()
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

                self.location = Room(tempLocation['name'], tempLocation['longDesc'], tempLocation['shortDesc'], tempLocation['priorVisit'], tempLocation['nextRoom'])

                # Convert inventory list received from json back into item objects
                for item in tempInventoryList:
                    curItem = Item(item['name'], item['description'])
                    self.inventory.addItem(curItem)

                # TEST METHOD TO CHECK THAT INVENTORY LOADS PROPERLY
                self.inventory.displayInventory()

                # Convert room list received from json back into room objects
                for room in tempRoomList:
                    # Re-create Room objects using list of strings using default constructor
                    curRoom = Room(room['name'], room['longDesc'], room['shortDesc'], room['priorVisit'], room['nextRoom'])
                    self.rooms.append(curRoom)

                    # Print room data to test proper loading of rooms
                    # curRoom.getLoadData()

                print()

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

        elif parsedText[0] == "use":
            self.playerUse("item")

        elif parsedText[0] == "take":
            self.playerTake(parsedText[1])

        elif parsedText[0] == "place":
            self.playerPlace("item")

        elif parsedText[0] == "game":
            self.playerGame()

# PLACEHOLDER METHODS

    def playerLook(self, direction):
        if len(direction) == 0:
            print("Command: Look")
        else:
            print("Command: Look " + direction)

    def playerMove(self, direction):
        if len(direction) == 0:
            print("Command: Move")
            newRoom = self.location.nextRoom

            for i, room in enumerate(self.rooms):
                print(room.name)
                if room.name == newRoom:
                    self.location = room
                    print("New location: ")
                    self.location.getLoadData()
                    break

            self.saveGame()
        else:
            print("Command: Move " + direction)

    def playerUse(self, item):
        print("Command: Use <" + item + ">")

    # Create an instance (aka object) of Item class using string received in user input
    # Add to Game inventory, display inventory, then save to json
    # GAME WILL NOT HAVE INVENTORY LATER - THIS IS FOR TESTING
    def playerTake(self, item):
        print("Command: Take " + item)
        testItem = Item(item, "test description")
        self.inventory.addItem(testItem)
        self.inventory.displayInventory()
        self.saveGame()

    def playerPlace(self, item):
        print("Command: Place <" + item + ">")

    def playerGame(self):
        print("Command: Game Status")

