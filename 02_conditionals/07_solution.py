"""
Coffe customization
Customixe a coffee order "Small","Mwdium" or "Extra large" with one 
extra shot of expresso

"""

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"

else:
    coffee = order_size + "coffee"

print("Order:",coffee)    