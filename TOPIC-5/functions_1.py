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
def sum_product(*args):
    sum=0
    product=1
    for i in args:
        sum+=i
        product*=i
    return sum,product
print(sum_product(1,2,3,4,5))

# Unpack returned values.
a,b=sum_product(1,2,3,4,5)
print(a)
print(b)
# Default arguments.
def greet(name="sunny"):
    print(f"hello {name}! Welcome to Google office")
    
# Keyword arguments.
def personal_details(**kwargs):
    for key,val in kwargs.items():
        print(f"{key} : {val} ")
personal_details(name="sunny",age="21",college="Nbkr")

# Mix positional and keyword arguments.
def details(*args,**kwargs):
    for val in args:
        print(f"positional arguments : {val}")
    for key,val in kwargs.items():
        print(f"{key} : {val}")
details(1,2,3,4,name="sunny",age="21",college="Nbkr")

# Find total using *args.
def total(*args):
    total=0
    for i in args:
        total+=i
    return total
print(total(1,2,3,4,5,6,7,8,9,10))
# Find average using *args.

def average(*args):
    total=0
    count=0
    for i in args:
        total+=i
        count+=1
    average=total/count
    return average
print(average(1,2,3,4,5,6,7,8,9,10))


# Google Mini Challenge using *args.
# Part 2 — Output Prediction (5)
# Q25
# Google Mini Challenge using *args.
# Create one function that accepts any number of integers.
# Without using sum(), max(), min(), find:
# Total
# Average
# Largest
# Smallest
# Even count
# Odd count

def analyze(*args):
    if not args:
        return "No values provided"

    total = 0
    count = 0
    largest = args[0]
    smallest = args[0]
    even_count = 0
    odd_count = 0

    for num in args:
        total += num
        count += 1

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    average = total / count

    return total, average, largest, smallest, even_count, odd_count


total, average, largest, smallest, even_count, odd_count = analyze(
    10,20,30,40,50
)

print("Total:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Count:", even_count)
print("Odd Count:", odd_count)

# Q26
# return vs print

def first():
    print(10)

def second():
    return 20

a = first()
b = second()

print(a)
print(b)

# Output:
# 10
# None
# 20

# Explanation:
# print(10) displays 10 but the function returns None.
# return 20 sends 20 back to the caller.
# Q27
# Local variable output

def show():
    x = 100
    print(x)

show()

# print(x)
# NameError: name 'x' is not defined

# Output:
# 100

# x is a local variable and exists only inside show().
# Q28
# Global variable output

x = 50

def show():
    print(x)

show()
print(x)

# Output:
# 50
# 50

# The function can read the global variable x.
# Q29
# Default parameter output

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sunny")

# Output:
# Hello Guest
# Hello Sunny
# Q30
# Keyword argument output

def student(name, age):
    print(name, age)

student(age=21, name="Sunny")

# Output:
# Sunny 21

# Keyword arguments can be supplied in a different order.
# PART 3 — Placement Questions
# Q31
# Difference between parameter and argument.

def greet(name):
    print("Hello", name)

greet("Sunny")

# name is a parameter.
# "Sunny" is an argument.

# Parameter:
# A variable written in the function definition.

# Argument:
# The actual value passed during the function call.
# Q32
# Difference between local and global variables.

x = 100

def show():
    y = 200
    print("Global x:", x)
    print("Local y:", y)

show()

print("Global x outside:", x)

# print(y)
# NameError

# Global variable:
# Created outside a function and can usually be accessed throughout the program.

# Local variable:
# Created inside a function and available only inside that function.
# Q33
# Difference between return and print.

def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(10, 20)
y = add_return(10, 20)

print("x =", x)
print("y =", y)

# Output:
# 30
# x = None
# y = 30

# print() only displays a value.
# return sends a value back to the caller.
# A returned value can be stored and reused.
# Q34
# Why use functions?

# Functions are used because they:
# 1. Avoid repeated code.
# 2. Make programs easier to read.
# 3. Divide a large program into smaller parts.
# 4. Make testing and debugging easier.
# 5. Allow code reuse.
# 6. Improve maintainability.

def calculate_total(a, b):
    return a + b

print(calculate_total(10, 20))
print(calculate_total(30, 40))
# Q35
# Difference between positional and keyword arguments.

def student(name, age, course):
    print(name, age, course)

# Positional arguments
student("Sunny", 21, "Python")

# Keyword arguments
student(course="Python", name="Sunny", age=21)

