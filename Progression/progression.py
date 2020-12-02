from Item.item import Item


class Progression:
    """Determines specific interactions required for progression

    Attributes
    ----------
        interactions : list( {str, str str} )
            list of tuples of valid interactions
        item_combo : list( {str, str} )
            list of tuples of valid item use combinations
    Methods
    -------
        get_progression(item_1, item_2, player_inventory, room)
            call appropriate method based on parameters
        perform_interaction(item, player_inventory, room)
            performs item exchange if interaction is valid
        combine_items(self, item_1, item_2, player_inventory)
            creates combined item and removes recipe items
    """
    def __init__(self):
        self.interactions = [
            ("tree branch", "Serene Forest - North", "rusted key"),
            ("rusted key", "Abandoned Home", "dull pendant"),
            ("flask", "Campsite", "lantern"),
            ("white flower", "Old Shrine", "gemstone")
        ]

        self.item_combo = [
            ("dull pendant", "gemstone")
        ]

    def get_progression(self, item_1, item_2, player_inventory, room):
        if item_2 is None:
            self.perform_interaction(item_1, player_inventory, room)
        else:
            self.combine_items(item_1, item_2, player_inventory)

    def perform_interaction(self, item, player_inventory, room):
        pair = (item, room.name)

        for group in self.interactions:
            if pair[0] == group[0] and pair[1] == group[1]:
                for obj in room.inventory.get_inventory_list():
                    if obj.name.lower() == group[2]:
                        obj.toggle_obtainable()
                        room.room_drop_item(group[2], player_inventory)
                        break
                break

    def combine_items(self, item_1, item_2, player_inventory):
        pair = (item_1, item_2)

        if pair in self.item_combo \
                or pair[::-1] in self.item_combo:
            new_item = Item.create_item_from_file(
                "./GameData/Items/shining_pendant.json")
            new_item.get_item_data()
            player_inventory.add_item(new_item)
            player_inventory.remove_item_by_name(item_1)
            player_inventory.remove_item_by_name(item_2)
