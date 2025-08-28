"""
Pet food recommendation
Recommend aa type of food based on pet's species and age
(e.g dog<2 years puppy food , cat>5 years senior cat food)

"""
pet = input("Who is your pet:")
age = int(input("Age of pet:"))

if pet == "Cat" and age > 5:
    print("Senior cat food")
    
elif pet == "Dog" and age < 2:
    print("puppy food")    