"""
Transportation Mode Selection
Choose a mode of transportation based on the distance(e.g <3km Walk,
3-15 Bike ,>15 Car)"""

dis = input("How much distance you have to cover:")
distance = int(dis)

if distance < 3:
    choose="Walk"
elif distance<=15:
    choose = "Bike"
elif distance >15:
    choose = "Car"        

print("Recommended transportation is",choose)