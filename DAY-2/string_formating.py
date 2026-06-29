# ============================================
# STRING FORMATTING - MODULE 3
# (f-string, format(), format specifiers)
# ============================================
# PART-1 : Coding Questions
# Q1
# # Create:
# # name = "Sunny"
# # age = 20
# # Print:
# # My name is Sunny and I am 20 years old.
# # Use an f-string.
name = "Sunny"
age = 20
print(f"My name is {name} and I am {age} years old ")

# Q2
# # Create:
# # product = "Laptop"
# # price = 65000
# # Print:
# # Laptop costs ₹65000.
# # Use an f-string.
product = "Laptop"
price = 65000
print(f"{product} costs ₹{price}")

# Q3
# # Create:
# # radius = 10
# # area = 3.14159 * radius ** 2
# # Print the area with 2 decimal places using an f-string.
radius=10
area =3.14159 * radius ** 2
print(f"{area:.2f}")

# Q4
# # Create:
# # marks = 87.45678
# # Print the marks with 2 decimal places.
marks = 87.45678
print(f"{marks:.2f}")

# Q5
# # Create:
# # num = 25
# # Print:
# # Number = 00025
# # (Use formatting only.)
num=25
print(f"number = "'%05d'%num)
print("{:05}".format(num))
# Q6
# # Create:
# # name = "Python"
# # Print it centered in a width of 20.
name = "Python"
print("{:.^20}".format(name))
# Q7
# # Create:
# # name = "Python"
# # Print it left aligned in a width of 15.
name = "Python"
print("{:<15}".format(name))
# Q8
# # Create:
# # name = "Python"
# # Print it right aligned in a width of 15.
name = "Python"
print("{:>15}".format(name))
# Q9
# # Create:
# # pi = 3.1415926535
# # Print pi with 4 decimal places.
pi = 3.1415926535
print(f"{pi:.4f}")

# Q10
# # Create:
# # percentage = 92.5678
# # Print:
# # Percentage: 92.57%
# # Use formatting.
percentage = 92.5678
print("{:.2f}%".format(percentage))

# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# name = "Sunny"
# print(f"Hello {name}")
# Predict Output:- Hello Sunny

# Q12
# age = 20

# print(f"Age = {age}")

# Predict Output:- Age = 20

# Q13
# x = 12.56789

# print(f"{x:.2f}")

# Predict Output:- 12.57

# Q14
# num = 5

# print(f"{num:05}")

# Predict Output:- 00005

# Q15
# name = "AI"

# print(f"{name:^10}")

# Predict Output:    AI    

# Q16
# name = "Python"

# print(f"{name:<10}")

# Predict Output:Python

# Q17
# name = "Python"

# print(f"{name:>10}")

# Predict Output:=          Python

# Q18
# value = 1234

# print(f"{value:,}")

# Predict Output:- 1,234

# Q19
# pi = 3.141592

# print(f"{pi:.3f}")

# Predict Output:-3.141

# Q20
# num = 45

# print(f"{num:b}")

# Predict Output:- 101101

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# name = "Sunny"
# age = 20

# print("{} {}".format(name, age))

# Predict Output:- Sunny 20

# Q22
# print("{1} {0}".format("Python", "Java"))

# Predict Output :- Java Python

# Q23
# print("{name} is {age}".format(name="Sunny", age=20))

# Predict Output:- Sunny is 20

# Q24
# num = 15

# print(f"{num:x}")

# Predict Output:- f

# Q25
# num = 15

# print(f"{num:o}")

# Predict Output:-17

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26
# # Take your name and age.
# # Print:
# # My name is ____ and I am ____ years old.
# # Use an f-string.

name = "Sunny"
age = 20
print(f"My name is {name} and I am {age} years old ")

# Q27
# # Take a float number.
# # Print it with 3 decimal places.
x = 12.56789
print(f"{x:.3f}")


# Q28
# # Take a number.
# # Print it as a 6-digit number by adding leading zeros.
num=25
print(f"number = "'%06d'%num)
print("{:06}".format(num))


# Q29
# # Take your salary.
# # Print it with commas.
# # Example:
# # 1500000
# # Output:
# # 1,500,000
salary=1500000
print("{:,}".format(salary))

# Q30
# # Take your CGPA.
# # Print:
# # CGPA = __.__
# # (2 decimal places)
cgpa=7.54567
print(f"cgpa = {cgpa:.2f}")
# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31
# # Take the following inputs:
# # Name
# # Age
# # CGPA
# # Salary

# # Print exactly like this:

# # -----------------------------
# # STUDENT DETAILS
# # -----------------------------
# # Name   : Sunny
# # Age    : 20
# # CGPA   : 8.75
# # Salary : 5,00,000
# # -----------------------------

# # Use only f-strings and formatting.
Name="Sunny"
Age=20
CGPA=8.75
Salary=500000

print("-----------------------------")
print("STUDENT DETAILS")
print("-----------------------------")
print(f"Name     : {Name}")
print(f"Age      : {Age}")
print("CGPA     : {:.2f}".format(CGPA))
print("Salary   : {:,}".format(Salary))



print(f"{'Name':<8}: {Name}")
print(f"{'Age':<8}: {Age}")
print(f"{'CGPA':<8}: {CGPA:.2f}")
print(f"{'Salary':<8}: {Salary:,}")
