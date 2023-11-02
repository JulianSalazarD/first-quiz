################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!


class MagicOven:

  def __init__(self):
    self.items = []
    self.material = None

  def add(self, item):
    self.items.append(item)

  def freeze(self):
    if len(self.items) != 0:
      if "air" in self.items and "water" in self.items:
        self.material = "snow"
      else:
        self.material = "some cold object"

  def boil(self):
    if len(self.items) != 0:
      if "lead" in self.items and "mercury" in self.items:
        self.material = "gold"
      elif "cheese" in self.items and "dough" in self.items and "tomato" in self.items:
        self.material = "pizza"
      else:
        self.material = "some hot object"

  def wait(self):
    if len(self.items) != 0:
      self.material = "object salad"

  def get_output(self):
    if self.material is None:
      return "items are empty"

    temp = self.material
    self.material = None
    self.items.clear()
    return temp



def make_oven():
  return MagicOven()

def alchemy_combine(oven, ingredients, temperature):

  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()