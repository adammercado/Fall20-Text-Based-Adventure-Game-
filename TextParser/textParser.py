class TextParser:
    def __init__(self):
        self.look_actions = ["look", "look at", "check", "examine", "observe"]

        self.move_actions = ["move", "go", "jump", "swim", "climb"]

        self.move_directions = ["north", "south", "east", "west"]

        self.use_actions = ["use", "combine", "hit", "strike", "pull", "push", "eat", "drink", "sit", "pour",
                            "consume", "spill", "pry", "whip", "shine"]

        self.take_actions = ["take", "grab"]

        self.place_actions = ["place", "put", "drop", "leave"]

        self.game_actions = ["savegame", "loadgame", "inventory", "help"]

        self.look_prepositions = ["on", "in", "into", "above", "below", "through"]

        self.use_prepositions = ["with", "together"]

        self.item_list = ["tree branch", "rusted key", "dull pendant", "map", "flask", "lantern", "white flower",
                          "gemstone"]

        self.feature_list = ["tree", "rabbit", "angry boar", "forest opening", "old journal", "old phone", "waterfall",
                             "jumping fishes", "town entrance", "fountain", "loud merchant", "market stand",
                             "abandoned home", "dog", "campfire", "tents", "middle-aged woman", "stalagmites", "bats",
                             "mountain path", "astraia", "fisherman", "birds", "wooden carriage", "river", "mountains"]

    # Receive list of arguments and determine type of action received using vocabulary space defined in class
    # Returns list of strings
    def parse(self, args):
        actions = 0
        direction_flag = False
        item_flag = False
        parsed_text = []

        if args[0] in self.take_actions or args[0] in self.place_actions or args[0] in self.look_actions:
            if args[0] in self.take_actions:
                parsed_text.append("take")
            elif args[0] in self.place_actions:
                parsed_text.append("place")
            else:
                parsed_text.append("look")

            package = ""

            for i, word in enumerate(args):
                if i > 0:
                    package += word

                    if i != (len(args) - 1):
                        package += " "

            if package in self.item_list or package in self.feature_list:
                parsed_text.append(package)
            elif parsed_text[0] != "look":
                parsed_text.clear()

            return parsed_text

        for word in args:
            if word == "quit" and len(args) == 1:
                return args

            elif word in self.look_actions or word in self.move_actions or word in self.use_actions \
                    or word in self.game_actions:
                actions += 1
                keyword = ""

                # List containing more than one recognized action will clear and return the empty list
                if actions > 1:
                    parsed_text.clear()

                # Otherwise, determine action type and append to return list
                else:
                    if word in self.move_actions:
                        direction_flag = True
                    if word in self.use_actions:
                        item_flag = True
                    if word in self.move_actions:
                        keyword = "move"
                    elif word in self.use_actions:
                        keyword = "use"
                    elif word in self.game_actions:
                        keyword = word

                    parsed_text.append(keyword)

            # If a direction is received is not valid with received action, list will clear and return empty list
            # Otherwise, append direction to return list
            elif direction_flag:
                if actions == 0 or word not in self.move_directions:
                    parsed_text.clear()
                else:
                    parsed_text.append(word)

            elif item_flag and actions == 1:
                parsed_text.append(word)
                item_flag = False
            # Clear list if current word is not found in vocabulary space
            else:
                parsed_text.clear()

        return parsed_text

    def convert_spaces(self, string):
        converted_str = ""

        for char in string:
            if char.isspace():
                converted_str += '_'
            else:
                converted_str += char

        return converted_str
