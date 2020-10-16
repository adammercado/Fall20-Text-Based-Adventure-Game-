class TextParser:
	def __init__(self):
		self.look_actions = ["look", "look at", "check", "examine", "observe"]

		self.move_actions = ["move", "go", "jump", "swim", "climb"]

		self.move_directions = ["up", "down", "left", "right", "north", "south", "east", "west"]

		self.use_actions = ["use", "combine", "hit", "strike", "pull", "push", "eat", "drink", "sit", "pour", "consume", "spill"]

		self.pick_up_actions = ["take", "grab"]

		self.place_actions = ["place", "put", "drop"]

		self.game_actions = ["savegame", "loadgame", "inventory", "help", "quit"]

	def parse(self, args):
		res = ""
		count = 0
		directionFlag = False
		invalidAction1 = "Not a valid action, please try again."
		invalidAction2 = "Please enter only one action word."

		for word in args:
			if word in self.look_actions or word in self.move_actions or word in self.use_actions or word in self.pick_up_actions or word in self.place_actions or word in self.game_actions or word in self.move_directions:
				if count < 1 and word not in self.move_directions:
					res += word
					count += 1

					if word in self.move_actions or word in self.look_actions:
						directionFlag = True

				elif word in self.move_directions:
					if directionFlag and count <= 1:
						res += " " + word
					else:
						return invalidAction1

				elif count >= 1:
					return invalidAction2

			else:
				return invalidAction1	

		return res
