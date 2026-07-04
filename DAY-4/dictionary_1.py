# 📘 DICTIONARIES — MODULE 1

# (Creation, Accessing, Updating, Removing, Iteration, Membership, Built-in Functions)
# PART 1 — Coding Questions

# Q1
# Create a dictionary containing:
# {
#     "name":"Sunny",
#     "age":21,
#     "city":"Hyderabad"
# }
# Print the dictionary.
details={"name":"sunny","age":21,"city":"Hyderabad"}
print(details)

# Q2
# Create an empty dictionary.
# Print its type.
d={}
print(type(d))

# Q3
# Create
# student={
# "name":"Sunny",
# "age":21
# }
# Print only the name.
student={"name":"sunny","age":21}
print(student["name"])

# Q4
# Print only the age using indexing.
student={"name":"sunny","age":21}
print(list(student.items())[1])

# Q5
# Create
# student={
# "name":"Sunny",
# "age":21
# }
# Add
# "course":"Python"
# Print the dictionary.
student={
"name":"Sunny",
"age":21
}
student.update({"course":"Python"})
print(student)

# Q6
# Update
# age
# to
# 22
# Print the dictionary.
student={
"name":"Sunny",
"age":21
}
student["age"]=22
print(student)

# Q7
# Remove
# age
# using pop().
# Print the removed value and remaining dictionary.
student={
"name":"Sunny",
"age":21
}
AGE=student.pop("age")
print(AGE)
print(student)

# Q8
# Remove the last inserted item using
# popitem()
students={"name":"sunny","age":20,"college":"N.B.K.R"}
students.popitem()
print(students)

# Q9
# Delete
# name
# using
# del
students={"name":"sunny","age":20,"college":"N.B.K.R"}
del students["name"]
print(students)

# Q10
# Clear the dictionary.
# Print the result.
students={"name":"sunny","age":20,"college":"N.B.K.R"}
students.clear()
print(student)

# Q11
# Copy a dictionary using
# copy()
# Print both dictionaries.
students={"name":"sunny","age":20,"college":"N.B.K.R"}
data=students.copy()
print(data)
print(students)

# Q12
# Check whether
# "name"
# exists using
# in
students={"name":"sunny","age":20,"college":"N.B.K.R"}
for i in students:
    if i == "name":
        print("exists")
        break
else:
    print("not exists")
        

# Q13
# Check whether
# "salary"
# does not exist.
students={"name":"sunny","age":20,"college":"N.B.K.R"}
for i in students:
    if i == "salary":
        print("exists")
        break
else:
    print("not exists")


# Q14
students={"name":"sunny","age":20,"college":"N.B.K.R"}
# Print only all keys using a loop.
for i in students.keys():
    print(i)

# Q15
# Print only all values using a loop.
students={"name":"sunny","age":20,"college":"N.B.K.R"}
for i in students.values:
    print(i)

# Q16
# Print key and value together using
# items()
# Expected output
# name Sunny
# age 21
# city Hyderabad
details={"name":"sunny","age":21,"city":"Hyderabad"}
for i,val in details.items():
    print(i,val)

# Q17
# Print all keys using
# keys()
details={"name":"sunny","age":21,"city":"Hyderabad"}
print(details.keys())
# Q18
# Print all values using
details={"name":"sunny","age":21,"city":"Hyderabad"}
print(details.values())
# values()

# Q19
# Print the length of the dictionary.
details={"name":"sunny","age":21,"city":"Hyderabad"}
print(len(details))

# Q20
# Create
# marks={
# "Math":90,
# "Science":80,
# "English":85
# }
# Find the total marks without using sum().
marks={
"Math":90,
"Science":80,
"English":85
}
total=0
for i,val in marks.items():
    total+=val
print(total)


# Q21
# Find the highest mark without using max().
marks={
"Math":90,
"Science":80,
"English":85
}
highest=0
for i,val in marks.items():
    if val>highest:
        highest=val
print(highest)

# Q22
# Find the lowest mark without using min().
marks={
"Math":90,
"Science":80,
"English":85
}
smallest=list(marks.values())[0]
subject=list(marks.values())[0]
for i,val in marks.items():
    if val<smallest:
        smallest=val
        subject=i
print(subject,smallest)

# Q23

# Search whether
# Science
# exists as a key without using get().
marks={
"Math":90,
"Science":80,
"English":85
}
for i in marks:
    found=False
    if i == "Science":
        found=True
        break
print(found)
        
# Q24
# Count total keys without using len().
marks={
"Math":90,
"Science":80,
"English":85
}
count=0
for i in marks.keys():
    count+=1
print(count)
    

# Q25
# Create a dictionary from two lists.
# keys=["A","B","C"]
# values=[10,20,30]
keys=["A","B","C"]
values=[10,20,30]
d=dict(zip(keys,values))
print(d)

# PART 2 — Output Prediction
# Q26
# d={"A":10,"B":20}
# print(d["A"])
# output:- 
# Q27
# d={}
# print(type(d))
# Q28
# d={"A":10}
# d["B"]=20
# print(d)
# Q29
# d={"A":10,"B":20}
# print(len(d))
# Q30
# d={"A":10}
# print("A" in d)
# Q31
# d={"A":10}
# print("B" not in d)
# Q32
# d={"A":10,"B":20}

# for k in d:
#     print(k)
# Q33
# d={"A":10,"B":20}

# for v in d.values():
#     print(v)
# Q34
# d={"A":10,"B":20}

# for k,v in d.items():
#     print(k,v)
# Q35
# d={"A":10}

# d.update({"B":20})

# print(d)
# PART 3 — Placement Questions
# Q36

# Without using len(), count total keys.

# Q37

# Without using sum(), find the total of all values.

# Q38

# Without using max(), find the maximum value.

# Q39

# Without using min(), find the minimum value.

# Q40

# Explain the difference between:

# []
# get()

# with code.

# Q41

# Explain the difference between:

# pop()
# popitem()
# del

# with examples.

# Q42

# Why must dictionary keys be immutable?

# Explain with an example.

# Q43

# Can a list be used as a dictionary key?

# Show with code and explain the error.

# PART 4 — Google / Amazon Challenge
# Q44

# Given

# student={
# "name":"Sunny",
# "Math":90,
# "Science":80,
# "English":95,
# "Python":100
# }

# Without using:

# sum()
# max()
# min()
# len()

# Find:

# Total marks
# Average
# Highest mark
# Lowest mark
# Total subjects
# Search whether "Python" exists
# Search whether "AI" exists
# Print all subjects
# Print all marks
# Print subject and mark together
# Count iterations
# Q45

# Given

# employees={
# 101:50000,
# 102:65000,
# 103:45000,
# 104:80000,
# 105:70000
# }

# Perform all of the following:

# Print all employee IDs
# Print all salaries
# Print ID and salary together
# Find total salary
# Find average salary
# Find highest salary
# Find lowest salary
# Search whether employee 103 exists
# Search whether employee 110 exists
# Count total employees
# Print employee IDs having salary greater than 60000

