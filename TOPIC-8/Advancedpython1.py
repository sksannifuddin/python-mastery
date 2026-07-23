# # 📘 ADVANCED PYTHON — MODULE 1
# # (Iterators, Generators, Decorators, Closures, Collections, itertools, functools, datetime, os, sys)
# # PART 1 — 30 Coding Questions with Answers

# ---

# ## Q1
# ### Create an iterator from a list using `iter()` and `next()`.

# ### Answer

# ```python
# numbers = [10, 20, 30]

# it = iter(numbers)

# print(next(it))
# print(next(it))
# print(next(it))
# ```

# ---

# ## Q2
# ### What happens when `next()` is called after the iterator ends?

# ### Answer

# ```python
# numbers = [10, 20]

# it = iter(numbers)

# print(next(it))
# print(next(it))

# # print(next(it))
# # StopIteration
# ```

# ---

# ## Q3
# ### Create a custom iterator from 1 to 5.

# ### Answer

# ```python
# class NumberIterator:

#     def __init__(self):
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.current <= 5:
#             value = self.current
#             self.current += 1
#             return value

#         raise StopIteration

# obj = NumberIterator()

# for i in obj:
#     print(i)
# ```

# ---

# ## Q4
# ### Create a custom iterator for even numbers.

# ### Answer

# ```python
# class EvenIterator:

#     def __init__(self):
#         self.current = 2

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.current <= 10:
#             value = self.current
#             self.current += 2
#             return value

#         raise StopIteration

# for i in EvenIterator():
#     print(i)
# ```

# ---

# ## Q5
# ### Create a simple generator using `yield`.

# ### Answer

# ```python
# def numbers():

#     yield 10
#     yield 20
#     yield 30

# g = numbers()

# print(next(g))
# print(next(g))
# print(next(g))
# ```

# ---

# ## Q6
# ### Create a generator from 1 to 5.

# ### Answer

# ```python
# def generate():

#     for i in range(1, 6):
#         yield i

# for value in generate():
#     print(value)
# ```

# ---

# ## Q7
# ### Create a generator for even numbers.

# ### Answer

# ```python
# def even():

#     for i in range(2, 21, 2):
#         yield i

# for value in even():
#     print(value)
# ```

# ---

# ## Q8
# ### Create a generator that returns squares.

# ### Answer

# ```python
# def squares():

#     for i in range(1, 11):
#         yield i ** 2

# for value in squares():
#     print(value)
# ```

# ---

# ## Q9
# ### Generator for Fibonacci numbers.

# ### Answer

# ```python
# def fibonacci(n):

#     a = 0
#     b = 1

#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# for value in fibonacci(10):
#     print(value)
# ```

# ---

# ## Q10
# ### Difference between a list and a generator.

# ### Answer

# ```python
# numbers = [x for x in range(5)]

# generator = (x for x in range(5))

# print(numbers)

# print(generator)
# ```

# ---

# ## Q11
# ### Create a basic decorator.

# ### Answer

# ```python
# def decorator(function):

#     def wrapper():

#         print("Before Function")

#         function()

#         print("After Function")

#     return wrapper


# @decorator
# def greet():
#     print("Hello")


# greet()
# ```

# ---

# ## Q12
# ### Decorator that measures execution time.

# ### Answer

# ```python
# import time

# def timer(function):

#     def wrapper():

#         start = time.time()

#         function()

#         end = time.time()

#         print("Execution Time:", end - start)

#     return wrapper


# @timer
# def display():

#     for i in range(1000000):
#         pass

# display()
# ```

# ---

# ## Q13
# ### Decorator with arguments.

# ### Answer

# ```python
# def decorator(function):

#     def wrapper(name):

#         print("Welcome")

#         function(name)

#     return wrapper


# @decorator
# def greet(name):
#     print(name)

# greet("Sunny")
# ```

# ---

# ## Q14
# ### Nested Function.

# ### Answer

# ```python
# def outer():

#     def inner():
#         print("Inner Function")

#     inner()

# outer()
# ```

# ---

# ## Q15
# ### Closure Example.

# ### Answer

# ```python
# def outer(name):

#     def inner():
#         print(name)

#     return inner

# function = outer("Sunny")

# function()
# ```

# ---

# ## Q16
# ### Function returning another function.

# ### Answer

# ```python
# def calculate():

#     def add(a, b):
#         return a + b

#     return add

# function = calculate()

# print(function(10, 20))
# ```

# ---

# ## Q17
# ### Use `Counter`.

# ### Answer

# ```python
# from collections import Counter

