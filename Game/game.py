import sys
import json
import os
from pathlib import Path
from TextParser.textParser import TextParser
from Room.room import Room
from Item.item import Item
from Player.player import Player
from Feature.feature import Feature

"""
Attributes:
    parser
    player
    location
    rooms

Methods:
    startGame()
    saveGame()
    loadGame()
    playGame()
    getInput()
"""


class Game:
    parser = TextParser()
    player = None
    location = None
    rooms = []

    # Initializes game state before calling playGame()
    def startGame(self):
        directory = "./GameData/RoomTypes"

        # Iterate through room JSON files in directory and initialize with Room class constructor using file name
        for fileName in os.listdir(directory):
            if fileName.endswith(".json"):
                roomPath = directory + "/" + fileName
                print(roomPath)
                curRoom = Room.fromFileName(roomPath)

                # Set starting location
                if curRoom.name == "Serene Forest - South":
                    self.location = curRoom

                self.rooms.append(curRoom)
            else:
                continue

        self.player = Player("")
        self.playGame()

    # Calls class methods to convert data into JSON format and write to save file
    def saveGame(self):
        playerData = json.dumps(self.player.convertPlayerToJson())
        locationData = json.dumps(self.location.convertRoomToJson())
        roomData = []

        for room in self.rooms:
            roomData.append(room.convertRoomToJson())

        roomData = json.dumps(roomData)

        data = {
            "player": playerData,
            "location": locationData,
            "rooms": roomData
        }

        # Open or create save file and dump JSON data into it
        with open("./Saves/gameSave.json", "w") as outfile:
            json.dump(data, outfile, indent=4)

        print("Game saved successfully.")

    # Opens save file use loaded JSON data to re-initialize game state
    def loadGame(self):
        saveFile = Path("./Saves/gameSave.json")

        if saveFile.is_file():
            with open("./Saves/gameSave.json") as infile:
                data = json.load(infile)

                # Receive JSON lists of data 
                playerData = json.loads(data["player"])
                locationData = json.loads(data["location"])
                roomData = json.loads(data["rooms"])

                # Call constructors for initializing using JSON data
                self.location = Room(locationData['name'], locationData['longDesc'], locationData['shortDesc'], locationData['priorVisit'], locationData['connections'], locationData['inventory'], locationData['featureList'])
                self.player = Player(playerData['inventory'])

                # Call constructors for each object in room list received from JSON and append to rooms list in Game
                for room in roomData:
                    curRoom = Room(room['name'], room['longDesc'], room['shortDesc'], room['priorVisit'], room['connections'], room['inventory'], room['featureList'])
                    self.rooms.append(curRoom)

            self.playGame()
        else:
            print("No save file found. Creating a new game...")
            self.startGame()

    # Handles actions pertaining to gameplay using received input 
    def playGame(self):
        while 1:
            print("Current location: " + self.location.name)

            args = input("Enter an action: ").lower().split()
            self.getInput(args)

    # Receive tokenized input as list and pass to TextParser to determine command
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

        elif parsedText[0] == "take" or parsedText[0] == "place":
            itemName = self.parser.convertSpaces(parsedText[1].lower())
            itemPath = "./GameData/Items/{}.json".format(itemName) 

            if parsedText[0] == "take":
                if self.location.inventory.checkInventory(parsedText[1]):
                    self.location.roomDropItem(parsedText[1])
                    curItem = Item.createItemFromFile(itemPath)

                    self.player.playerAddItem(curItem)
                    print("PLAYER INVENTORY")
                    self.player.inventory.displayInventory()
                    print("ROOM INVENTORY")
                    self.location.inventory.displayInventory()
                else:
                    print("There is no {} in this location.".format(parsedText[1]))

            elif parsedText[0] == "place":
                 if self.player.inventory.checkInventory(parsedText[1]):
                    self.player.playerDropItem(parsedText[1])
                    curItem = Item.createItemFromFile(itemPath)

                    self.location.roomAddItem(curItem)
                    print("PLAYER INVENTORY")
                    self.player.inventory.displayInventory()
                    print("ROOM INVENTORY")
                    self.location.inventory.displayInventory()
                 else:
                    print("Cannot drop {} because it is not in the inventory.".format(parsedText[1]))
 
        elif parsedText[0] == "savegame":
            self.saveGame()

        elif parsedText[0] == "loadgame":
            self.loadGame()

        elif parsedText[0] == "inventory":
            self.player.inventory.displayInventory()

        elif parsedText[0] == "help":
            print("Display help menu here")

# PLACEHOLDER METHODS

    def playerLook(self, direction):
        if len(direction) == 0:
            print("Command: Look")
        else:
            print("Command: Look " + direction)
            self.location.examine(direction)

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
                    self.location.getLoadData()
                    self.location.getFeatures()

                    if self.location.name == "Lake Lunaria":
                        print("You have reached the last room. Exiting game.")
                        sys.exit()
                    else:
                        break

    def playerUse(self, item):
        print("Command: Use <" + item + ">")

    def playerGame(self):
        print("Command: Game Status")
