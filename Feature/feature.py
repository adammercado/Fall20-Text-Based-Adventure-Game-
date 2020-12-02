
class Feature:
    """Represents features that can be viewed in game

    Attributes
    ----------
        name : str
            name of feature
        desc : str
            description of feature
        is_interactive : boolean (UNUSED)
            if object is interactive
        interactions : list (UNUSED)
            list of objects that can interact with feature
    Methods
    -------
        __init__(name, desc, is_interactive, interactions)
            default constructor creates instances using parameters
        get_feature_info()
            prints all information related to feature
        convert_feature_to_json()
            returns object containing feature data to write to JSON
        get_desc()
            prints description of feature
    """

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
            "is_interactive": self.is_interactive,
            "interactions": self.interactions
        }

        return feature_data

    def get_desc(self):
        print(self.desc)
