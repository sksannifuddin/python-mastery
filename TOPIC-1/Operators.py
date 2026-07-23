# Q1 Take two numbers and print:
# Addition
# Subtraction
# Multiplication
# Division
a=float(input("enter the number"))
b=float(input("enter the number"))
addition=a+b
difference=a-b
multiplication=a*b
division=a/b
print(f"addition:{addition}")
print(f"difference:{difference}")
print(f"multiplication:{multiplication}")
print(f"division:{division}")

# Q2 Take two numbers and print:
# Floor Division (//)
# Modulus (%)
a=float(input("enter the number"))
b=float(input("enter the number"))
floor_division=a//b
modulus=a%b
print(f"floor division: {floor_division}")
print(f"modulus: {modulus}")
# Q3 Take a number and print its square using:
# **
a=float(input("enter the number"))
print(f"square:{a**2}")
# Q4 Take a number and print its cube.
a=float(input("enter the number"))
print(f"cube:{a**3}")
# Q5 Check whether a number is even or odd using %.
a=float(input("enter the number"))
if a%2==0:
    print("even")
else:
    print("odd")
# Q6 Take two numbers and print:
# a > b
# a < b
# a == b
a=float(input("enter the number"))
b=float(input("enter the number"))
print(a>b)
print(a<b)
print(a==b)
# Q7 Take age as input.
# Check whether:
# age >= 18
# Print result.
age=int(input("enter your age:"))
print(age>=18)
if age >=18:
    print("yes")
else:
    print("no")
# Q8 Take marks.
# Check whether:
# marks >= 35
# Print result.
marks=int(input("enter your marks:"))
print(marks>=35)
if marks >=35:
    print("yes")
else:
    print("no")
# Q9 Create:
# username = "sunny"
# Check:
# "sun" in username
username="sunny"
print("sun" in username)
if "sun" in username:
    print("yes")
else:
    print("no")
# Q10 Create:
# languages = ["Python","Java","C"]
# Check:
# "Python" in languages
languages = ["Python","Java","C"]
print("Python" in languages)
if "Python" in languages:
    print("yes")
else:
    print("no")


# Q11
print(10 + 5 * 2)
# output:- 20

# Q12
print((10 + 5) * 2)
# output:- 30

# Q13
print(10 // 3)
# output:- 3

# Q14
print(10 % 3)
# output:- 1

# Q15
print(2 ** 3)
# output:- 8

# Q16
print(10 > 5)
# output:- True

# Q17
print(10 == "10")
# output:- False

# Q18
print(True and False)
# output:- False

# Q19
print(True or False)
# output:- True

# Q20
print(not True)
# output:- False


# Q21
print(5 > 3 and 10 > 5)
# output:- True

# Q22
print(5 > 3 and 10 < 5)
# output:- False

# Q23
print(5 > 3 or 10 < 5)
# output:- True

# Q24
a = [1, 2, 3]
b = a
print(a is b)
# output:- True

# Q25
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(a in b)
# output:- True
# False
#False

# Bonus FAANG Question
x = 2
y = 3
z = 4
print(x + y * z ** 2)
# output:- 50
