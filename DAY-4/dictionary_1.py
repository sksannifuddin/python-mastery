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
print(student["age"])

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
print(students)

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
for i in students.values():
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
highest=list(marks.values())[0]
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
found=False
for i in marks:
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
# output:- 10
# Q27
# d={}
# print(type(d))
# output:- <class 'dict'>
# Q28
# d={"A":10}
# d["B"]=20
# print(d)
# output:- {'A': 10, 'B': 20}
# Q29
# d={"A":10,"B":20}
# print(len(d))
# output:- 2
# Q30
# d={"A":10}
# print("A" in d)
# output:- True
# Q31
# d={"A":10}
# print("B" not in d)
# output:- True
# Q32
# d={"A":10,"B":20}
# for k in d:
#     print(k)
# output:- A,B
# Q33
# d={"A":10,"B":20}
# for v in d.values():
#     print(v)
# output:- 10,20
# Q34
# d={"A":10,"B":20}
# for k,v in d.items():
#     print(k,v)
# output:- A 10 ,B 20

# Q35
# d={"A":10}
# d.update({"B":20})
# print(d)
# output:- {"A":10,"B":20}

# PART 3 — Placement Questions
# Q36
# Without using len(), count total keys.
# Q36
# Without using len(), count total keys.
d={"A":10,"B":20,"C":30}

count=0
for key in d:
    count+=1

print(count)

# Q37
# Without using sum(), find the total of all values.
d={"A":10,"B":20,"C":30}

total=0
for value in d.values():
    total+=value

print(total)

# Q38
# Without using max(), find the maximum value.
d={"A":10,"B":20,"C":30}

maximum=list(d.values())[0]

for value in d.values():
    if value>maximum:
        maximum=value

print(maximum)

# Q39
# Without using min(), find the minimum value.
d={"A":10,"B":20,"C":30}

minimum=list(d.values())[0]

for value in d.values():
    if value<minimum:
        minimum=value

print(minimum)

# Q40
# Explain the difference between:
# []
# get()
# with code.

d={"A":10,"B":20}

print(d["A"])
print(d.get("A"))

# print(d["C"])      # KeyError
print(d.get("C"))    # None
print(d.get("C",0))  # 0



# Q41
# Explain the difference between:
# pop()
# popitem()
# del
# with examples.

d={"A":10,"B":20,"C":30}

x=d.pop("B")
print(x)
print(d)

item=d.popitem()
print(item)
print(d)

del d["A"]
print(d)

# Q42
# Why must dictionary keys be immutable?
# Explain with an example.

# Dictionary keys must be immutable because Python uses their hash value
# to store and find data. If a key changes, its hash changes, so Python
# cannot locate the value correctly.

d={(10,20):"Tuple key"}
print(d)

# Q43
# Can a list be used as a dictionary key?
# Show with code and explain the error.

# Lists cannot be dictionary keys because lists are mutable and unhashable.

# d={[10,20]:"List key"}
# TypeError: unhashable type: 'list'

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
# Q44

student = {
    "name": "Sunny",
    "Math": 90,
    "Science": 80,
    "English": 95,
    "Python": 100
}

total = 0
highest = student["Math"]
lowest = student["Math"]
subject_count = 0
iterations = 0
python_found = False
ai_found = False

for key, value in student.items():
    iterations += 1

    if key == "Python":
        python_found = True

    if key == "AI":
        ai_found = True

    if isinstance(value, int):
        total += value
        subject_count += 1

        if value > highest:
            highest = value

        if value < lowest:
            lowest = value

average = total / subject_count

print("Total Marks:", total)
print("Average:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Total Subjects:", subject_count)

print("Python Exists:", python_found)
print("AI Exists:", ai_found)

print("\nSubjects:")
for key in student.keys():
    print(key)

print("\nMarks:")
for value in student.values():
    print(value)

print("\nSubject and Mark:")
for key, value in student.items():
    print(key, value)

print("\nIterations:", iterations)

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

# Q45
employees={
101:50000,
102:65000,
103:45000,
104:80000,
105:70000
}

total=0
count=0
highest=list(employees.values())[0]
lowest=list(employees.values())[0]
found_103=False
found_110=False

for emp_id,salary in employees.items():
    print(emp_id)
    print(salary)
    print(emp_id,salary)

    total+=salary
    count+=1

    if salary>highest:
        highest=salary

    if salary<lowest:
        lowest=salary

    if emp_id==103:
        found_103=True

    if emp_id==110:
        found_110=True

    if salary>60000:
        print("Salary greater than 60000:", emp_id)

average=total/count

print("Total Salary:", total)
print("Average Salary:", average)
print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("103 Exists:", found_103)
print("110 Exists:", found_110)
print("Total Employees:", count)