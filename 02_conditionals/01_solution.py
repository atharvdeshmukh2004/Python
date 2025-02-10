"""
Question 
   Age group categorization
   classify age group person: child(<13) , teeneger(13-19),
   adult(20-59),senior(60+)

"""

user_age = input ("Enetr your age:")
print(user_age)

if user_age<13:
    print("Child")
elif user_age<20:
    print("Teeneger")    
elif user_age<60:
    print("Adult")    
else:
    print("Senior")    