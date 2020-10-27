import sys
import json
from pathlib import Path

class Item:
   """The item class is used to represent the objects
      that can be acquired during gameplay.

      Attribute(s):
      - Name (string)
      - Description (string)
      - Valid actions (int): item specific or room specific interactions
      
   """
   
   #Constructor
   def __init__(self, name, description, valid_action):
   
      self.name = name
      self.description = description
      self.valid_action = valid_action
   
