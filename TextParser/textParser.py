class TextParser:
    def __init__(self):
        self.look_actions = ["look", "look at", "check", "examine", "observe"]

        self.move_actions = ["move", "go", "head"]

        self.move_directions = ["north", "south", "east", "west"]

        self.use_actions = ["use", "combine"]

        self.take_actions = ["take", "grab"]

        self.place_actions = ["place", "put", "drop", "leave"]

        self.game_actions = ["savegame", "loadgame", "inventory", "help", "quit"]

        self.look_prepositions = ["on", "in", "into",
                                  "above", "below", "through"]

        self.use_prepositions = ["with", "together"]

        self.item_list = ["tree branch", "rusted key", "dull pendant", "map",
                          "flask", "lantern", "white flower", "gemstone"]

        self.feature_list = ["tree", "rabbit", "boar", "forest opening",
                             "old journal", "old phone",
                             "waterfall", "town entrance",
                             "fountain", "market stand",
                             "abandoned home", "dog", "campfire",
                             "woman", "stalagmites", "bats",
                             "mountain path", "astraia", "fisherman",
                             "birds", "wooden carriage", "river", "lake",
                             "clouds", "water", "dock", "statue", "plaque",
                             "white flower", "signpost"]

    def parse_interaction(self, args, command, prepositions):
        package = ""
        res = [command]

        # Ignore prepositions
        for i, word in enumerate(args):
            if i > 0:
                if word not in prepositions:
                    package += word

                    if i < (len(args) - 1) and args[i+1] not in prepositions:
                        package += " "
                elif word in prepositions:
                    res.append(package)
                    del package
                    package = ""

        if package in self.item_list:
            res.append(package)

        if len(res) == 1:
            res.clear()

        return res

    def parse_look(self, args, command, prepositions):
        res = []

        if args[0] == "look" and len(args) == 1:
            res.append(command)
            return res
        else:
            res.append(command + " at")
            idx = 0

            if args[1] == "at":
                idx += 1

            package = ""

            for i, word in enumerate(args):
                if i > idx:
                    if word not in prepositions:
                        package += word

                        if i < (len(args) - 1) and args[i + 1] not in prepositions:
                            package += " "
                    elif word in prepositions:
                        res.append(package)
                        del package
                        package = ""

            if package in self.item_list:
                res.append(package)
                res.append("item")
            elif package in self.feature_list:
                res.append(package)
                res.append("feature")

        if len(res) == 1:
            res.clear()

        return res

    def parse_movement(self, args, command):
        res = []

        if len(args) == 2 and args[1] in self.move_directions:
            res.append(command)
            res.append(args[1])

        return res

    # Receive list of arguments and determine action received
    def parse(self, args):
        word = args[0]
        res = []

        if word in self.take_actions:
            res = self.parse_interaction(args, "take", self.use_prepositions)
        elif word in self.place_actions:
            res = self.parse_interaction(args, "place", self.use_prepositions)
        elif word in self.use_actions:
            res = self.parse_interaction(args, "use", self.use_prepositions)
        elif word in self.look_actions:
            res = self.parse_look(args, "look", self.look_prepositions)
        elif word in self.move_directions and len(args) == 1:
            res = self.parse_movement(["move"] + args, "move")
        elif word in self.move_actions:
            res = self.parse_movement(args, "move")
        elif word in self.game_actions:
            res.append(word)

        return res

    def convert_spaces(self, string):
        converted_str = ""

        for char in string:
            if char.isspace():
                converted_str += '_'
            else:
                converted_str += char

        return converted_str
