# PART 1 — Coding Questions
# Q1

# Create two tuples:
# a = (10,20,30)
# b = (40,50,60)
# Concatenate them and print the result.
a = (10,20,30)
b = (40,50,60)
c=a+b
print(c)

# Q2
# Create:
# a = ("Python","Java")
# Repeat it 3 times and print the result.
a = ("Python","Java")
b=a*3
print(b)

# Q3
# Compare:
# a = (10,20)
# b = (10,20)
# Print:
# a == b
# a != b
a = (10,20)
b = (10,20)
print(a==b)
print(a!=b)

# Q4
# Compare:
# a = (10,20)
# b = (10,30)
# Print:
# a < b
# a > b
a = (10,20)
b = (10,30)
print(a<b)
print(a>b)

# Q5
# Create:
# a = (10,20)
# b = (10,20)
# Print:
# a is b
# a is not b
a = (10,20)
b = (10,20)
print(a is b)
print(a is not b)

# Q6
# Create:
# numbers = (50,20,80,10,30)
# Print:
# min(numbers)
# max(numbers)
# sum(numbers)
numbers = (50,20,80,10,30)
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# Q7
# Sort this tuple using sorted():
# numbers = (50,20,80,10,30)
# Print the result and its type.
numbers=(50,20,80,10,30)
num=sorted(numbers)
print(num)
print(type(num))


# Q8
# Convert this list to a tuple:
# data = [10,20,30]
# Print the tuple and its type.
data = [10,20,30]
a=tuple(data)
print(a)
print(type(a))

# Q9
# Convert this tuple to a list:
# data = (10,20,30)
# Print the list and its type.
data = (10,20,30)
a=list(data)
print(a)
print(type(a))

# Q10
# Use enumerate() on:
# names = ("Sunny","Ravi","Ajay")
# Print index and value.
names = ("Sunny","Ravi","Ajay")
for i, val in enumerate(names):
    print(i,val)

# Q11
# Use zip() on:
# names = ("Sunny","Ravi","Ajay")
# marks = (90,80,70)
# Print name and mark together.
names = ("Sunny","Ravi","Ajay")
marks = (90,80,70)
a=zip(names , marks)
print(tuple(a))

# Q12
# Unpack:
# student = ("Sunny",21,"AIDS")
# into:
# name, age, branch
# Print all values.
student = ("Sunny",21,"AIDS")
names,age,branch=student
print(names)
print(age)
print(branch)


# Q13

# Use multiple assignment:
# a,b,c = 10,20,30
# Print all values.
a,b,c = 10,20,30
print(a)
print(b)
print(c)

# Q14
# Swap two variables using tuple unpacking:
a = 100
b = 200
a,b=b,a
print(a,b)

# Q15

# Try to modify:
# t = (10,20,30)
# Change 20 to 200.
t = (10,20,30)
t.insert(1,200)
print(t)
# it gives AttributeError: 'tuple' object has no attribute 'insert'
# Write the code and comment the error.

# Q16

# Convert tuple to list, modify it, and convert back:

# t = (10,20,30)
# Change 20 to 200.
t = (10,20,30)
b=list(t)
b[1]=200
t=tuple(b)
print(t)

# Q17
# Create:
# t = ([10,20], [30,40])
# Append 50 to the first inner list and print t.
t = ([10,20], [30,40])
t[0].append(50)
print(t)

# Q18
# Create:
# a = (1,2,3)
# b = a
a = (1,2,3)
b = a
# Print:

# a is b
# a == b

print( a is b)
print( a == b)

# Q19

# Create:

# a = (1,2,3)
# b = tuple(a)

a = (1,2,3)
b = tuple(a)
# Print:

# a is b
# a == b
print( a is b)
print( a == b)

# Q20

# Create:
# a = [1,2,3]
# b = tuple(a)
# c = list(b)
a = [1,2,3]
b = tuple(a)
c = list(b)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
# Print a, b, c and their types.

# PART 2 — Output Prediction
# Q21
# a = (1,2)
# b = (3,4)
# print(a+b)
# output:-(1,2,3,4)

# Q22
# a = (10,)
# print(a*4)
# output:-(10,10,10,10)

