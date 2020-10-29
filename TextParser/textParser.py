class TextParser:
    def __init__(self):
        self.look_actions = ["look", "look at", "check", "examine", "observe"]

        self.move_actions = ["move", "go", "jump", "swim", "climb"]

        self.move_directions = ["up", "down", "left", "right", "north", "south", "east", "west"]

        self.use_actions = ["use", "combine", "hit", "strike", "pull", "push", "eat", "drink", "sit", "pour", "consume", "spill", "pry", "whip", "shine"]

        self.take_actions = ["take", "grab"]

        self.place_actions = ["place", "put", "drop", "leave"]

        self.game_actions = ["savegame", "loadgame", "inventory", "help"]

        self.look_prepositions = ["on", "in", "into", "above", "below", "through"]

        self.use_prepositions = ["with", "together"]

    # Receive list of arguments and determine type of action received using vocabulary space defined in class
    # Returns list of strings
    def parse(self, args):
        actions = 0
        directionFlag = False
        itemFlag = False
        parsedText = []

        for word in args:
            if word == "quit" and len(args) == 1:
                return args

            elif word in self.look_actions or word in self.move_actions or word in self.use_actions or word in self.take_actions or word in self.place_actions or word in self.game_actions:
                actions += 1
                keyword = ""

                # List containing more than one recognized action will clear and return the empty list
                if actions > 1:
                    parsedText.clear()

                # Otherwise, determine action type and append to return list
                else:
                    if word in self.move_actions or word in self.look_actions:
                        directionFlag = True
                    if word in self.use_actions or self.take_actions or self.place_actions:
                        itemFlag = True

                    if word in self.move_actions:
                        keyword = "move"
                    elif word in self.look_actions:
                        keyword = "look"
                    elif word in self.use_actions:
                        keyword = "use"
                    elif word in self.take_actions:
                        keyword = "take"
                    elif word in self.place_actions:
                        keyword = "place"
                    elif word in self.game_actions:
                        keyword = "game"

                    parsedText.append(keyword)

            # If a direction is received is not valid with received action, list will clear and return empty list
            # Otherwise, append direction to return list
            elif word in self.move_directions:
                if actions == 0 or directionFlag == False:
                    parsedText.clear()
                else:
                    parsedText.append(word)

            elif itemFlag == True and actions == 1:
                parsedText.append(word)
                itemFlag == False
            # Clear list if current word is not found in vocabulary space
            else:
                parsedText.clear()    

        return parsedText

