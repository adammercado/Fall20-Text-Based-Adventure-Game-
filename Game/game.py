import sys
import json
import os
from pathlib import Path
from TextParser.textParser import TextParser
from Room.room import Room
from Item.item import Item
from Player.player import Player
from Progression.progression import Progression
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
    progression = Progression()
    player = None
    location = None
    rooms = []

    # Initializes game state before calling playGame()
    def start_game(self):
        directory = "./GameData/RoomTypes"

        # Iterate through room JSON files in directory and
        # initialize with Room class constructor using file name
        for fileName in os.listdir(directory):
            if fileName.endswith(".json"):
                room_path = directory + "/" + fileName
                cur_room = Room.from_file_name(room_path)

                # Set starting location
                if cur_room.name == "Serene Forest - South":
                    self.location = cur_room

                self.rooms.append(cur_room)
            else:
                continue

        self.player = Player(None)
        self.play_game()

    # Calls class methods to convert data into JSON format and write to save
    def save_game(self):
        player_data = json.dumps(self.player.convert_player_to_json())
        location_data = json.dumps(self.location.convert_room_to_json())
        room_data = []

        for room in self.rooms:
            room_data.append(room.convert_room_to_json())

        room_data = json.dumps(room_data)

        data = {
            "player": player_data,
            "location": location_data,
            "rooms": room_data
        }

        # Open or create save file and dump JSON data into it
        with open("./Saves/gameSave.json", "w") as outfile:
            json.dump(data, outfile, indent=4)

        print("Game saved successfully.")

    # Opens save file use loaded JSON data to re-initialize game state
    def load_game(self):
        save_file = Path("./Saves/gameSave.json")

        if save_file.is_file():
            with open("./Saves/gameSave.json") as infile:
                data = json.load(infile)

                # Receive JSON lists of data
                player_data = json.loads(data["player"])
                location_data = json.loads(data["location"])
                room_data = json.loads(data["rooms"])

                # Call constructors for initializing using JSON data
                self.location = Room(location_data['name'],
                                     location_data['long_desc'],
                                     location_data['short_desc'],
                                     location_data['prior_visit'],
                                     location_data['connections'],
                                     location_data['inventory'],
                                     location_data['feature_list'],
                                     True)

                self.player = Player(player_data['inventory'])

                # Call constructors for each object in room list from JSON
                # and append to rooms list in Game
                for room in room_data:
                    cur_room = Room(room['name'], room['long_desc'],
                                    room['short_desc'], room['prior_visit'],
                                    room['connections'], room['inventory'],
                                    room['feature_list'], True)
                    self.rooms.append(cur_room)

            self.play_game()
        else:
            print("No save file found. Creating a new game...")
            self.start_game()

    # Handles actions pertaining to gameplay using received input
    def play_game(self):
        while 1:
            print("Current location: " + self.location.name)

            args = []

            while len(args) == 0 or args[0] == '\n':
                args.clear()
                args = input("Enter an action: ").lower().split()

            self.get_input(args)

    # Receive tokenized input as list and pass to TextParser
    def get_input(self, args):
        parsed_text = self.parser.parse(args)

        if len(parsed_text) == 0:
            print("Not a valid action.")

        elif parsed_text[0] == "quit":
            print("Exiting gameplay")
            sys.exit()

        elif parsed_text[0] == "look":
            direction = ""

            if len(parsed_text) == 2:
                direction = parsed_text[1]

            self.player_look(direction)

        elif parsed_text[0] == "move":
            if len(parsed_text) == 2:
                direction = parsed_text[1]
                self.player_move(direction)
            else:
                print("You must enter a cardinal direction to move in.")
        elif parsed_text[0] == "use":
            if self.player.inventory.check_inventory(parsed_text[1]):
                self.player_use(parsed_text[1])
            else:
                print("{} is not in the inventory.".format(parsed_text[1]))
        elif parsed_text[0] == "take":
            if self.location.inventory.check_inventory(parsed_text[1]):
                self.location.room_drop_item(parsed_text[1], self.player.inventory)
            else:
                print("There is no {} in this location."
                      .format(parsed_text[1]))
        elif parsed_text[0] == "place":
            if self.player.inventory.check_inventory(parsed_text[1]):
                self.player.player_drop_item(parsed_text[1], self.location.inventory)
            else:
                print("Cannot drop {} because it is not in the inventory."
                      .format(parsed_text[1]))
        elif parsed_text[0] == "savegame":
            self.save_game()
        elif parsed_text[0] == "loadgame":
            self.load_game()
        elif parsed_text[0] == "inventory":
            self.player.inventory.display_inventory()
        elif parsed_text[0] == "help":
            print("Display help menu here")

    def player_look(self, name):
        if len(name) == 0:
            self.location.get_long_desc()
        else:
            print("Command: Look " + name)
            self.location.examine(name)

    def player_move(self, direction):
        print("Command: Move " + direction)
        num = -1

        if direction == "north":
            num = 0
        elif direction == "south":
            num = 1
        elif direction == "east":
            num = 2
        elif direction == "west":
            num = 3

        new_room = self.location.get_connection(num)

        if new_room is None:
            print("There is no exit in that direction.")
        else:
            for i, room in enumerate(self.rooms):
                if room.name == new_room:
                    self.location = room
                    self.location.get_short_desc()
                    # self.location.getFeatures()

                    if self.location.name == "Lake Lunaria":
                        print("You have reached the last room. Exiting game.")
                        sys.exit()
                    else:
                        break

    def player_use(self, item):
        print("Command: Use <" + item + ">")
        self.progression.perform_interaction(item, self.player.inventory, self.location)

    def player_game(self):
        print("Command: Game Status")

