#Decision making statements

#if statement
#if condition:
#     block of code
#     .
#     . 
#     .
#if condition:
#   if-block
#else:
#     else-block

#Eg for if statement
from unittest import case


age=17
if age>=18:
    print("Adult")

#if-else statement
if age>=18:
    print("Adult")
else:
    print("Child")
print("after if block")

#if-elif-else statement
if age>0 and age<13:
    print("Child")
elif age>=13 and age<20:
    print("Teenager")
elif age>=20 and age<60:
    print("Adult")
elif age>=60:
    print("Senior Citizen")
else:
    print("Invalid entry")

#Nested if statement
# if age>=18:
#     print("Adult")
#     if age>=18 and age<60:
#         print("Eligible for job")
#     else:
#         print("Not eligible for job")

age=int(input("Enter your age:"))
mark=int(input("Enter your mark:"))
if age>=18:
    print("Age requirement satisfied")
    if mark>=50:
        print("Eligible for Admission")
    else:
        print("Not eligible for Admission: Insufficient marks")
else:
    print("Admission Rejected: Age requirement not satisfied")
    
#Match statement used to match a value with a case and execute the corresponding block of code. It is similar to switch-case statements in other programming languages.
#match expression:
    # case value1:
    #     case block1
    # case value2:
    #     case block2
    # .
    # .
    # .
    # case valueN:
    #     case blockN
        
day=int(input("Enter day number:"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case _:
        print("Invalid entry")
        
mark=int(input("Enter your mark:"))
if mark>90 and mark<=100:
    print("A+")
elif mark>80 and mark<=90:
    print("A")
elif mark>70 and mark<=80:
    print("B+")
elif mark>60 and mark<=70:
    print("B")
elif mark>50 and mark<=60:
    print("C")
elif mark>40 and mark<=50:
    print("D")
elif mark<40 and mark>=0:
    print("E")
else:
    print("Invalid mark entry!")
    
day="sunday"
match day.capitalize(): #use capitalize() to make the first letter uppercase and the rest lowercase for case-insensitive matchingq2
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Sunday" | "Saturday":
        print("Weekend")
    case _:
        print("Invalid")