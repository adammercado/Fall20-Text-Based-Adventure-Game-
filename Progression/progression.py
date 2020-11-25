
class Progression:
    def __init__(self):
        self.interactions = [
            ("tree branch", "Serene Forest - North", "rusted key"),
            ("rusted key", "Abandoned Home", "dull pendant"),
            ("flask", "Campsite", "lantern"),
            ("white flower", "Old Shrine", "gemstone")
        ]

    def perform_interaction(self, item, player_inventory, room):
        pair = (item, room.name)

        for group in self.interactions:
            if pair[0] == group[0] and pair[1] == group[1]:
                for obj in room.inventory.get_inventory_list():
                    if obj.name.lower() == group[2]:
                        print("Item to be dropped: {}".format(group[2]))
                        obj.toggle_obtainable()
                        room.room_drop_item(group[2], player_inventory)
                        print("End of function.")
                        break
                break
            else:
                print("Not a valid interaction.")
