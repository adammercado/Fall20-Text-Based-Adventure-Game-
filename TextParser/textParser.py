class TextParser:
	def __init__(self):
		self.look_actions = ["look", "look at", "check", "examine", "observe"]

		self.move_actions = ["move", "go", "jump", "swim", "climb"]

		self.move_directions = ["up", "down", "left", "right", "north", "south", "east", "west"]

		self.use_actions = ["use", "combine", "hit", "strike", "pull", "push", "eat", "drink", "sit", "pour", "consume", "spill"]

		self.pick_up_actions = ["take", "grab"]

		self.place_actions = ["place", "put", "drop"]

		self.game_actions = ["savegame", "loadgame", "inventory", "help"]

		self.look_prepositions = ["on", "in", "into", "above", "below", "through"]

		self.use_prepositions = ["with", "together"]

	def parse(self, args):
		actions = 0
		directionFlag = False

		for word in args:
			if word == "quit" and len(args) == 1:
				return args
			elif word in self.look_actions or word in self.move_actions or word in self.use_actions or word in self.pick_up_actions or word in self.place_actions or word in self.game_actions:
				actions += 1

				if actions > 1:
					args.clear()
				elif word in self.move_actions or word in self.look_actions:
					directionFlag = True
			elif word in self.move_directions:
				if actions == 0 or directionFlag == False:
					args.clear()
			else:
				args.clear()	

		return args
