""" 
grade Calculator
Assign a letter to a student score : A(90-100),B(80-89),
C(70-79),D(60-69),F(below 60)

"""
stud_score = input("Enter student score:")
score = int(stud_score)

if score >100:
     print("Please verify your score")
     exit()
     
if score >=90:
    print("A")
elif score >=80: 
     print("B")    
elif score >=70:
     print("C")
elif score >=60:
     print("D")
else:
     print("F")