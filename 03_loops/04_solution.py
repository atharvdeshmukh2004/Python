"""
4. Reverse a String
Problem: Reverse a string using a loop.

"""
input_str = "Python"
reverse_str = ""

for char in input_str:
    reverse_str = char + reverse_str

print(reverse_str)