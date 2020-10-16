from TextParser.textParser import TextParser

class Game:
	parser = TextParser()
	userInput = ""

	def startGame(self):
		while 1:
			args = input("Enter an action: ").lower().split()
			self.getInput(args)

	def getInput(self, args):
		action = self.parser.parse(args)
	
		if action == "quit":
			print("Exiting gameplay")
			exit()
		else:
			print(action)
			print()

