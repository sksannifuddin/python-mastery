# SETS — MODULE 3
# Advanced Sets, Comprehension, Hashing, Interview Tricks
# PART 1 — Coding Questions
# Q1
# Create a set of squares from 1 to 10 using set comprehension.


# Q2
# Create a set of even numbers from 1 to 50 using set comprehension.

# Q3
# Create a set of odd numbers from 1 to 50 using set comprehension.

# Q4
# Given:

# numbers=[10,20,20,30,40,40,50]

# Create a set using comprehension.

# Q5
# Given:

# words=["apple","banana","apple","mango","banana"]

# Create a set of unique words.

# Q6
# Create a set of first letters from:

# names=["Sunny","Ravi","Ajay","Sonia"]

# Q7
# Create a set of word lengths from:

# words=["python","java","go","javascript"]

# Q8
# Given:

# numbers={10,20,30,40,50,60}

# Create a new set containing numbers greater than 30.

# Q9
# Given:

# numbers={5,10,15,20,25,30}

# Create a set containing numbers divisible by 5 and greater than 10.

# Q10
# Given:

# a={10,20,30,40}
# b={30,40,50,60}

# Find elements common to both sets without using intersection().

# Q11
# Find elements present in a but not in b without using difference().

# Q12
# Find elements present in either set but not both without using symmetric_difference().

# Q13
# Given:

# data=[10,20,20,30,30,40,50,50]

# Find duplicate elements using set logic.

# Q14
# Given:

# data=[10,20,30,40]

# Check whether all elements are unique.

# Q15
# Given:

# s={10,20,30}

# Try adding a list [40,50] into the set. Comment the error.

# Q16
# Add a tuple (40,50) into a set.

# Q17
# Create a set containing frozensets:

# frozenset({1,2})
# frozenset({3,4})

# Q18
# Given:

# students={"Sunny","Ravi","Ajay"}
# passed={"Sunny","Ajay"}

# Find students who failed.

# Q19
# Given:

# python_students={"Sunny","Ravi","Ajay"}
# java_students={"Ravi","Sonia","Ajay"}

# Find students who know both Python and Java.

# Q20
# Find students who know only one language.

# PART 2 — Output Prediction

# Q21

# s={x*x for x in range(5)}
# print(s)

# Q22

# s={x for x in range(10) if x%2==0}
# print(s)

# Q23

# s=set("banana")
# print(s)

# Q24

# s={1,True,0,False}
# print(s)

# Q25

# s={10,20,30}
# # print(s[0])

# Predict the error.

# Q26

# s={10,20,30}
# s.add((40,50))
# print(s)

# Q27

# s={10,20,30}
# # s.add([40,50])

# Predict the error.

# Q28

# a={1,2,3}
# b={3,4,5}
# print(a-b)
# print(b-a)

# Q29

# a={1,2,3}
# b={3,4,5}
# print((a|b)-(a&b))

# Q30

# s=frozenset({1,2,3})
# # s.add(4)

# Predict the error.

# PART 3 — Placement / Interview Questions

# Q31
# Explain why sets are unordered.

# Q32
# Explain why sets remove duplicates automatically.

# Q33
# Explain why lists cannot be added into sets.

# Q34
# Explain why tuples can be added into sets.

# Q35
# Explain why True and 1 are treated as duplicate-like values in a set.

# Q36
# Find duplicate elements from a list using only set logic.

# Q37
# Find unique elements from a list.

# Q38
# Check whether two lists have at least one common element using sets.

# Q39
# Check whether one list is fully contained inside another using sets.

# Q40
# Find common characters between two strings using sets.

# PART 4 — Google / Amazon Challenge

# Q41

# Given:

# students_all = {"Sunny","Ravi","Ajay","Sonia","Mahesh","Kiran"}

# python = {"Sunny","Ajay","Mahesh"}
# java = {"Ravi","Ajay","Sonia"}
# sql = {"Sunny","Sonia","Kiran"}

# Find:

# Students who know Python or Java
# Students who know both Python and Java
# Students who know Python but not Java
# Students who know Java but not Python
# Students who know exactly one of Python or Java
# Students who know all three: Python, Java, SQL
# Students who know none of the three
# Whether all Python students are in students_all
# Whether students_all is a superset of SQL students
# Whether Python and SQL are disjoint
# Total unique students who know at least one skill
# Convert final result to frozenset
