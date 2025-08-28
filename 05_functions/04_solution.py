"""
4. Function Returning Multiple Values
Problem: Create a function that returns both the area and circumference of a circle given its radius.

"""
import math

def area(radius):
    return math.pi* radius**2

def circumference(radius):
    return 2*math.pi*radius

print("Area:",area(3),"Circumference:",circumference(3))