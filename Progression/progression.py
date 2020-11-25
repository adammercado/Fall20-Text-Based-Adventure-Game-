from Room.room import Room
from Player.player import Player
from Inventory.inventory import Inventory
from Item.item import Item
import re


class Progression:
    def __init__(self):
        self.interactions = [
            ("Tree Branch", "Serene Forest - North", "Rusted Key"),
            ("Rusted Key", "Abandoned Home", "Dull Pendant")
        ]

    def perform_interaction(self, item, player_inventory, room):
        pair = (item, room.name)

        for group in self.interactions:
            if pair[0] == group[0].lower() and pair[1] == group[1]:
                # Debug print statements
                print("Conditional check match passed.")
                print("Item to be dropped: {}".format(group[2]))

                for obj in room.inventory.get_inventory_list():
                    if obj.name.lower() == group[2]:
                        obj.toggle_obtainable()
                        room.room_drop_item(group[2], player_inventory)
                        break

                return
            else:
                print("Not a valid interaction.")
