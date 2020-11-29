from Item.item import Item


class Progression:
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
        print("Perform")
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

    def combine_items(self, item_1, item_2, player_inventory):
        pair = (item_1, item_2)
        if pair in self.item_combo \
                or pair[::-1] in self.item_combo:
            new_item = Item.create_item_from_file("./GameData/Items/shining_pendant.json")
            new_item.get_item_data()
            player_inventory.add_item(new_item)

    def get_victory_text(self):
        text = """The shining pendant the Boy has begins glowing. As he pulls it out and observes the light, he 
        looks up and realizes something strange is happening. Daylight is suddenly shifting into a night sky, 
        and taking the place of the sun is a full moon. Just like the moon back home, it is fills the land with 
        light. The Boy notices that the moonlight seems to be particularly shining on the Lake Lunaria itself.
        
        All around him, he is surrounded by a glow. Glowing moonlight, a glowing pendant, the glistening water of 
        the lake.  It seems the old pendant with the gemstone slotted inside of it is reacting to the scene. Gradually, 
        the Boy comes to suspect that the owner of the old home in Astraia was searching for this exact moment. As 
        he reflects further, he thinks about the adventure he has had - waking up in a forest, experiencing the sight 
        of a rapid waterfall, a different town full of different people, mountains, caves... all for the first 
        time in his short life. He felt nervous, anxious, but above all - curious. Curiosity to the point that he 
        often forgot his situation, and that he was away from home.   
        
        Thinking about this, he walks out on the dock, as if forgetting all about what was happening in front 
        of his eyes. Instead of fear, he felt relief. The Boy had been caught up in his own worries about 
        leaving home and growing up, but before he knew it, he had come to embrace this strange world for all of its 
        discoveries and experiences it had to offer. As the moonlight becomes more blinding, it envelops the Boy, 
        who instinctively closes his eyes.
        
        He feels the familiar touch of his covers, and recognizes the familiar scent 
        of his home. Turning over, lost in the comfort of familiarity and optimism towards his unknown future, the 
        weary Boy begins to drift off to sleep, peacefully, for the first time in a long time.
        """
