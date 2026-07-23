# 📘 FUNCTIONS — MODULE 2 (Advanced Functions)
# Topics Covered (100%)
# Recursion
# Basic Recursion
# Factorial
# Fibonacci
# Sum of digits
# Reverse number
# Palindrome
# Anonymous Functions
# Lambda
# Functional Programming
# map()
# filter()
# reduce()
# Utility Functions
# any()
# all()
# enumerate()
# zip()
# Nested Functions
# Nested Functions
# Closures
# LEGB Rule
# Scope Resolution
# First-Class Functions
# Functions as Objects
# Functions as Arguments
# Functions Returning Functions
# Decorators
# Basic Decorators
# Decorators with Arguments
# Multiple Decorators
# functools.wraps
# Advanced Concepts
# Memoization
# Function Caching
# Questions (40)



# Part 1 — Coding Questions (25)
# Factorial using recursion.
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
# Q2. Fibonacci using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=" ")
# Q3. Sum of digits using recursion.
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(12345))
# Q4. Reverse a number using recursion.
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n//10, rev*10 + n%10)

print(reverse_number(12345))
# Q5. Palindrome using recursion.
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

print(palindrome("madam"))
print(palindrome("python"))
# Q6. Lambda for square.
square = lambda x: x*x

print(square(5))
# Q7. Lambda for maximum.
largest = lambda a,b: a if a>b else b

print(largest(10,20))
# Q8. Lambda for sorting.
students=[
("Sunny",90),
("Ajay",70),
("Ravi",80)
]

print(sorted(students,key=lambda x:x[1]))
# Q9. map() to square numbers.
numbers=[1,2,3,4,5]

result=list(map(lambda x:x*x,numbers))

print(result)
# Q10. map() to uppercase names.
names=["sunny","ravi","ajay"]

result=list(map(str.upper,names))

print(result)
# Q11. filter() even numbers.
numbers=[1,2,3,4,5,6,7,8]

result=list(filter(lambda x:x%2==0,numbers))

print(result)
names=["Sunny","Ravi","Sannifuddin","Ajay"]

result=list(filter(lambda x:len(x)>5,names))

print(result)
# Q13. reduce() sum.
from functools import reduce

numbers=[1,2,3,4,5]

result=reduce(lambda x,y:x+y,numbers)

print(result)
# Q14. reduce() multiplication.
from functools import reduce

numbers=[1,2,3,4,5]

result=reduce(lambda x,y:x*y,numbers)

print(result)
# Q15. any() example.
numbers=[0,0,5,0]

print(any(numbers))
# Q16. all() example.
numbers=[1,2,3,4]

print(all(numbers))
# Q17. enumerate() example.
names=["Sunny","Ajay","Ravi"]

for index,value in enumerate(names):
    print(index,value)
# Q18. zip() example.
names=["Sunny","Ajay","Ravi"]
marks=[90,80,95]

for name,mark in zip(names,marks):
    print(name,mark)
# Q19. Nested function.
def outer():

    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()
# Q20. Closure example.
def outer(msg):

    def inner():
        print(msg)

    return inner

x=outer("Hello Python")

x()
# Q21. Function as argument.
def square(x):
    return x*x

def display(fun,value):
    print(fun(value))

display(square,5)
# Q22. Function returning function.
def outer():

    def inner():
        print("Hello World")

    return inner

x=outer()

x()
# Q23. Basic decorator.
def decorator(fun):

    def wrapper():
        print("Before Function")
        fun()
        print("After Function")

    return wrapper


@decorator
def hello():
    print("Hello Python")

hello()
# Q24. Decorator measuring execution time.
import time

def timer(fun):

    def wrapper():

        start=time.time()

        fun()

        end=time.time()

        print("Execution Time:",end-start)

    return wrapper


@timer
def test():

    for i in range(1000000):
        pass

test()
# Q25. Memoization example.
cache={}

def fibonacci(n):

    if n in cache:
        return cache[n]

    if n<=1:
        return n

    cache[n]=fibonacci(n-1)+fibonacci(n-2)

    return cache[n]

print(fibonacci(10))
# Part 2 — Output Prediction (5)
# Q26 — Recursion Output
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)

fun(3)
# Output
# 3
# 2
# 1
# Explanation

# The function prints first, then calls itself with n - 1.

# Q27 — Lambda Output
square = lambda x: x * x
print(square(6))

# Q28 — map() Output
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
# Output
# [2, 4, 6, 8]