# Q23
# a = (10,20)
# b = (10,20)
# print(a == b) 
# output:-True
# Q24
# a = (10,20)
# b = (10,30)
# # print(a < b)
#  output:-True
# Q25
# a = (1,2,3)
# print(min(a), max(a), sum(a))
# a=(1,2,3)
# output:-
# print(min(a),max(a),sum(a))


# Q26
# a = (3,1,2)
# print(sorted(a))
# output:-[1,2,3]

# Q27
# a = (10,20,30)
# b = list(a)
# print(type(b))
# output:-<class 'list'>

# Q28
# a = [10,20,30]
# b = tuple(a)
# print(type(b))
# output:-<class 'tuple'>

# Q29
# a = ("A","B")
# for i,v in enumerate(a):
#     print(i,v)
# output:-
# 0 'A'
# 1 'B'

# Q30
# a = ("Sunny","Ravi")
# b = (90,80)
# print(tuple(zip(a,b)))
# output:-
# (('Sunny',90),('Ravi',80))

# PART 3 — Placement / Interview Questions
# Q31
# Explain with code the difference between:
# ==
# and
# is
# for tuples.
a=(1,2,3)
b=(1,2,3)
print(a==b)
print(a is b)
#  here == checks the value in the vriables but is checks the memory address of the both variables 

# Q32
# Why can’t we modify a tuple directly? Show with code.
# tuple is immutable we cant change add,remove , modify directly , we can change only by converting it into list and then converting it back into tuple


# Q33

# If tuple is immutable, why does this work?
# t = ([10,20], [30,40])
# t[0].append(50)
# print(t)
# it is list inside tuple where we can change the list 

# Q34

# Take:
# names = ("Sunny","Ravi","Ajay")
# marks = (90,80,70)
# Use zip() to create:
# (("Sunny",90),("Ravi",80),("Ajay",70))
names = ("Sunny","Ravi","Ajay")
marks = (90,80,70)
total=tuple(zip(names,marks))
print(total)

# Q35

# Use enumerate() to print:

# Student 1 : Sunny
# Student 2 : Ravi
# Student 3 : Ajay
names = ("Sunny","Ravi","Ajay")
for i,value in enumerate(names):
    print(f"student {i+1} : {value}")

# Q36
# Convert:
# t = (10,20,30,40)
# to list, remove 30, convert back to tuple.
t = (10,20,30,40)
a=list(t)
a.remove(30)
t=tuple(a)
print(t)


# Q37
# Create two tuples and compare them using all:
# ==, !=, <, >
a=(1,2)
b=(1,3)
print(a==b)
print(a!=b)
print(a<b)
print(a>b)

# Q38
# Use tuple unpacking to swap three variables:
# a = 10
# b = 20
# c = 30
# Make:
# a = 30
# b = 10
# c = 20
a = 10
b = 20
c = 30
a,b,c=c,a,b
print(a,b,c)

# Q39
# Given:
# data = ((1,2),(3,4))
# Use unpacking in loop:
# for a,b in data:
# Print both values.
data = ((1,2),(3,4))
for a,b in data:
    print(a,b)
    
data = ((1,2),(3,4))
for a in data:
    for b in a:
        print(b)

# Q40
# Create a tuple from string:
# "Python"
# using tuple().
t="Python"
t=tuple(t)
print(t)

# PART 4 — Google/Amazon Challenge
# Q41
# Given:
# names = ("Sunny","Ravi","Ajay","Sonia")
# marks = (90,80,70,95)

# Do all:

# Use zip() to combine names and marks.
# Convert zipped result to tuple.
# Print each name and mark using loop.
# Find highest mark.
# Find lowest mark.
# Find total marks.
# Sort marks using sorted().
# Convert marks tuple to list.
# Append 100.
# Convert it back to tuple.
# Compare original marks tuple and modified tuple using ==.
# Compare using is.

# This is Module 2 with all your listed topics included.

names = ("Sunny","Ravi","Ajay","Sonia")
marks = (90,80,70,95)
highest=marks[0]
smallest=marks[0]
total=0
t=zip(names,marks)
b=tuple(t)
for a,c in b:
    print(a,c)
    total+=c
    if c >highest:
        highest=c
    if c<smallest:
        smallest=c
a=sorted(marks)
d=list(marks)
d.append(100)
d=tuple(d)
print(d)
print(b)
print(highest)
print(smallest)
print(total)
print(a)
print(marks==d)
print(marks is d)



        