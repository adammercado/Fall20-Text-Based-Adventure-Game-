import json

class Room:

	def __init__(self, name, longDesc, shortDesc, priorVisit):
		self.name = name
		self.longDesc = longDesc
		self.shortDesc = shortDesc
		self.priorVisit = bool(priorVisit == "true")

	# Constructor using file name
	def fromFileName(fileName):

		with open(fileName) as infile:
			data = json.load(infile)

			name = data["name"]
			longDesc = data["longDesc"]
			shortDesc = data["shortDesc"]
			priorVisit = data["priorVisit"]

		return Room(name, longDesc, shortDesc, priorVisit)

	# Test method called when saving room data to json
	def getData(self):
		print(self.name)
		print(self.longDesc)
		
	# Test method called when loading room data from json
	def getLoadData(self):
		print(self.name)
		print(self.shortDesc)