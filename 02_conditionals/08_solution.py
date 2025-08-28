"""
Password Strength Checker
Check if password is "Weak","Medium" or "Strong"
Criteria:<6 char(Weak),6-10 cahr(Medium) or >10char(Strong)

"""
char = input("Enter your password:")

if len(char) < 6:
    Password = "Weak"
elif len(char) < 10:
    Password = "Medium"
elif len(char) >10:
    Password = "Strong"

print("Enterd password is:",Password)        