"""
10. Recursive Function
Problem: Create a recursive function to calculate the factorial of a number.

"""
def rec(n):
    if n == 0: 
       return 1 
    else:     
      return n * rec(n-1)
       

print(rec(5))
