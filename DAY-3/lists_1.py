# ============================================
# LISTS - MODULE 1
# (Introduction, Creation, Basic Properties)
# ============================================
# PART-1 : Coding Questions
# Q1
# Create an empty list named numbers.
numbers=[]
numbers=list()
# Q2

# Create a list containing:
# 10, 20, 30, 40, 50
# Print the list.
num=[10,20,30,40,50]
print(num)

# Q3
# Create a list of five fruits.
# Print the list.
fruits=["mango","kiwi","banana","watermelon","orange"]
print(fruits)

# Q4
# Create a list containing:
# 10
# 3.14
# "Python"
# True
# Print the list.
data=[10,3.14,"Python",True]
print(data)

# Q5
# Create a nested list containing:
# [1,2,3]
# [4,5,6]
# [7,8,9]
# Print the complete list.
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(nested_list)

# Q6
# Create a list of your favourite movies.
# Print the list.
movies=["f1","bahubali","avengers","avatar"]
print(movies)

# Q7
# Create a list of your family members' names.
# Print the list.
family=["shameem","sunny","masthanbasha","soniya"]
print(family)

# Q8
#  Create a list of five floating-point numbers.
# Print the list.
floating=[3.14,7.5,6.7,8.5,6.8]
print(floating)

# Q9
# Create a list of five Boolean values.
# Print the list.
boolean=[True,True,False,False,True]
print(boolean)

# Q10
# Create an empty list.
# Add no elements.
# Print the list.
list=[]
print(list)

# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# a = [10,20,30]
# print(a)

# Predict Output.:- [10,20,30]

# Q12
# a = []
# print(a)

# Predict Output.:- []

# Q13
# a = [1,2,3]

# print(len(a))

# Predict Output.:- 3

# Q14
# a = [10]
# print(type(a))
# Predict Output.:-<class 'list'>

# Q15
# a = ["Python",100,True]
# print(a)
# Predict Output.:- ['Python',100,True]

# Q16
# a = [[1,2],[3,4]]
# print(a)
# Predict Output.:- [[1,2],[3,4]]

# Q17
# a = [10,20,30]
# print(type(a))
# Predict Output.:- <class 'list'>

# Q18
# a = [1,2,3]
# b = a
# print(b)
# Predict Output.:- [1,2,3]

# Q19
# a = [10,20]
# print(len(a))
# Predict Output.:- 2

# Q20
# a = [10,20,30]
# print(a,a)
# Predict Output.:- [10,20,30] [10,20,30]

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================

# Q21
# a = [10]
# print(type(a))
# Predict Output.:-<class 'list'>

# Q22
# a = list()
# print(a)
# Predict Output.:- []

# Q23
# a = list("Python")
# print(a)
# Predict Output.:- ['P','y','t','h','o','n']

# Q24
# a = list((10,20,30))
# print(a)
# Predict Output.:-[10,20,30]

# Q25
# a = [1,2,3]
# print(bool(a))
# Predict Output.:-True

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26

# Create a list of your favourite programming languages.

# Print:

# The list
# Its type
# Its length
programs=["python","c","java","javascript"]
print(programs)
print(type(programs))
print(len(programs))

# Q27
# Create a list containing:
# Integer
# Float
# String
# Boolean
# List
# Print the list.
l=[3,3.14,"sunny",True,[1,2]]
print(l)

# Q28
# Create two different lists.
# Print both lists together.
s=[1,2,3,"sunny"]
b=[4,5,6,"soniya"]
print(s,b)
print(s+b)


# Q29

# Create a nested list representing:

# Class A
# Class B
# Class C
nes_list=[["ClassA",["sunny","raffi","mahesh"]],["ClassB",["sunny","raffi","mahesh"]],["ClassC",["sunny","raffi","mahesh"]]]
print(nes_list)
# Each class should contain three student names.

# Print the nested list.

# Q30
# Create a list containing:
# Name
# Age
# College
# CGPA
# Print the list.
details=["sunny",20,"N.B.K.R",7.5]
print(details)

# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31
# Create a nested list representing a student database.
# Each student should have:
# Name
# Age
# Department
# CGPA
# Store information for 5 students.
# Finally print the entire database.
student=[["Name",["sunny","raffi","mahesh","govardhan","suresh"]],["Age",[20,19,21,21,19]],["Department",["AIDS","PharmD","bussiness","AIDS","pharmD"]],["CGPA",[9,7.9,8,9.5,9]]]
print(student)
