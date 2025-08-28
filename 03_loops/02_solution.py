"""
2. Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.

"""
n=10
sum = 0

for num in range(1,n+1):
    if num%2==0:
        sum += num

print("Sum of n even numbers:",sum)        