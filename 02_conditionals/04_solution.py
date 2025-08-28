"""
Fruit Ripness Checker
Determine fruit is ripe , overrip or unripe based on its color
(eg Banana unripe-green , yellow-ripe black-overripe)

"""

Fruit = input("Enter fruit :")
Color= input("Enter fruit color:")

if Fruit == "Banana":
  if Color == "green":
     print("unripe")
  elif Color == "yellow":
     print("ripe")
  elif Color == "brown":
     print("overripe")        