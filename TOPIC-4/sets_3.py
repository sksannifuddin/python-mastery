# SETS — MODULE 3
# Advanced Sets, Comprehension, Hashing, Interview Tricks
# PART 1 — Coding Questions
# Q1
# Create a set of squares from 1 to 10 using set comprehension.
square=set(x**2 for x in range(1,11))
print(square)
# Q2
# Create a set of even numbers from 1 to 50 using set comprehension.
even={x for x in range(1,11) if x%2==0}
print(even)

# Q3
# Create a set of odd numbers from 1 to 50 using set comprehension.
odd={x for x in range(1,51) if x%2!=0}
print(odd)

# Q4
# Given:
# numbers=[10,20,20,30,40,40,50]
# Create a set using comprehension.
numbers=[10,20,20,30,40,40,50]
sets={i for i in numbers}
print(sets)

# Q5
# Given:
# words=["apple","banana","apple","mango","banana"]
# Create a set of unique words.
words=["apple","banana","apple","mango","banana"]
s=set(words)
print(s)

# Q6
# Create a set of first letters from:
# names=["Sunny","Ravi","Ajay","Sonia"]
names=["Sunny","Ravi","Ajay","Sonia"]
sets=set()
for i in names:
    sets.add(i[0])
print(sets)
    
# Q7
# Create a set of word lengths from:
# words=["python","java","go","javascript"]
words=["python","java","go","javascript"]
word_length=set()
for i in words:
    word_length.add(len(i))
print(word_length)

words=["python","java","go","javascript"]
word_length={}
for i in words:
    word_length[i]=(len(i))
print(word_length)

# Q8
# Given:
# numbers={10,20,30,40,50,60}
# Create a new set containing numbers greater than 30.
numbers={10,20,30,40,50,60}
greatest=set()
for i in numbers:
    if i>30:
        greatest.add(i)
print(greatest)

# Q9
# Given:
# numbers={5,10,15,20,25,30}
# Create a set containing numbers divisible by 5 and greater than 10.
numbers={5,10,15,20,25,30}
data=set(i for i in numbers if i>10 and i%5==0)
print(data)

# Q10
# Given:
# a={10,20,30,40}
# b={30,40,50,60}
# Find elements common to both sets without using intersection().
a = {10,20,30,40}
b = {30,40,50,60}

result = set()

for i in a:
    if i in b:
        result.add(i)

print(result)


a={10,20,30,40}
b={30,40,50,60}
for i in a:
    if i in b:
        print(i)

# Q11
# Find elements present in a but not in b without using difference().
a={10,20,30,40}
b={30,40,50,60}
for i in a:
    if i not in b:
        print(i)
        

a = {10,20,30,40}
b = {30,40,50,60}

result = set()

for i in a:
    if i not in b:
        result.add(i)

print(result)

# Q12
# Find elements present in either set but not both without using symmetric_difference().
a = {10,20,30,40}
b = {30,40,50,60}
result = set()

for i in a:
    if i not in b:
        result.add(i)
for i in b:
    if i not in a:
        result.add(i)

print(result)

# Q13
# Given:
# data=[10,20,20,30,30,40,50,50]
# Find duplicate elements using set logic.
data=[10,20,20,30,30,40,50,50]
result={}
for i in data:
    if i in result:
        result[i]+=1
    if i not in result:
        result[i]=1
print(result)
for i,val in result.items():
    if val > 1:
        print(f"duplicates are {i}")
        
data = [10,20,20,30,30,40,50,50]

seen = set()
duplicates = set()

for i in data:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates)


# Q14
# Given:
# data=[10,20,30,40]
# data=[10,20,30,40]
# result={}
# for i in data:
#     if i in result:
#         result[i]+=1
#     if i not in result:
#         result[i]=1
# print(result)
# for i,val in result.items():
#     if val == 1:
#         print(f"unique are {i}")
        
data = [10,20,30,40]

if len(data) == len(set(data)):
    print("All elements are unique")
else:
    print("Duplicates exist")



# Q15
# Given:
# s={10,20,30}
# Try adding a list [40,50] into the set. Comment the error.
s={10,20,30}
s.add([40,50])
print(s)
# output:- ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 2, in <module>
# TypeError: unhashable type: 'list'

# Q16
# Add a tuple (40,50) into a set.
s={10,20,30}
s.add((40,50))
print(s)
# output:- {10, (40, 50), 20, 30}

# Q17
# Create a set containing frozensets:
# frozenset({1,2})
# frozenset({3,4})
s = {
    frozenset({1,2}),
    frozenset({3,4})
}

print(s)

# Q18
# Given:
# students={"Sunny","Ravi","Ajay"}
# passed={"Sunny","Ajay"}
# Find students who failed.
students={"Sunny","Ravi","Ajay"}
passed={"Sunny","Ajay"}
# for i in students:
#     if i not in passed:
#         print(f"failed students are {i}")

failed = students - passed
print(failed)
        
    

# Q19
# Given:
# python_students={"Sunny","Ravi","Ajay"}
# java_students={"Ravi","Sonia","Ajay"}
# Find students who know both Python and Java.
python_students={"Sunny","Ravi","Ajay"}
java_students={"Ravi","Sonia","Ajay"}
for i in python_students:
    if i in java_students:
        print(f"students know both languages are {i}")
c=python_students.intersection(java_students)
print(c)


# Q20
# Find students who know only one language.
python_students={"Sunny","Ravi","Ajay"}
java_students={"Ravi","Sonia","Ajay"}
c=python_students.symmetric_difference(java_students)
print(c)
result = set()

