# Q1 Take the user's name as input and print:
# Hello Sunny, Welcome to Python.
name=input("enter your name")
print(f"Hello {name}, Welcome to Python.")

# Q2 Take age as input and print:
# Your age is 20
age=int(input("enter your age"))
print(f"your age is {age}")

# Q3 Take two numbers as input and print their sum.
a=int(input("enter a number"))
b=int(input("enter a number"))
print(a+b)

# Q4 Take length and breadth as input and calculate area of rectangle.
l=float(input("enter the length"))
b=float(input("enter the breadth"))
area=l*b
print(f"area of a rectangle: {area}cm²")

# Q5 Take radius as input and calculate area of circle.
# Use:
# import math
import math
radius=float(input("enter the radius"))
area=math.pi*radius**2
print(f"Area of a Circle: {area:.2f}cm²")

# Q6 Take principal, rate, and time as input and calculate simple interest.
principal=float(input("enter the principal"))
rate=float(input("enter the rate"))
time=float(input("enter the time"))
simple_interest=(principal*rate*time)/100
print(f"simple interest: {simple_interest}")

# Q7 Take temperature in Celsius and convert it to Fahrenheit.
# Formula:
# (F = C × 9/5 + 32)
c=float(input("enter the temperature"))
f=(c*9/5)+32
print(f)

# Q8 Take your name, age, and college as input and display them using f-strings.
name=input("enter your name")
age=int(input("enter your age"))
college=input("enter your college")
print(f"My name is {name} , my age is {age} and my college name is {college}")

# Q9 Take quantity and price as input and calculate total bill.
quantity=int(input("enter the quantity"))
price=float(input("enter the price"))
total_bill=quantity*price
print(total_bill)

# Q10 Take your birth year as input and calculate current age.
# Use:
# 2026
# as current year.
birth_year=int(input("enter your birth year"))
current_age=2026-birth_year
print(f"my age is {current_age}")



# Q11
name = input("Enter name: ")
print(name)
# What datatype is name?
# output:- string datatype

# Q12
age = input("Enter age: ")
print(type(age))
# Output:- string datatype

# Q13
num = input("Enter number: ")
print(num + num)
# User enters:
# 10
# Output:- 1010

# Q14
num = int(input("Enter number: "))
print(num + num)
# User enters:
# 10
# Output:- 20

# Q15
a = input()
b = input()
print(a + b)
# User enters:
# 10
# 20
# Output:- 1020

# Q16
a = int(input())
b = int(input())
print(a + b)
# User enters:
# 10
# 20
# Output:- 30

# Q17
name = "Sunny"
age = 20
print(f"My name is {name} and I am {age} years old")
# Output:- My name is Sunny and I am 20 years old

# Q18
x = input("Enter number: ")
print(type(x))
# User enters:
# 100
# Output:- <class 'str'>

# Q19
x = float(input())
print(type(x))
# User enters:
# 10.5
# Output:- <class 'float'>

# Q20
x = int(input())
print(type(x))
# User enters:
# 50
# Output:- <class 'int'>

# Tricky Interview Questions
# Q21
age = input()
print(age + 10)
# Will it work or give an error?
# it will give the error because input is string and 10 is int value so it gives value error

# Q22
age = int(input())
print(age + 10)
# Will it work?
# yes, it will work because both are integers

# Q23
x = input()
print(bool(x))
# User enters:
# 0
# Output:- True

# Q24
x = input()
print(type(x))
# User enters:
# True
# Output:- <class 'bool'>

# Q25
x = input()
print(x * 3)
# User enters:
# 5
# Output:- 555

