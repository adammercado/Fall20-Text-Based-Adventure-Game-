import sys
import json
import os
from pathlib import Path
from TextParser.textParser import TextParser
from Room.room import Room

"""
Methods:
    startGame()
    loadGame()
    getInput()

    -- TEMPORARY ATTRIBUTES TO BE REPLACED/CHANGED--
    playerName

    -- TEMPORARY METHODS TO BE REPLACED/CHANGED --
    playerLook()
    playerMove()
    playerUse()
    playerTake()
    playerPlace()
    playerGame()
"""


class Game:
    parser = TextParser()
    playerName = ""
    location = "Janitor's Closet"
    inventory = ["key", "wallet"]
    rooms = []

    def startGame(self):
        directory = "./GameData/RoomTypes"

        # Iterate through each .json file in directory of room types, pass into constructor using file name
        for fileName in os.listdir(directory):
            if fileName.endswith(".json"):
                roomPath = directory + "/" + fileName
                curRoom = Room.fromFileName(roomPath)
                self.rooms.append(curRoom)
                print("tst indent")
            else:
                continue

        # Test initialization of rooms
        for room in self.rooms:
            print()
            print("*** INITIALIZING ROOM AND PRINTING DATA ***")
            print("*** THIS SHOULD DISPLAY LONG DESCRIPTION ***")
            print()
            room.getData()
            print()

            self.playerName = input("Enter a name: ")

        # Convert object into JSON list of strings because cannot store object in JSON format
        jsonRoomsList = json.dumps([obj.__dict__ for obj in self.rooms])

        data = {
            "name": self.playerName,
            "location": self.location,
            "inventory": self.inventory,
            "rooms": jsonRoomsList
        }

        with open("./Saves/gameSave.json", "w") as outfile:
            json.dump(data, outfile, indent=4)

        self.playGame()

    def loadGame(self):
        saveFile = Path("./Saves/gameSave.json")

        if saveFile.is_file():
            with open("./Saves/gameSave.json") as infile:
                data = json.load(infile)

                self.playerName = data["name"]
                self.location = data["location"]
                self.inventory = data["inventory"]
                # Convert JSON array into list of strings
                temp = json.loads(data["rooms"])

                print("TEST - Player Name is " + self.playerName)
                print("TEST - Location is " + self.location)

                for item in self.inventory:
                    print("TEST - Item in inventory is " + item)

                print()
                print("*** LOADING ROOM DATA ***")
                print("*** THIS SHOULD DISPLAY SHORT DESCRIPTION ***")
                print()

                for room in temp:
                    # Re-create Room objects using list of strings using default constructor
                    curRoom = Room(room['name'], room['longDesc'], room['shortDesc'], room['priorVisit'])
                    self.rooms.append(curRoom)

                    # Print room data to test proper loading of rooms
                    curRoom.getLoadData()

                print()

            self.playGame()
        else:
            print("No save file found. Creating a new game...")
            self.startGame()


    # Tokenize input and pass into class method
    def playGame(self):
        while 1:
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
            self.playerTake("item")

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
        else:
            print("Command: Move " + direction)

    def playerUse(self, item):
        print("Command: Use <" + item + ">")

    def playerTake(self, item):
        print("Command: Take <" + item + ">")

    def playerPlace(self, item):
        print("Command: Place <" + item + ">")

    def playerGame(self):
        print("Command: Game Status")

