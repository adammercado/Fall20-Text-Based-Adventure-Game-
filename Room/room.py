import json

class Room:
	name = ""
	longDesc = ""
	shortDesc = ""
	priorVisit = False

	def createRoom(self, fileName):
		if fileName.is_file():
			with open(fileName) as infile:
				data = json.load(infile)

				self.name = data["name"]
				self.longDesc = data["longDesc"]
				self.shortDesc = data["shortDesc"]
				self.priorVisit = data["priorVisit"]

	# Testing
	def printRoom(self):
		print(self.name)
		print()
		print(self.longDesc)
		print()
		print(self.shortDesc)
		print()
		print(priorVisit)
		print()
	
