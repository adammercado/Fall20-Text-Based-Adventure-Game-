class TextParser:
    def __init__(self):
        self.look_actions = ["look", "look at", "check", "examine", "observe"]

        self.move_actions = ["move", "go", "jump", "swim", "climb"]

        self.move_directions = ["north", "south", "east", "west"]

        self.use_actions = ["use", "combine", "hit", "strike", "pull",
                            "push", "eat", "drink", "sit", "pour",
                            "consume", "spill", "pry", "whip", "shine"]

        self.take_actions = ["take", "grab"]

        self.place_actions = ["place", "put", "drop", "leave"]

        self.game_actions = ["savegame", "loadgame", "inventory", "help", "quit"]

        self.look_prepositions = ["on", "in", "into",
                                  "above", "below", "through"]

        self.use_prepositions = ["with", "together"]

        self.item_list = ["tree branch", "rusted key", "dull pendant", "map",
                          "flask", "lantern", "white flower", "gemstone"]

        self.feature_list = ["tree", "rabbit", "angry boar", "forest opening",
                             "old journal", "old phone",
                             "waterfall", "town entrance",
                             "fountain", "loud merchant", "market stand",
                             "abandoned home", "dog", "campfire", "tents",
                             "middle-aged woman", "stalagmites", "bats",
                             "mountain path", "astraia", "fisherman",
                             "birds", "wooden carriage", "river", "mountains"]

    def parse_action(self, args, command, prepositions):
        package = ""
        res = []

        # Ignore prepositions
        for i, word in enumerate(args):
            if i > 0:
                if word not in prepositions:
                    package += word

                    if i != (len(args) - 1):
                        package += " "

        if (package in self.item_list and command not in self.look_actions)\
                or (package in self.feature_list and command in self.look_actions):
            res.append(command)
            res.append(package)

        print("parse_item_action package: {}".format(res))
        return res

    # def parse_look_action(self, args, command, prepositions):
    #     package = ""
    #     res = []
    #
    #     # Ignore prepositions
    #     for i, word in enumerate(args):
    #         if i > 0:
    #             if word not in prepositions:
    #                 package += word
    #
    #                 if i != (len(args) - 1):
    #                     package += " "
    #
    #     if package in self.feature_list:
    #         res.append(command)
    #         res.append(package)
    #
    #     print("parse_look_action package: {}".format(res))
    #     return res

    def parse_move_action(self, args, command):
        res = []

        if len(args) == 2 and args[1] in self.move_directions:
            res.append(command)
            res.append(args[1])

        print("parse_move_action package: {}".format(res))
        return res

    # Receive list of arguments and determine action received
    def parse(self, args):
        word = args[0]
        res = []

        if word in self.take_actions:
            res = self.parse_action(args, "take", self.use_prepositions)
        elif word in self.place_actions:
            res = self.parse_action(args, "place", self.use_prepositions)
        elif word in self.use_actions:
            res = self.parse_action(args, "use", self.use_prepositions)
        elif word in self.look_actions:
            res = self.parse_action(args, "look", self.look_prepositions)
        elif word in self.move_actions:
            res = self.parse_move_action(args, "move")
        elif word in self.game_actions:
            res.append(word)

        return res


        # actions = 0
        # direction_flag = False
        # item_flag = False
        # parsed_text = []
        #
        # if args[0] in self.take_actions\
        #         or args[0] in self.place_actions\
        #         or args[0] in self.look_actions\
        #         or args[0] in self.use_actions:
        #     if args[0] in self.take_actions:
        #         parsed_text.append("take")
        #     elif args[0] in self.place_actions:
        #         parsed_text.append("place")
        #     elif args[0] in self.use_actions:
        #         parsed_text.append("use")
        #     else:
        #         parsed_text.append("look")
        #
        #     package = ""
        #
        #     for i, word in enumerate(args):
        #         if i > 0:
        #             package += word
        #
        #             if i != (len(args) - 1):
        #                 package += " "
        #
        #     if package in self.item_list\
        #             or package in self.feature_list:
        #         parsed_text.append(package)
        #     elif parsed_text[0] != "look":
        #         parsed_text.clear()
        #
        #     return parsed_text
        #
        # for word in args:
        #     if word == "quit" and len(args) == 1:
        #         return args
        #
        #     elif word in self.look_actions\
        #             or word in self.move_actions\
        #             or word in self.game_actions:
        #         actions += 1
        #         keyword = ""
        #
        #         # List containing more than one action will clear
        #         if actions > 1:
        #             parsed_text.clear()
        #
        #         # Otherwise, determine action type and append to return list
        #         else:
        #             if word in self.move_actions:
        #                 direction_flag = True
        #             if word in self.move_actions:
        #                 keyword = "move"
        #             elif word in self.game_actions:
        #                 keyword = word
        #
        #             parsed_text.append(keyword)
        #
        #     # If a direction is received is not valid, list will clear
        #     # Otherwise, append direction to return list
        #     elif direction_flag:
        #         if actions == 0 or word not in self.move_directions:
        #             parsed_text.clear()
        #         else:
        #             parsed_text.append(word)
        #     # Clear list if current word is not found in vocabulary space
        #     else:
        #         parsed_text.clear()
        #
        # return parsed_text


    def convert_spaces(self, string):
        converted_str = ""

        for char in string:
            if char.isspace():
                converted_str += '_'
            else:
                converted_str += char

        return converted_str
