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
print(student.get("salary","not found"))

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
students={
1:{"name":"Sunny","age":21},
2:{"name":"Ravi","age":22}
}

for sid,info in students.items():
    print("ID:",sid)
    for k,v in info.items():
        print(k,v)

# Q15
# Create
# employees=[
# {"id":101,"salary":50000},
# {"id":102,"salary":60000}
# ]
# Print every employee's salary.
employees=[
{"id":101,"salary":50000},
{"id":102,"salary":60000}
]
for i in employees:
    print(i["salary"])
    
# Q16
# Create
# {
# "Math":[90,80,70],
# "Science":[85,75,65]
# }
# Print every mark using nested loops.
marks={
"Math":[90,80,70],
"Science":[85,75,65]
}
for i in marks:
    for j in marks[i]:
        print(j)


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
A={
"A":10,
"B":20,
"C":30
}
reverse={}
for i,values in A.items():
    reverse[values]=i
print(reverse)

# Q18
# Sort a dictionary by keys.
# {
# "C":30,
# "A":10,
# "B":20
# }
A={
"C":30,
"A":10,
"B":20
}
print(dict(sorted(A.items())))

# Q19
# Sort a dictionary by values.
# {
# "A":30,
# "B":10,
# "C":20
# }
A={
"C":30,
"A":10,
"B":20
}
print(dict(sorted(A.items(),key=lambda x:x[1])))

# Q20
# Create
# text="banana"
# Find the frequency of every character using a dictionary.
# Expected
# b ->1
# a ->3
# n ->2
text="banana"
freq={}
for i in text:
    if i in freq:
        freq[i]+=1
    elif i not in freq:
        freq[i]=1
for i,value in freq.items():
    print(f"{i} -> {value}")
    
    
text = "banana is happy i am happy , so everybody is happy"
text = text.replace(",", "")
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
for word, count in freq.items():
    print(f"{word} -> {count}")

# Q21
# Create
# numbers=[10,20,20,30,40,40,40]
# Find the frequency of every number.
numbers=[10,20,20,30,40,40,40]
freq={}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

# Q22
# Merge
# {"A":10}
# and
# {"A":20,"B":30}
# Observe which value remains.
a={"A":10}
b={"A":20,"B":30}
print(a|b)
a.update(b)
print(a)

# Q23
# Create
# student={
# "name":"Sunny",
# "Math":90,
# "Science":80
# }
# Update all marks by adding 5.
student = {
    "name": "Sunny",
    "Math": 90,
    "Science": 80
}

for key, value in student.items():
    if isinstance(value, int):
        student[key] += 5

print(student)

student = {
    "name": "Sunny",
    "Math": 90,
    "Science": 80
}

for key, value in student.items():
    if key != "name":
        student[key] = value + 5

print(student)


# Q24
# Remove every key whose value is less than 50.
# {
# "A":20,
# "B":70,
# "C":40,
# "D":90
# }
b={
"A":20,
"B":70,
"C":40,
"D":90
}
c={}
for i,values in b.items():
    if values>50:
        c[i]=values
print(c)

b = {
    "A": 20,
    "B": 70,
    "C": 40,
    "D": 90
}

for key in list(b.keys()):
    if b[key] < 50:
        del b[key]

print(b)

# Q25
# Create a dictionary from two lists using dictionary comprehension.
# keys=["A","B","C"]
# values=[10,20,30]
keys = ["A","B","C"]
values = [10,20,30]
d = dict(zip(keys, values))
print(d)

keys = ["A","B","C"]
values = [10,20,30]
d = {}
for key, value in zip(keys, values):
    d[key] = value
print(d)

keys = ["A","B","C"]
values = [10,20,30]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)

# PART 2 — Output Prediction
# Q26
# d={"A":10}
# print(d.get("B"))
# output:-
# none

# Q27
# d={"A":10}
# print(d.get("B",0))
# output:-0

# Q28
# d={"A":10}
# d.setdefault("A",20)
# print(d)
# output:-{"A":10}

# Q29
# d={"A":10}
# d.setdefault("B",20)
# print(d)
# output:- {'A':10,'B':20}
# Q30
# print(dict.fromkeys(["A","B"],100))
# output:- {'A':100,'B':100}
# Q31
# print(dict([("A",1),("B",2)]))
# output:- {'A':1,'B':2}
# Q32
# print({x:x*x for x in range(3)})
# output:- {0:0,1:1,2:4}
# Q33
# print({x:x for x in range(5) if x%2==0})
# output:- {0:0,2:2,4:4}
# Q34
# d={"A":10,"B":20}
# print(list(d.items()))
# output:- [('A',10),('B',20)]
# Q35
# d={"A":10}
# d.update({"A":50})
# print(d)
# output:- {'A':50}
# PART 3 — Placement Questions
# Q36
# Explain the difference between:
# get()
# []

