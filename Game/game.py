import sys
from TextParser.textParser import TextParser

class Game:
	parser = TextParser()
	userInput = ""

	def startGame(self):
		while 1:
			args = input("Enter an action: ").lower().split()
			self.getInput(args)

	def getInput(self, args):
		args = self.parser.parse(args)

		if len(args) == 0:
			print("Not a valid action.")
		elif args[0] == "quit":
			print("Exiting gameplay")
			sys.exit()
		else:
			for word in args:
				print(word)