# map() returns a map object, so it is converted into a list.

# Q29 — Closure Output
def outer(x):
    def inner(y):
        return x + y
    return inner

add_10 = outer(10)

print(add_10(5))
# Output
# 15

# The inner function remembers the value x = 10 even after outer() finishes.

# Q30 — Decorator Output
def decorator(function):
    def wrapper():
        print("Start")
        function()
        print("End")
    return wrapper

@decorator
def display():
    print("Python")

display()
# Output
# Start
# Python
# End
# 📘 PART 3 — Placement Questions (Q31–Q35)
# Q31 — Recursion vs Iteration
# Recursion

# A function calls itself repeatedly until it reaches a base condition.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
# Iteration

# A loop repeats instructions.

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))
# Main differences
# Recursion	Iteration
# Function calls itself	Uses loops
# Requires a base case	Requires loop condition
# Uses more call-stack memory	Usually uses less memory
# Often easier for tree-like problems	Usually faster for simple repetition
# Can cause RecursionError	No recursion depth problem
# Q32 — Lambda vs Normal Function
# Lambda function
square = lambda x: x * x
print(square(5))
# Normal function
def square(x):
    return x * x

print(square(5))
# Difference
# Lambda is anonymous and normally contains one expression.
# A normal function can contain multiple statements, loops, conditions and documentation.
# Lambda is useful for short operations in map(), filter() and sorting.
# A normal function is better for complex and reusable logic.
# Q33 — map() vs filter()
# map()

# Transforms every element.

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * x, numbers))

print(result)

# Output:

# [1, 4, 9, 16]
# filter()

# Selects only elements that satisfy a condition.

numbers = [1, 2, 3, 4]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# Output:

# [2, 4]
# Q34 — Closure vs Nested Function
# Nested function

# A function defined inside another function.

def outer():
    def inner():
        print("Inner function")

    inner()

outer()
# Closure

# A returned inner function that remembers variables from the enclosing scope.

def outer(message):
    def inner():
        print(message)

    return inner

show = outer("Hello")
show()

# Every closure uses a nested function, but not every nested function becomes a closure.

# # Q35 — Decorator vs Normal Function

# A normal function performs its own task.

def greet():
    print("Hello")

# A decorator adds extra behaviour without changing the original function's code.

def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()

# Part 4 — Google/Amazon Challenge (5)
# Q36 — Student Management using Functions
students = {
    "Sunny": [90, 80, 95],
    "Ravi": [75, 85, 70],
    "Ajay": [88, 91, 84]
}

def student_report(students):

    for name, marks in students.items():

        total = 0

        for mark in marks:
            total += mark

        average = total / len(marks)

        print(f"{name}")
        print("Total =", total)
        print("Average =", average)
        print()

student_report(students)
# Q37 — Recursive Calculator
def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2,5))
# Q38 — Employee Payroll System
employees = {
    "Sunny":50000,
    "Ravi":60000,
    "Ajay":45000,
    "Sonia":80000
}

def payroll(data):

    highest = 0
    total = 0

    for salary in data.values():

        total += salary

        if salary > highest:
            highest = salary

    average = total / len(data)

    print("Total Salary =", total)
    print("Average Salary =", average)
    print("Highest Salary =", highest)

payroll(employees)
# Q39 — Library Management Function System
library = [
    "Python",
    "Java",
    "AI",
    "Machine Learning"
]

def search_book(book):

    if book in library:
        print("Book Available")
    else:
        print("Book Not Available")

search_book("Python")
search_book("C++")
# ⭐ Q40 — Google / Amazon Final Challenge
# Write one program that uses:
# Functions
# Recursion
# Lambda
map()
filter()
reduce()
# Closures
# Decorators
from functools import reduce

def timer(function):

    def wrapper(*args, **kwargs):

        print("Program Started")

        result = function(*args, **kwargs)

        print("Program Finished")

        return result

    return wrapper


def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n - 1)


def multiplier(x):

    def inner(y):
        return x * y

    return inner


@timer
def analyze(numbers):

    squares = list(map(lambda x: x*x, numbers))

    even = list(filter(lambda x: x % 2 == 0, numbers))

    total = reduce(lambda x, y: x + y, numbers)

    print("Numbers :", numbers)
    print("Squares :", squares)
    print("Even :", even)
    print("Total :", total)

    print("Factorial of 5 =", factorial(5))

    double = multiplier(2)

    print("Closure Result =", double(10))


analyze([10,20,30,40,50])