# Positional arguments depend on their order.
# Keyword arguments use parameter names, so their order can change.
# PART 4 — Google/Amazon Challenges
# Q36
# Student Result Analyzer
# Create a function that accepts a student's name and marks.
# Find:
# Total
# Average
# Highest mark
# Lowest mark
# Pass or Fail
# Grade

def student_result(name, *marks):
    if not marks:
        return "No marks provided"

    total = 0
    count = 0
    highest = marks[0]
    lowest = marks[0]
    failed = False

    for mark in marks:
        total += mark
        count += 1

        if mark > highest:
            highest = mark

        if mark < lowest:
            lowest = mark

        if mark < 35:
            failed = True

    average = total / count

    if failed:
        result = "Fail"
    else:
        result = "Pass"

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "F"

    return name, total, average, highest, lowest, result, grade


report = student_result("Sunny", 90, 80, 95, 100)

print("Name:", report[0])
print("Total:", report[1])
print("Average:", report[2])
print("Highest:", report[3])
print("Lowest:", report[4])
print("Result:", report[5])
print("Grade:", report[6])
# Q37
# Employee Salary Analyzer
# Accept any number of salaries using *args.
# Find:
# Total salary
# Average salary
# Highest salary
# Lowest salary
# Count salaries greater than 60000

def salary_analyzer(*salaries):
    if not salaries:
        return "No salaries provided"

    total = 0
    count = 0
    highest = salaries[0]
    lowest = salaries[0]
    above_60000 = 0

    for salary in salaries:
        total += salary
        count += 1

        if salary > highest:
            highest = salary

        if salary < lowest:
            lowest = salary

        if salary > 60000:
            above_60000 += 1

    average = total / count

    return total, average, highest, lowest, above_60000


result = salary_analyzer(50000, 65000, 45000, 80000, 70000)

print("Total Salary:", result[0])
print("Average Salary:", result[1])
print("Highest Salary:", result[2])
print("Lowest Salary:", result[3])
print("Above 60000:", result[4])
# Q38
# Bank Interest Calculator
# Create a function with:
# principal
# rate
# time
# Calculate simple interest and final amount.

def simple_interest(principal, rate=10, time=1):
    interest = principal * rate * time / 100
    final_amount = principal + interest

    return interest, final_amount


interest, amount = simple_interest(
    principal=50000,
    rate=8,
    time=2
)

print("Simple Interest:", interest)
print("Final Amount:", amount)
# Q39
# Marks Calculator
# Accept any number of marks using *args.
# Find:
# Total
# Average
# Highest
# Lowest
# Number of passed subjects
# Number of failed subjects

def marks_calculator(*marks):
    if not marks:
        return "No marks provided"

    total = 0
    count = 0
    highest = marks[0]
    lowest = marks[0]
    passed = 0
    failed = 0

    for mark in marks:
        total += mark
        count += 1

        if mark > highest:
            highest = mark

        if mark < lowest:
            lowest = mark

        if mark >= 35:
            passed += 1
        else:
            failed += 1

    average = total / count

    return total, average, highest, lowest, passed, failed


result = marks_calculator(90, 80, 34, 75, 25)

print("Total:", result[0])
print("Average:", result[1])
print("Highest:", result[2])
print("Lowest:", result[3])
print("Passed Subjects:", result[4])
print("Failed Subjects:", result[5])
# Q40
# Universal Number Analyzer
# Accept any number of values using *args.
# Without using:
# sum()
# max()
# min()
# len()
#
# Find:
# Total
# Average
# Largest
# Smallest
# Even count
# Odd count
# Positive count
# Negative count
# Zero count
# Numbers greater than average

def universal_analyzer(*numbers):
    if not numbers:
        return "No numbers provided"

    total = 0
    count = 0
    largest = numbers[0]
    smallest = numbers[0]

    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in numbers:
        total += num
        count += 1

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    average = total / count

    greater_than_average = []

    for num in numbers:
        if num > average:
            greater_than_average.append(num)

    return (
        total,
        average,
        largest,
        smallest,
        even_count,
        odd_count,
        positive_count,
        negative_count,
        zero_count,
        greater_than_average
    )


result = universal_analyzer(
    10, 20, -5, 0, 30, 15, -10, 40
)

print("Total:", result[0])
print("Average:", result[1])
print("Largest:", result[2])
print("Smallest:", result[3])
print("Even Count:", result[4])
print("Odd Count:", result[5])
print("Positive Count:", result[6])
print("Negative Count:", result[7])
print("Zero Count:", result[8])
print("Greater Than Average:", result[9])
