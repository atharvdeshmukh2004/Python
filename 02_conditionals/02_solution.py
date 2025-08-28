"""
Movie tickit pricing
Movie tickets price based on age:$12 for Adults (18 and over) ,
$8 for childern . Everyone gets $2 discount on every Wednesday
"""
user_age = input("Enetr your age:")
age = int(user_age)
day = input("Enter the day:")

if age >= 18:
    price =12   

else:
    price = 8  

if day=="Wednesday":
     price = price-2
   
print("Ticket price for you is:$",price)  