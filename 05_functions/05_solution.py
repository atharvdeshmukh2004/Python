"""
5. Default Parameter Value
Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

"""
def greet(name="Sir"):
    return "Hello "+name

print(greet())  
print(greet("Atharv"))  