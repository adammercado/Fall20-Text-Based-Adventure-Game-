class TextParser:
    def __init__(self):
        self.look_actions = ["look", "look at", "check", "examine", "observe"]

        self.move_actions = ["move", "go", "jump", "swim", "climb"]

        self.move_directions = ["north", "south", "east", "west"]

        self.use_actions = ["use", "combine", "hit", "strike", "pull", "push", "eat", "drink", "sit", "pour", "consume", "spill", "pry", "whip", "shine"]

        self.take_actions = ["take", "grab"]

        self.place_actions = ["place", "put", "drop", "leave"]

        self.game_actions = ["savegame", "loadgame", "inventory", "help"]

        self.look_prepositions = ["on", "in", "into", "above", "below", "through"]

        self.use_prepositions = ["with", "together"]

        self.item_list = ["tree branch", "rusted key", "dull pendant", "map", "flask", "lantern", "white flower", "gemstone"]

        self.feature_list = ["tree", "rabbit"]

    # Receive list of arguments and determine type of action received using vocabulary space defined in class
    # Returns list of strings
    def parse(self, args):
        actions = 0
        directionFlag = False
        itemFlag = False
        parsedText = []

        if args[0] in self.take_actions or args[0] in self.place_actions:
            if args[0] in self.take_actions:
                parsedText.append("take")
            elif args[0] in self.place_actions:
                parsedText.append("place")

            package = ""

            for i, word in enumerate(args):
                if i > 0:
                    package += word

                    if i != (len(args) - 1):
                       package += " "

            print(package)
            if package in self.item_list:
                parsedText.append(package)
            else:
                parsedText.clear()
    
            return parsedText

        for word in args:
            if word == "quit" and len(args) == 1:
                return args

            elif word in self.look_actions or word in self.move_actions or word in self.use_actions or word in self.game_actions:
                actions += 1
                keyword = ""

                # List containing more than one recognized action will clear and return the empty list
                if actions > 1:
                    parsedText.clear()

                # Otherwise, determine action type and append to return list
                else:
                    if word in self.move_actions or word in self.look_actions:
                        directionFlag = True
                    if word in self.use_actions:
                        itemFlag = True
                    if word in self.move_actions:
                        keyword = "move"
                    elif word in self.look_actions:
                        keyword = "look"
                    elif word in self.use_actions:
                        keyword = "use"
                    elif word in self.game_actions:
                        keyword = word

                    parsedText.append(keyword)

            # If a direction is received is not valid with received action, list will clear and return empty list
            # Otherwise, append direction to return list
            elif directionFlag == True:
                if actions == 0 or (word not in self.move_directions and  word not in self.feature_list):
                    parsedText.clear()
                else:
                    print(word)
                    parsedText.append(word)

            elif itemFlag == True and actions == 1:
                parsedText.append(word)
                itemFlag == False
            # Clear list if current word is not found in vocabulary space
            else:
                parsedText.clear()    

        return parsedText

    def convertSpaces(self, string):
        convertedStr = ""

        for char in string:
            if char.isspace():
                convertedStr += '_'
            else:
                convertedStr += char

        return convertedStr                