d = {"A":10,"B":20}

print(d["A"])          # 10
print(d.get("A"))      # 10

# print(d["C"])        # KeyError
print(d.get("C"))      # None
print(d.get("C",0))    # 0

# [] raises KeyError if key doesn't exist.
# get() returns None (or default value) instead of an error.

# Q37
# Explain the difference between:
# update()
# |

d1={"A":10,"B":20}
d2={"B":50,"C":30}

temp=d1.copy()

temp.update(d2)
print(temp)

print(d1|d2)

# update() modifies the original dictionary.
# | creates a new merged dictionary.

# Q38
# Explain the difference between:
# setdefault()
# update()

d={"A":10}

d.setdefault("B",20)
print(d)

d.setdefault("A",100)
print(d)

d.update({"A":100})
print(d)

# setdefault() adds the key only if it doesn't exist.
# update() always updates or inserts the key.
# Q39
# Reverse a dictionary without using built-in reverse functions.

d={
"A":10,
"B":20,
"C":30
}

reverse={}

for key,value in d.items():
    reverse[value]=key

print(reverse)

# Q40
# Explain why dictionary keys must be unique.
# Show with code.

d={
"A":10,
"A":20,
"B":30
}

print(d)

# Output:
# {'A':20,'B':30}

# Dictionary keys must be unique.
# If the same key appears again, the old value is overwritten.

# Q41
# Sort a dictionary by values in ascending order.

d={
"A":40,
"B":10,
"C":30,
"D":20
}

sorted_dict=dict(sorted(d.items(),key=lambda x:x[1]))

print(sorted_dict)

# Q42
# Find the frequency of every word in:
# "python java python ai java python"

text="python java python ai java python"

freq={}

for word in text.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

for word,count in freq.items():
    print(word,"->",count)
# Q43
# Convert
# {"A":10,"B":20}
# to
# [("A",10),("B",20)]
# using dictionary methods.

d={
"A":10,
"B":20
}

result=list(d.items())

print(result)

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
students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

highest=None
lowest=None
highest_student=""
highest_total=0
iterations=0

found102=False
found110=False

for sid,info in students.items():

    iterations+=1

    total=0
    subjects=0

    print(info["name"])

    if sid==102:
        found102=True

    if sid==110:
        found110=True

    for key,value in info.items():

        iterations+=1

        if key!="name":

            print(key,value)

            total+=value
            subjects+=1

            if highest is None or value>highest:
                highest=value

            if lowest is None or value<lowest:
                lowest=value

    average=total/subjects

    print("Total =",total)
    print("Average =",average)

    if total>highest_total:
        highest_total=total
        highest_student=info["name"]

print("Highest Mark =",highest)
print("Lowest Mark =",lowest)
print("Highest Total Student =",highest_student)
print("102 Exists =",found102)
print("110 Exists =",found110)
print("Iterations =",iterations)
# Q45

# Given

# text = "programming"

# Perform:
# Character frequency
# Highest frequency character
# Lowest frequency character
# Total unique characters
# Print characters in alphabetical order
# Reverse the frequency dictionary
# Print only vowels with frequency
# Print only consonants with frequency

text = "programming"

# Character Frequency
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:")
for ch, count in freq.items():
    print(ch, "->", count)

# Highest Frequency Character
highest_char = ""
highest_freq = 0

for ch, count in freq.items():
    if count > highest_freq:
        highest_freq = count
        highest_char = ch

print("\nHighest Frequency Character:")
print(highest_char, "->", highest_freq)

# Lowest Frequency Character
lowest_char = ""
lowest_freq = None

for ch, count in freq.items():
    if lowest_freq is None or count < lowest_freq:
        lowest_freq = count
        lowest_char = ch

print("\nLowest Frequency Character:")
print(lowest_char, "->", lowest_freq)

# Total Unique Characters
count = 0
for _ in freq:
    count += 1

print("\nTotal Unique Characters:")
print(count)

# Characters in Alphabetical Order
print("\nCharacters in Alphabetical Order:")
for ch in sorted(freq):
    print(ch, "->", freq[ch])

# Reverse Frequency Dictionary
reverse = {}

for ch, count in freq.items():
    if count not in reverse:
        reverse[count] = []
    reverse[count].append(ch)

print("\nReverse Frequency Dictionary:")
print(reverse)

# Vowels Only
print("\nVowels:")
vowels = "aeiou"

for ch, count in freq.items():
    if ch in vowels:
        print(ch, "->", count)

# Consonants Only
print("\nConsonants:")

for ch, count in freq.items():
    if ch not in vowels:
        print(ch, "->", count)