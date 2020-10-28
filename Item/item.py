class Item:
   """The item class is used to represent the objects
      that can be acquired during gameplay.

      Attribute(s):
      - Name (string)
      - Description (string)
      - Valid actions (int): item specific or room specific interactions
      
      Method(s):
      item_save(): returns the item number for saving it
   """
   
   #Constructor
   def __init__(self, name, description, valid_action):
   
      self.name = name
      self.description = description
      self.valid_action = valid_action
   
   def item_save(self):
   
      dict_item = {
         'name':self.name,
         'description': self.description,
         'valid_action': self.valid_action
      }
      return dict_item
   
