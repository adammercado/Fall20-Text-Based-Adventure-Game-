class TextParser:
	def __init__(self):
		self.look_actions = ["look", "look at", "check", "examine", "observe"]

		self.move_actions = ["move", "go", "jump", "swim", "climb"]

		self.move_directions = ["up", "down", "left", "right", "north", "south", "east", "west"]

		self.use_actions = ["use", "combine", "hit", "strike", "pull", "push", "eat", "drink", "sit", "pour", "consume", "spill"]

		self.pick_up_actions = ["take", "grab"]

		self.place_actions = ["place", "put", "drop"]

		self.game_actions = ["savegame", "loadgame", "inventory", "help"]

	def parse(self):
		args = input("Enter an action: ").lower().split()
		res = ""

		for word in args:
			res += word

			if word == "quit":
				return res
			elif word in self.look_actions:
				res += " is a look action."
			elif word in self.move_actions:
				res += " is a move action."
			elif word in self.use_actions:
				res += " is a use action."
			elif word in self.pick_up_actions:
				res += " is a pick up action."
			elif word in self.place_actions:
				res += " is a place action."
			elif word in self.game_actions:
				res += " is a game action."
			else:	
				res += " is not a valid action."

		return res
