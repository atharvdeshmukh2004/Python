"""
Leap Year Checker
Determine year is a leap year(leap year is divisible by 4 ,
but not by 100 also divisible by 400)

"""
year = int(input("Enter year:"))

if (year%400==0)or(year%4==0 and year%100 !=0):
    print("leap year")

else:
    print("Not leap year")        
