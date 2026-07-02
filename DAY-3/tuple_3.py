# TUPLES — MODULE 3
# (Advanced Tuples, Nested Tuples, *args, Functions, Generator Expressions)
# PART 1 — Coding Questions
# Q1

# Create a nested tuple:

# ((10,20),(30,40),(50,60))

# Print every element using nested loops.

# Q2

# Print only the second inner tuple.

# Q3

# Print only the value 40 from

# ((10,20),(30,40),(50,60))
# Q4

# Create

# [(10,20),(30,40),(50,60)]

# Print every tuple using a loop.

# Q5

# Create

# ((10,20),[30,40],(50,60))

# Append 100 to the list and print the tuple.

# Q6

# Create a 3×3 matrix using tuples.

# Example

# (
# (1,2,3),
# (4,5,6),
# (7,8,9)
# )

# Print row by row.

# Q7

# Print every element of the matrix using nested loops.

# Q8

# Find the sum of all elements in the matrix without using sum().

# Q9

# Search whether 40 exists without using in.

# Q10

# Find the frequency of 20 without using count().

# (10,20,30,20,40,20)
# Q11

# Find the frequency of every element.

# Example output

# 10 -> 1
# 20 -> 3
# 30 -> 1
# 40 -> 1
# Q12

# Create a tuple of squares from 1 to 10 using a generator expression.

# Example

# tuple(x*x for x in range(1,11))
# Q13

# Create a tuple containing only even numbers from 1 to 20.

# Q14

# Create a tuple containing only odd numbers from 1 to 20.

# Q15

# Create a function

# def add(a,b):

# Return both

# Sum
# Product

# using a tuple.

# Q16

# Call the above function and unpack the returned values.

# Q17

# Create a function using *args.

# Print all numbers passed to it.

# Q18

# Create another function using *args.

# Return the largest value without using max().

# Q19

# Create a function using *args.

# Return the total without using sum().

# Q20

# Create a function

# student()

# Return

# ("Sunny",21,"AIDS")

# Unpack and print the values.

# PART 2 — Output Prediction
# Q21
# a=((1,2),(3,4))
# print(a[1][0])
# Q22
# a=((10,20),(30,40))
# for row in a:
#     print(row)
# Q23
# a=(x*x for x in range(3))
# print(tuple(a))
# Q24
# def fun():
#     return 10,20

# a,b=fun()
# print(a,b)
# Q25
# def fun(*x):
#     print(len(x))

# fun(10,20,30)
# Q26
# def fun(*x):
#     print(x)

# fun(5)
# Q27
# a=((1,2),(3,4))
# print(len(a))
# Q28
# a=((1,2),(3,4))
# print(a[-1][-1])
# Q29
# a=tuple(x for x in range(5))
# print(a)
# Q30
# def fun():
#     return ("Python","Java")

# print(fun())
# PART 3 — Placement / Interview Questions
# Q31

# Explain the difference between

# (x*x for x in range(5))

# and

# tuple(x*x for x in range(5))
# Q32

# Explain why this works:

# t=((10,20),[30,40])
# t[1].append(50)
# Q33

# Can a tuple be used as a dictionary key?

# Show with code.

# Q34

# Can a tuple containing a list be used as a dictionary key?

# Explain with code.

# Q35

# Find the largest element from a nested tuple.

# Q36

# Find the smallest element from a nested tuple.

# Q37

# Find the sum of all elements in a nested tuple.

# Q38

# Flatten

# ((1,2),(3,4),(5,6))

# into

# (1,2,3,4,5,6)
# Q39

# Using *args, find

# Sum
# Average

# without using sum().

# Q40

# Write a function that returns three values.

# Receive them using multiple assignment.

# PART 4 — Google / Amazon Challenge
# Q41

# Given

# matrix = (
#     (10,20,30),
#     (40,50,60),
#     (70,80,90)
# )

# Without using

# sum()
# max()
# min()

# perform all of the following:

# Print every row.
# Print every element.
# Find total sum.
# Find average.
# Find largest element.
# Find smallest element.
# Count even numbers.
# Count odd numbers.
# Search whether 50 exists.
# Find the frequency of every element.
# Flatten the matrix into one tuple.
# Create a tuple of squares using a generator expression.
# Create a function using *args to calculate the total of the flattened tuple.
# Return the largest and smallest values from a function and unpack them.
# Print the total number of iterations performed.

# This completes Tuple Module 3. After this, your tuple preparation will be placement-ready, and we'll move on to Sets.