# text = "banana"

# count = Counter(text)

# print(count)
# ```

# ---

# ## Q18
# ### Find the most common element.

# ### Answer

# ```python
# from collections import Counter

# numbers = [1,2,2,3,3,3,4]

# count = Counter(numbers)

# print(count.most_common(1))
# ```

# ---

# ## Q19
# ### Use `defaultdict`.

# ### Answer

# ```python
# from collections import defaultdict

# data = defaultdict(int)

# data["A"] += 1

# print(data)
# ```

# ---

# ## Q20
# ### Use `deque`.

# ### Answer

# ```python
# from collections import deque

# queue = deque()

# queue.append(10)
# queue.append(20)

# print(queue)

# queue.popleft()

# print(queue)
# ```

# ---

# ## Q21
# ### Use `itertools.count()`.

# ### Answer

# ```python
# from itertools import count

# counter = count(1)

# for i in range(5):
#     print(next(counter))
# ```

# ---

# ## Q22
# ### Use `itertools.cycle()`.

# ### Answer

# ```python
# from itertools import cycle

# colors = cycle(["Red","Blue","Green"])

# for i in range(6):
#     print(next(colors))
# ```

# ---

# ## Q23
# ### Use `itertools.repeat()`.

# ### Answer

# ```python
# from itertools import repeat

# for value in repeat("Python",5):
#     print(value)
# ```

# ---

# ## Q24
# ### Use `reduce()`.

# ### Answer

# ```python
# from functools import reduce

# numbers = [1,2,3,4,5]

# result = reduce(lambda x,y: x+y, numbers)

# print(result)
# ```

# ---

# ## Q25
# ### Reduce for multiplication.

# ### Answer

# ```python
# from functools import reduce

# numbers = [1,2,3,4]

# result = reduce(lambda x,y: x*y, numbers)

# print(result)
# ```

# ---

# ## Q26
# ### Print today's date.

# ### Answer

# ```python
# from datetime import datetime

# today = datetime.now()

# print(today)
# ```

# ---

# ## Q27
# ### Print current year, month and day.

# ### Answer

# ```python
# from datetime import datetime

# today = datetime.now()

# print(today.year)
# print(today.month)
# print(today.day)
# ```

# ---

# ## Q28
# ### Print current working directory.

# ### Answer

# ```python
# import os

# print(os.getcwd())
# ```

# ---

# ## Q29
# ### Print Python version.

# ### Answer

# ```python
# import sys

# print(sys.version)
# ```

# ---

# ## Q30 — Google/Amazon Challenge

# ### Create a Student Data Analyzer.

# Requirements:

# - Generate student IDs using a generator.
# - Store marks using `Counter`.
# - Use a decorator to measure execution time.
# - Print today's date.
# - Print Python version.
# - Print current directory.
# - Find the total marks using `reduce()`.

# ### Answer

# ```python
# from collections import Counter
# from functools import reduce
# from datetime import datetime
# import os
# import sys
# import time

# def student_ids():

#     for i in range(101,106):
#         yield i

# def timer(function):

#     def wrapper():

#         start = time.time()

#         function()

#         end = time.time()

#         print("Execution Time:", end-start)

#     return wrapper


# @timer
# def analyze():

#     marks = [90,95,90,80,95]

#     print("Student IDs")

#     for sid in student_ids():
#         print(sid)

#     print()

#     print("Counter")

#     print(Counter(marks))

#     print()

#     total = reduce(lambda x,y:x+y, marks)

#     print("Total Marks:", total)

#     print()

#     print("Today's Date:", datetime.now())

#     print()

#     print("Current Directory:", os.getcwd())

#     print()

#     print("Python Version:")

#     print(sys.version)

# analyze()
# ```

# ---

# # ✅ Advanced Python Module 1 Completed

# ### Topics Covered

# - ✅ Iterators
# - ✅ Custom Iterators
# - ✅ Generators
# - ✅ Decorators
# - ✅ Closures
# - ✅ Nested Functions
# - ✅ `Counter`
# - ✅ `defaultdict`
# - ✅ `deque`
# - ✅ `itertools`
# - ✅ `functools.reduce`
# - ✅ `datetime`
# - ✅ `os`
# - ✅ `sys`
# - ✅ Google/Amazon Challenge

# ## Next Module

# **Advanced Python Module 2** will cover:

# - Lambda
# - map()
# - filter()
# - zip()
# - enumerate()
# - any()
# - all()
# - eval()
# - exec()
# - Memory optimization
# - Interview tricks
# - Google/Amazon advanced coding questions