for i in python_students:
    if i not in java_students:
        result.add(i)
for i in java_students:
    if i not in python_students:
        result.add(i)

print(result)
    



# PART 2 — Output Prediction

# Q21

# s={x*x for x in range(5)}
# print(s)
# output:- {0,1,4,9,16}

# Q22

# s={x for x in range(10) if x%2==0}
# print(s)
# output:- {0,2,4,6,8}

# Q23
# s=set("banana")
# print(s)
# output:- {'b', 'a', 'n'}

# Q24
# s={1,True,0,False}
# print(s)
# output:- {1,0}


# Q25
# s={10,20,30}
# # print(s[0])
# Predict the error.
# it gives the error because the sets are unorderded , so there any index in sets

# Q26
# s={10,20,30}
# s.add((40,50))
# print(s)
#  output:- {10, (40, 50), 20, 30}

# Q27
# s={10,20,30}
# # s.add([40,50])
# Predict the error.
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 2, in <module>
# TypeError: unhashable type: 'list'

# Q28
# a={1,2,3}
# b={3,4,5}
# print(a-b)
# print(b-a)
#  output:- {1,2}
#  output:- {4,5}


# Q29

# a={1,2,3}
# b={3,4,5}
# print((a|b)-(a&b))
#  output:- {1,2,4,5}
# Q30

# s=frozenset({1,2,3})
# # s.add(4)
# Predict the error.
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 2, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'

# PART 3 — Placement / Interview Questions

# Q31
# Explain why sets are unordered.
# Sets are unordered because they are implemented using a hash table. Elements are stored according to their hash values, not by insertion order, so indexing is not supported.

# Q32
# Explain why sets remove duplicates automatically.
# Sets store only unique hash values. When a duplicate element is added, Python finds that the hash already exists and ignores the duplicate.

# Q33
# Explain why lists cannot be added into sets.
# Lists are mutable, so their hash value can change. Since sets require hashable (immutable) elements, lists cannot be added.

# Q34
# Explain why tuples can be added into sets.
# Tuples are immutable, so they are hashable (if all their elements are hashable). Therefore, tuples can be stored inside sets.

# Q35
# Explain why True and 1 are treated as duplicate-like values in a set.
# True == 1
# returns
# True
# and
# False == 0
# returns
# True
# Therefore
# {1, True}
# becomes
# {1}
# because they have the same value and hash.
# Q36
# Find duplicate elements from a list using only set logic.
data = [10,20,20,30,30,40,50,50]

seen = set()
duplicates = set()
for i in data:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)

# Q37
# Find unique elements from a list.
data = [10,20,20,30,30,40,50,50]
unique = set(data)
print(unique)


# Q38
# Check whether two lists have at least one common element using sets.
a = [1,2,3]
b = [3,4,5]
if set(a).isdisjoint(set(b)):
    print("No Common Elements")
else:
    print("Common Elements Exist")


# Q39
# Check whether one list is fully contained inside another using sets.
a = [1,2]
b = [1,2,3,4]

if set(a).issubset(set(b)):
    print("Contained")
else:
    print("Not Contained")


# Q40
# Find common characters between two strings using sets.
a = "python"
b = "typhoon"

print(set(a) & set(b))

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

# Q41
# Given:

students_all = {"Sunny","Ravi","Ajay","Sonia","Mahesh","Kiran"}

python = {"Sunny","Ajay","Mahesh"}
java = {"Ravi","Ajay","Sonia"}
sql = {"Sunny","Sonia","Kiran"}

# ----------------------------------------------------
# 1. Students who know Python or Java
# ----------------------------------------------------

print("1. Python or Java:")
print(python | java)

# ----------------------------------------------------
# 2. Students who know both Python and Java
# ----------------------------------------------------

print("\n2. Python and Java:")
print(python & java)

# ----------------------------------------------------
# 3. Students who know Python but not Java
# ----------------------------------------------------

print("\n3. Python but not Java:")
print(python - java)

# ----------------------------------------------------
# 4. Students who know Java but not Python
# ----------------------------------------------------

print("\n4. Java but not Python:")
print(java - python)

# ----------------------------------------------------
# 5. Students who know exactly one of Python or Java
# ----------------------------------------------------

print("\n5. Exactly one of Python or Java:")
print(python ^ java)

# ----------------------------------------------------
# 6. Students who know all three languages
# ----------------------------------------------------

print("\n6. Python, Java and SQL:")
print(python & java & sql)

# ----------------------------------------------------
# 7. Students who know none of the three
# ----------------------------------------------------

print("\n7. None of the three:")

skills = python | java | sql

print(students_all - skills)

# ----------------------------------------------------
# 8. Whether all Python students are in students_all
# ----------------------------------------------------

print("\n8. Python is subset of students_all:")
print(python.issubset(students_all))

# ----------------------------------------------------
# 9. Whether students_all is a superset of SQL students
# ----------------------------------------------------

print("\n9. students_all is superset of SQL:")
print(students_all.issuperset(sql))

# ----------------------------------------------------
# 10. Whether Python and SQL are disjoint
# ----------------------------------------------------

print("\n10. Python and SQL are disjoint:")
print(python.isdisjoint(sql))

# ----------------------------------------------------
# 11. Total unique students who know at least one skill
# ----------------------------------------------------

print("\n11. Total unique students with at least one skill:")
print(skills)
print("Total =", len(skills))

# ----------------------------------------------------
# 12. Convert final result to frozenset
# ----------------------------------------------------

print("\n12. Final result as frozenset:")

final = frozenset(skills)

print(final)