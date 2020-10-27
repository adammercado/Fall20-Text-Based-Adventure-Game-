import sys
import json
from pathlib import Path
from TextParser.textParser import TextParser
from Item.Item import Item


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

    def startGame(self):
        self.playerName = input("Enter a name: ")

        data = {
            "name": self.playerName,
            "location": self.location,
            "inventory": self.inventory
        }

        with open("./Saves/gameSave.txt", "w") as outfile:
            json.dump(data, outfile, indent=4)

        self.playGame()

    def loadGame(self):
        saveFile = Path("./Saves/gameSave.txt")

        if saveFile.is_file():
            with open("./Saves/gameSave.txt") as infile:
                data = json.load(infile)

                self.playerName = data["name"]
                self.location = data["location"]
                self.inventory = data["inventory"]

                print("TEST - Player Name is " + self.playerName)
                print("TEST - Location is " + self.location)

                for item in self.inventory:
                    print("TEST - Item in inventory is " + item)

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
        # user inputs command received by game class to pick up an item in room
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

