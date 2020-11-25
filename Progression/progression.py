from Room.room import Room
from Player.player import Player
from Inventory.inventory import Inventory
from Item.item import Item

class Progression:

    @staticmethod
    def perform_interaction(item, room):
        if item == "tree branch" and room.name == "Serene Forest - North":
            print("TEST")
        else:
            print("Not a valid interaction.")
