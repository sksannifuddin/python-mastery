# 📘 DICTIONARIES — MODULE 2
# (Dictionary Methods, Comprehensions, Nested Dictionaries, Merging, Sorting, Frequency)
# PART 1 — Coding Questions
# Q1

# Create:
# student={
#     "name":"Sunny",
#     "age":21
# }
# Print the value of "name" using get().
student={
    "name":"sunny",
    "age":21
}
print(student.get("name"))

# Q2
# Print the value of "salary" using get().
# If it doesn't exist, print "Not Found".
student={
    "name":"sunny",
    "age":21
}
print(student.get("name","not found"))

# Q3

# Use setdefault() to insert
# "course":"Python"
# Print the dictionary.
student={
    "name":"sunny",
    "age":21
}
student.setdefault("course","python")
print(student)

# Q4
# Use setdefault() on an existing key "name".
# Observe whether it changes.
student={
    "name":"sunny",
    "age":21
}
student.setdefault("name","govardhan")
print(student)

# Q5
# Merge two dictionaries using update()
d1={"A":10,"B":20}
d2={"C":30,"D":40}
d1.update(d2)
print(d1)

# Q6
# Merge the same dictionaries using
# |
# (Python 3.9+)
d1={"A":10,"B":20}
d2={"C":30,"D":40}
print(d1|d2)

# Q7
# Create a dictionary using
# dict.fromkeys()
# Example
# keys=["A","B","C"]
# value=0
keys=["A","B","C"]
print(dict.fromkeys(keys,0))


# Q8

# Create a dictionary using
# dict()
# from a list of tuples.
l=[("A",10),("B",20),("C",30)]
print(dict(l))
# Example

# [("A",10),("B",20),("C",30)]

# Q9
# Create a dictionary comprehension
# Squares of numbers from 1–10.
# Expected
# {1:1,2:4,3:9...}
squares={x:x**2 for x in range(1,11) }
print(squares)

# Q10
# Create a dictionary comprehension
# Only even numbers from 1–20.
# Expected
# {2:4,4:16...}
evens={x:x**2 for x in range(1,21) if x%2==0 }
print(evens)

# Q11
# Convert
# names=["Sunny","Ravi","Ajay"]
# to
# {
# "Sunny":5,
# "Ravi":4,
# "Ajay":4
# }
# using dictionary comprehension.
names=["Sunny","Ravi","Ajay"]
name={x:len(x) for x in names}
print(name)

# Q12
# Create a nested dictionary.
# students={
# 1:{"name":"Sunny","age":21},
# 2:{"name":"Ravi","age":22}
# }
# Print the complete dictionary.
students={
1:{"name":"Sunny","age":21},
2:{"name":"Ravi","age":22}
}
print(students)

# Q13
# Print only Sunny's age from the nested dictionary.
students={
1:{"name":"Sunny","age":21},
2:{"name":"Ravi","age":22}
}
print(students[1]["age"])

# Q14
# Print every student's details using loops.

# Expected

# ID : 1
# name Sunny
# age 21
# Q15

# Create

# employees=[
# {"id":101,"salary":50000},
# {"id":102,"salary":60000}
# ]

# Print every employee's salary.

# Q16

# Create

# {
# "Math":[90,80,70],
# "Science":[85,75,65]
# }

# Print every mark using nested loops.

# Q17

# Reverse this dictionary.

# {
# "A":10,
# "B":20,
# "C":30
# }

# Expected

# {
# 10:"A",
# 20:"B",
# 30:"C"
# }
# Q18

# Sort a dictionary by keys.

# {
# "C":30,
# "A":10,
# "B":20
# }
# Q19

# Sort a dictionary by values.

# {
# "A":30,
# "B":10,
# "C":20
# }
# Q20

# Create

# text="banana"

# Find the frequency of every character using a dictionary.

# Expected

# b ->1
# a ->3
# n ->2
# Q21

# Create

# numbers=[10,20,20,30,40,40,40]

# Find the frequency of every number.

# Q22

# Merge

# {"A":10}

# and

# {"A":20,"B":30}

# Observe which value remains.

# Q23

# Create

# student={
# "name":"Sunny",
# "Math":90,
# "Science":80
# }

# Update all marks by adding 5.

# Q24

# Remove every key whose value is less than 50.

# {
# "A":20,
# "B":70,
# "C":40,
# "D":90
# }
# Q25

# Create a dictionary from two lists using dictionary comprehension.

# keys=["A","B","C"]
# values=[10,20,30]
# PART 2 — Output Prediction
# Q26
# d={"A":10}
# print(d.get("B"))
# Q27
# d={"A":10}
# print(d.get("B",0))
# Q28
# d={"A":10}
# d.setdefault("A",20)
# print(d)
# Q29
# d={"A":10}
# d.setdefault("B",20)
# print(d)
# Q30
# print(dict.fromkeys(["A","B"],100))
# Q31
# print(dict([("A",1),("B",2)]))
# Q32
# print({x:x*x for x in range(3)})
# Q33
# print({x:x for x in range(5) if x%2==0})
# Q34
# d={"A":10,"B":20}
# print(list(d.items()))
# Q35
# d={"A":10}
# d.update({"A":50})
# print(d)
# PART 3 — Placement Questions
# Q36

# Explain the difference between

# get()
# []

# with code.

# Q37

# Explain the difference between

# update()
# |

# with examples.

# Q38

# Explain the difference between

# setdefault()
# update()
# Q39

# Reverse a dictionary without using built-in reverse functions.

# Q40

# Explain why dictionary keys must be unique.

# Show with code.

# Q41

# Sort a dictionary by values in ascending order.

# Q42

# Find the frequency of every word in:

# "python java python ai java python"
# Q43

# Convert

# {"A":10,"B":20}

# to

# [("A",10),("B",20)]

# using dictionary methods.

# PART 4 — Google / Amazon Challenge
# Q44

# Given

# students={
# 101:{"name":"Sunny","Math":90,"Science":80},
# 102:{"name":"Ravi","Math":75,"Science":95},
# 103:{"name":"Ajay","Math":88,"Science":91}
# }

# Without using:

# sum()
# max()
# min()

# Find:

# Total marks of each student
# Average of each student
# Overall highest mark
# Overall lowest mark
# Student having highest total
# Search whether student ID 102 exists
# Search whether student ID 110 exists
# Print all names
# Print all subjects and marks
# Count total iterations
# Q45

# Given

# text="programming"

# Perform:

# Character frequency
# Highest frequency character
# Lowest frequency character
# Total unique characters
# Print characters in alphabetical order
# Reverse the frequency dictionary
# Print only vowels with frequency
# Print only consonants with frequency

# ✅ This module covers every remaining dictionary concept except function-related dictionary usage (**kwargs), which we'll do in the Functions topic as you requested.