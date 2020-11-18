class Feature:

    def __init__(self, name, desc, isInteractive, interactions):
        self.name = name
        self.desc = desc
        self.isInteractive = isInteractive
        self.interactions = interactions

    def getInfo(self):
        print("Feature: {}\nDesc: {}\nInteract: {}\nInteract With: {}".format(self.name, self.desc, self.isInteractive, self.interactions))

    def convertFeatureToJson(self):
        featureData = {
            "name": self.name,
            "desc": self.desc,
            "isInteractive": self.isInteractive,
            "interactions": self.interactions
        }

        return featureData

    def getDesc(self):
        print(self.desc)
