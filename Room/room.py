import json

class Room:
	name = ""
	longDesc = ""
	shortDesc = ""
	priorVisit = False

	def __init__(self, fileName):
		print(fileName)

		with open(fileName) as infile:
			data = json.load(infile)

			self.name = data["name"]
			self.longDesc = data["longDesc"]
			self.shortDesc = data["shortDesc"]
			self.priorVisit = bool(data["priorVisit"] == "true")
