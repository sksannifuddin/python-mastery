# ============================================
# LISTS - MODULE 3
# (append(), extend(), insert())
# ============================================
# PART-1 : Coding Questions
# Q1
# Create an empty list.
# Add 10 using append().
# Print the list.
empty_list=[]
empty_list.append(10)
print(empty_list)
# Q2
# Create
# numbers = [10,20]
# Add 30 using append().
# Print the list.
numbers=[10,20]
numbers.append(30)
print(numbers)

# Q3
# Create
# fruits = ["Apple","Banana"]
# Append "Mango".
# Print the list.
fruits=["Apple","Banana"]
fruits.append("Mango")
print(fruits)

# Q4
# Create
# colors = ["Red","Blue"]
# Insert "Green" at index 1.
# Print the list.
color=["Red","Blue"]
color.insert(1,"Green")
print(color)

# Q5
# Create
# numbers = [10,20,40]
# Insert 30 at index 2.
# Print the list.
numbers=[10,20,40]
numbers.insert(2,30)
print(numbers)

# Q6
# Create
# a = [1,2]
# b = [3,4]
# Use extend() to combine them.
# Print the result.
a=[1,2]
b=[3,4]
a.extend(b)
print(a)

# Q7
# Create
# languages = ["Python"]
# Extend it with
# ["Java","C++","Go"]
# Print the list.
languages=["Python"]
languages.extend(["Java","C++","Go"])
print(languages)

# Q8
# Create
# marks = [70,80]
# Append 90.
# Append 100.
# Print the list.
marks=[70,80]
marks.append(90)
marks.append(100)
print(marks)

# Q9
# Create
# letters = ["A","C","D"]
# Insert "B" at the correct position.
# Print the list.
letters=["A","C","D"]
letters.insert(1,"B")
print(letters)

# Q10
# Create
# cities = ["Delhi","Mumbai"]
# Extend it wit
# ["Hyderabad","Chennai"]
# Print the list.
cities=["Delhi","Mumbai"]
cities.extend(["Hyderabad","Chennai"])
print(cities)


# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# a = [10]
# a.append(20)
# print(a)
# Predict Output.:- [10,20]

# Q12
# a = [1,2]
# a.extend([3,4])
# print(a)
# Predict Output.:-[1,2,3,4]

# Q13
# a = [10,30]
# a.insert(1,20)
# print(a)
# Predict Output.:- [10,20,30]

# Q14
# a = []
# a.append(100)
# print(len(a))

# Predict Output.:- 1

# Q15
# a = [1]
# a.extend([2])

# print(a)

# Predict Output.:[1,2]

# Q16
# a = [10]
# a.insert(0,5)
# print(a)
# Predict Output.:- [5,10]

# Q17
# a = [10]
# a.insert(5,20)
# print(a)
# Predict Output.:- [10,20]

# Q18
# a = [1,2]
# a.append([3,4])
# print(a)
# Predict Output.:-[1,2,[3,4]]

# Q19
# a = [1,2]

# a.extend([3,4])

# print(len(a))

# Predict Output.:- 4

# Q20
# a = [1]

# a.extend("AB")

# print(a)

# Predict Output.:- [1,'A','B']

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# a = [1,2]

# a.append([3,4])

# print(len(a))

# Predict Output.:- 3

# Q22
# a = [1,2]

# a.extend([[3,4]])

# print(a)

# Predict Output.:-[1,2,[3,4]]

# Q23
# a = [10]

# a.insert(-1,5)

# print(a)

# Predict Output.:-[5,10]

# Q24
# a = []

# a.extend("Python")

# print(a)

# Predict Output.:- ['P','y','t','h','o','n']

# Q25
# a = [10]

# a.append(20)

# a.extend([30])

# print(a)

# Predict Output:- [10,20,30]

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26

# Create an empty list.

# Append the numbers:

# 10
# 20
# 30
# 40
# 50

# Print the list.:- 
a=[]
a.append(10)
a.append(20)
a.append(30)
a.append(40)
a.append(50)
print(a)

# Q27

# Create two lists.

# Merge them using extend().

# Print the merged list.
a=[2,3,4,5]
b=[6,7,8,9]
a.extend(b)
print(a)


# Q28

# Create a list:

# [10,20,40,50]

# Insert 30 in the correct position.

# Print the list.
l=[10,20,40,50]
l.insert(2,30)
print(l)


# Q29

# Create a list of your five favourite movies.

# Insert your favourite movie at the beginning.

# Print the list.
l=["f1","avatar","avengers","bahubali","jersey"]
l.insert(0,"jersey")
print(l)

# Q30

# Create a list of programming languages.

# Append "Rust".

# Insert "Python" at index 0.

# Extend the list with

# ["Go","Kotlin"]

# Print the final list.
programming=[]
programming.append("Rust")
programming.insert(0,"Python")
programming.extend(["Go","Kotlin"])
print(programming)


# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31

# Create an empty list.

# Perform the following operations in order:

# Append 10
# Append 20
# Append 30
# Insert 15 at index 1
# Extend with [40,50,60]
# Insert 5 at the beginning
# Append [70,80] (not extend)
# Extend "AB"

# Finally print:

# The final list
# Length of the list
# First element
# Last element
# Second last element
# Type of the last element
# 📌 Interview Concepts Covered

l=[]
l.append(10)
l.append(20)
l.append(30)
l.insert(1,15)
l.extend([40,50,60])
l.insert(0,5)
l.append([70,80])
l.extend("AB")
print(l)
print(len(l))
print(l[0])
print(l[-1])
print(l[-2])
print(type(l[-1]))

