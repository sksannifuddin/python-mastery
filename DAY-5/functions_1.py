# 📘 FUNCTIONS — MODULE 1 (Basics & Intermediate)
# Topics Covered (100%)
# Function Basics
# Function Introduction
# Why Functions?
# Syntax
# Function Definition
# Function Calling
# Parameters & Arguments
# Parameters
# Arguments
# Positional Arguments
# Keyword Arguments
# Default Arguments
# Return
# return statement
# Returning one value
# Returning multiple values
# Multiple assignment
# Variable Scope
# Local Variables
# Global Variables
# global keyword
# Special Features
# None
# pass
# Docstrings
# Function Annotations
# Built-in vs User-defined Functions
# Variable Length Arguments
# *args





# Questions (40)
# Part 1 — Coding Questions (25)
# Create a simple function that prints "Hello World".
def simple_function():
    return "hello world"
print(simple_function())
# Create a function that prints your name.
def name(name):
    print(f"my name is {name}")
name("sunny")
# Call one function three times.
def name(name):
    print(f"my name is {name}")
name("sunny")
name("ramesh")
name("suresh")
# Create a function with one parameter.
def name(name="sunny"):
    print(f"my name is {name}")
name()
# Function with two parameters.
def details(name="sunny",age="21"):
    print(f"my name is {name} and my age is {age}")
details()
# Find sum using function.
def add(a,b):
    return a+b
result=add(10,5)
print(result)
# Find largest of two numbers.
def greatest(a,b):
    if a>b:
        print("a is greater")
    elif a<b:
        print("b is greater")
    else:
        print("both are equal")
greatest(10,5)

# Find largest of three numbers.
def greatest(a,b,c):
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greater")
    elif c>a and c>b:
        print("c is greater")
    else:
        print("all  are equal")
greatest(10,5,11)
# Check even/odd using function.
def even_odd(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
even_odd(10)
# Print multiplication table using function.
def multiplication(b):
    for i in range(1,11):
        print(f"{b}x{i}={b*i}")
multiplication(5)
# Reverse a string using function.
def reverse(s):
    return s[::-1]
print(reverse("sunny"))

def reverse(s):
    for i in range(len(s) - 1, -1, -1):
        print(s[i])
reverse("sunny")

# Count vowels using function.
def vowels(s):
    count=0
    for i in s.lower():
        if i in "aeiou":
            count+=1
    return count
result=vowels("pomegranate")
print(result)

# Return square.
def square(a):
    return a**2
result=square(5)
print(result)

# Return cube.
def cube(a):
    return a**3
result=cube(5)
print(result)

# Return largest.
def larger(*args):
    if not  args:
        return "no value provided"
    large=args[0]
    for i in args:
        if i>large:
            large=i
    return large
print(larger(10,20,30))
print(larger())


def larger(a, b, c):
    numbers = [a, b, c]
    large = numbers[0]

    for i in numbers:
        if i > large:
            large = i

    return large

largest = larger(10, 20, 30)
print(largest)
       

# Return smallest.
def smallest(*args):
    if not args:
        return "no value provided"
    small=args[0]
    for i in args:
        if i<small:
            small=i
    return small
print(smallest(1,2,3,4,5,5,6))
    

# Return sum and product together.
# Unpack returned values.
# Default arguments.
# Keyword arguments.
# Mix positional and keyword arguments.
# Use *args.
# Find total using *args.
# Find average using *args.
# Google Mini Challenge using *args.
# Part 2 — Output Prediction (5)
# return vs print
# Local variable output
# Global variable output
# Default parameter output
# Keyword argument output
# Part 3 — Placement Questions (5)
# Difference between parameter and argument.
# Difference between local and global variables.
# Difference between return and print.
# Why use functions?
# Difference between positional and keyword arguments.
# Part 4 — Google/Amazon Challenge (5)
# Student Result Analyzer
# Employee Salary Analyzer
# Bank Interest Calculator
# Marks Calculator
# Universal Number Analyzer

