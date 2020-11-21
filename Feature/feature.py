
class Feature:

    def __init__(self, name, desc, is_interactive, interactions):
        self.name = name
        self.desc = desc
        self.is_interactive = is_interactive
        self.interactions = interactions

    def get_feature_info(self):
        print("Feature: {}\nDesc: {}\nInteract: {}\nInteract With: {}"
              .format(self.name, self.desc, self.is_interactive, self.interactions))

    def convert_feature_to_json(self):
        feature_data = {
            "name": self.name,
            "desc": self.desc,
            "isInteractive": self.is_interactive,
            "interactions": self.interactions
        }

        return feature_data

    def get_desc(self):
        print(self.desc)
