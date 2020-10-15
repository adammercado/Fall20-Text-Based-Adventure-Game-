from TextParser.textParser import TextParser

class Game:
	parser = TextParser()
	userInput = ""

	def startGame(self):
		while 1:
			self.getInput()

	def getInput(self):
		action = self.parser.parse()
	
		if action == "quit":
			print("Exiting gameplay")
			exit()
		else:
			print(action)

