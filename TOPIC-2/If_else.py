# Q1 Take a person's age as input.
# If age is greater than or equal to 18, print:
# Eligible to Vote
# Otherwise print:
# Not Eligible to Vote
age = int(input("enter your age:"))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")
    
# Q2 Take marks as input.
# If marks are greater than or equal to 35, print:
# Pass
# Otherwise print:
# Fail
exam_marks=int(input("enter your marks"))
if exam_marks >=35:
    print("Pass")
else:
    print("Fail")

# Q3 Take a number.
# If it is positive, print:
# Positive Number
# Otherwise print:
# Negative Number
num=int(input("enter the number"))
if num >0 :
    print("positive number")
else:
    print("Negative number")

# Q4
# Take two numbers.
# Print:
# First Number is Greater
# or
# Second Number is Greater
num1=int(input("enter the number"))
num2=int(input("enter the number"))
if num1 > num2 :
    print("first number is greater")
else:
    print("Second number is greater")
    
# Q5 Take a password.
# Correct password:
# python123
# If correct:
# Login Successful
# Else:
# Invalid Password
password=input("enter the password")
correct_pass="python123"
if password==correct_pass:
    print("Login Successful")
else:
    print("Invalid Password")

# Q6 Take a username.
# Correct username:
# Sunny
# If correct:
# Welcome Sunny
# Else:
# User Not Found
username=input("enter the username")
correct_user="Sunny"
if username==correct_user:
    print("Welcome Sunny")
else:
    print("User Not Found")

# Q7 Take a number.
# If number is divisible by 5 print:
# Divisible by 5
# Else:
# Not Divisible by 5
num=int(input("enter a number"))
if num%5==0:
    print("Divisible by 5")
else:
    print("not divisible by 5")

# Q8 Take temperature.
# If temperature is greater than 30 print:
# Hot Weather
# Else print:
# Pleasant Weather
temperature=float(input("enter the temperature"))
if temperature > 30:
    print("Hot Weather")
else:
    print("Pleasent Weather")
    
# Q9 Take salary.
# If salary is greater than or equal to 50000 print:
# High Salary
# Else print:
# Average Salary
salary=int(input("enter the salary"))
if salary >= 50000:
    print("High salary")
else:
    print("Average Salary")

# Q10 Take an integer.
# If it is even print:
# Even
# Else print:
# Odd
integer=int(input("enter the interger"))
if integer%2==0:
    print("Even")
else:
    print("odd")
    
# PART-2 : OUTPUT PREDICTION

# Predict the output without running.

# Q11
age = 20
if age >= 18:
    print("Adult")
else:
    print("Child")
# output:- Adult

# Q12
marks = 25
if marks >= 35:
    print("Pass")
else:
    print("Fail")
# output:- Fail

# Q13
x = -5
if x > 0:
    print("Positive")
else:
    print("Negative")
# output:- Negative

# Q14
a = 10
b = 20
if a > b:
    print(a)
else:
    print(b)
# output:-  20

# Q15
password = "python123"

if password == "python123":
    print("Login")
else:
    print("Invalid")
# output:- Login

# Q16
number = 15

if number % 5 == 0:
    print("Yes")
else:
    print("No")
# output:- Yes    
    
# Q17
salary = 60000

if salary >= 50000:
    print("High")
else:
    print("Low")
# output:- High

# Q18
temp = 28
if temp > 30:
    print("Hot")
else:
    print("Cool")
# output:- Cool

# Q19
x = 10
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
# output:- Even

# Q20
username = "Sunny"
if username == "Admin":
    print("Welcome")
else:
    print("Access Denied")
# output:- Access Denied

# PART-3 : FAANG TRICKY QUESTIONS

# These are the type of logical questions asked in screening rounds.

# Q21
if True:
    print("A")
print("B")
# output:- a,b

# Q22
if False:
    print("A")
else:
    print("B")
print("C")
# output:- b,c

# Q23
x = 0
if x:
    print("True")
else:
    print("False")
# output:- False

# Q24
if "":
    print("Python")
else:
    print("Java")
# output:-Java

# Q25
if "False":
    print("Google")
else:
    print("Microsoft")
# output:- Google

# PART-4 : Small Logic Questions (Placement Level)
# These are frequently asked in online coding assessments.

# Q26
# Check whether a number is divisible by both 3 and 5.
num=int(input("enter the number"))
if num%3==0 and num%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisible with both 3 and 5")
    
    
# Q27
# Check whether a student is eligible for placement.
# Condition:
# CGPA ≥ 7.5
# Print eligible or not eligible.
cgpa=float(input("enter the cgpa"))
if cgpa >=7.5:
    print("eligible")
else:
    print("not eligible")

# Q28
# Check whether a person is eligible for a driving license.
# Condition:
# Age ≥ 18
age=int(input("enter the age"))
if age>=18:
    print("eligible for driving license")
else:
    print("not eligible")

# Q29
# Take a character.
# Check whether it is a vowel.
character=input("enter the char")
vowel="aeiou"
if character.lower() in vowel:
    print("vowel")
else:
    print("not a vowel")

# Q30
# Take a number.
# Check whether it is divisible by 2 or 7.
num=int(input("enter the number"))
if num%2==0 or num%7==0:
    print("divisible by 2 or 7")
else:
    print("not divisible")


