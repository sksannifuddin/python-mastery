# 📘 DICTIONARIES — MODULE 3
# (Nested Dictionaries, Matrix using Dictionaries, Grouping Data, Dictionary Tricks)
# PART 1 — Coding Questions (With Answers)
# Q1
# Given

# students={
# 101:{"name":"Sunny","Math":90,"Science":80},
# 102:{"name":"Ravi","Math":75,"Science":95},
# 103:{"name":"Ajay","Math":88,"Science":91}
# }

# Print every student's complete details.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

for sid,info in students.items():
    print("ID:",sid)
    for key,value in info.items():
        print(key,value)
# Q2
# Print only all student names.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

for sid,info in students.items():
    print(info["name"])
# Q3
# Print only all Math marks.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

for sid,info in students.items():
    print(info["Math"])
# Q4
# Print the names of students whose Science marks are greater than 90.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

for sid,info in students.items():
    if info["Science"]>90:
        print(info["name"])
# Q5
# Find the total marks of each student.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

for sid,info in students.items():
    total=0

    for key,value in info.items():
        if isinstance(value,int):
            total+=value

    print(info["name"],total)
# Q6
# Find the average marks of each student.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

for sid,info in students.items():

    total=0
    count=0

    for key,value in info.items():
        if isinstance(value,int):
            total+=value
            count+=1

    print(info["name"],total/count)
# Q7
# Find the overall highest mark.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

highest=None

for sid,info in students.items():

    for key,value in info.items():

        if isinstance(value,int):

            if highest is None or value>highest:
                highest=value

print(highest)
# Q8
# Find the overall lowest mark.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

lowest=None

for sid,info in students.items():

    for key,value in info.items():

        if isinstance(value,int):

            if lowest is None or value<lowest:
                lowest=value

print(lowest)
# Q9
# Find the student having the highest total marks.

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

highest_total=0
top_student=""

for sid,info in students.items():

    total=0

    for key,value in info.items():

        if isinstance(value,int):
            total+=value

    if total>highest_total:
        highest_total=total
        top_student=info["name"]

print(top_student,highest_total)
# Q10
# Search whether student ID 102 exists without using "in".

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

found=False

for sid in students:

    if sid==102:
        found=True
        break

print(found)
# Q11
# Search whether student ID 110 exists without using "in".

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

found=False

for sid in students:

    if sid==110:
        found=True
        break

print(found)
# Q12
# Create a 3×3 matrix using dictionaries and print every row.

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

for row in matrix.values():
    print(row)
# Q13
# Print every element of the matrix.

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

for row in matrix.values():

    for value in row.values():
        print(value)
# Q14
# Find the sum of all matrix elements.

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

total=0

for row in matrix.values():

    for value in row.values():
        total+=value

print(total)
# Q15
# Find the largest element in the matrix.

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

largest=None

for row in matrix.values():

    for value in row.values():

        if largest is None or value>largest:
            largest=value

print(largest)

# Q16
# Find the smallest element in the matrix.

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

smallest=None

for row in matrix.values():

    for value in row.values():

        if smallest is None or value<smallest:
            smallest=value

print(smallest)
# Q17
# Find the average of all elements in the matrix.

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

total=0
count=0

for row in matrix.values():

    for value in row.values():
        total+=value
        count+=1

print(total/count)
# Q18
# Search whether 8 exists in the matrix without using "in".

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

found=False

for row in matrix.values():

    for value in row.values():

        if value==8:
            found=True
            break

print(found)
# Q19
# Count total elements in the matrix.

matrix={
0:{0:1,1:2,2:3},
1:{0:4,1:5,2:6},
2:{0:7,1:8,2:9}
}

count=0

for row in matrix.values():

    for value in row.values():
        count+=1

print(count)
# Q20
# Group names according to their first letter.

names=["Sunny","Sonia","Ajay","Anil","Ravi","Ramesh"]

group={}

for name in names:

    first=name[0]

    if first not in group:
        group[first]=[]

    group[first].append(name)

print(group)
# Q21
# Create a dictionary using zip().

keys=["A","B","C"]
values=[10,20,30]

d=dict(zip(keys,values))

print(d)
# Q22
# Print index and key using enumerate().

d={
"A":10,
"B":20,
"C":30
}

for index,key in enumerate(d):
    print(index,key)
# Q23
# Print index, key and value together.

d={
"A":10,
"B":20,
"C":30
}

for index,(key,value) in enumerate(d.items()):
    print(index,key,value)
# Q24
# Merge two dictionaries using dictionary unpacking (**).

d1={
"A":10,
"B":20
}

d2={
"C":30,
"D":40
}

d={
**d1,
**d2
}

print(d)
# Q25
# Merge dictionaries having common keys.

d1={
"A":10,
"B":20
}

d2={
"B":100,
"C":30
}

d={
**d1,
**d2
}

print(d)
# Q26
# Create a lookup dictionary for grades.

grades={
90:"A",
80:"B",
70:"C",
60:"D"
}

print(grades)
# Q27
# Search a value from the lookup dictionary.

grades={
90:"A",
80:"B",
70:"C",
60:"D"
}

print(grades[90])
# Q28
# Reverse a lookup dictionary.

grades={
90:"A",
80:"B",
70:"C",
60:"D"
}

reverse={}

for key,value in grades.items():
    reverse[value]=key

print(reverse)
# Q29
# Count vowels using a dictionary.

text="programming"

freq={}

for ch in text:

    if ch in "aeiou":

        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

print(freq)
# Q30
# Count consonants using a dictionary.

text="programming"

freq={}

for ch in text:

    if ch.isalpha() and ch not in "aeiou":

        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

print(freq)

# Q31
# Explain the difference between get() and [] with code.

d={"A":10,"B":20}

print(d["A"])          # 10
print(d.get("A"))      # 10

# print(d["C"])        # KeyError
print(d.get("C"))      # None
print(d.get("C",0))    # 0

# [] raises KeyError if key is absent.
# get() returns None or a default value.
# Q32
# Explain the difference between update() and | with code.

d1={"A":10,"B":20}
d2={"B":50,"C":30}

# update() modifies original dictionary
x=d1.copy()
x.update(d2)
print(x)

# | creates a new dictionary
print(d1 | d2)

# update() changes original dictionary.
# | returns a new merged dictionary.
# Q33
# Explain dictionary unpacking (**)

d1={"A":10}
d2={"B":20}

d={
    **d1,
    **d2
}

print(d)

# Output:
# {'A':10,'B':20}
# Q34
# Explain why dictionary keys must be immutable.

d={
    (10,20):"Tuple Key"
}

print(d)

# Tuple works because it is immutable.

# d={[10,20]:"List Key"}
# TypeError: unhashable type: 'list'

# Mutable objects cannot be dictionary keys.
# Q35
# Explain dictionary comprehension with example.

square={x:x*x for x in range(1,6)}

print(square)
# Q36
# Explain word frequency using dictionaries.

text="python java python ai java python"

freq={}

for word in text.split():

    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

print(freq)
# Q37
# Explain character frequency using dictionaries.

text="banana"

freq={}

for ch in text:

    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)
# Q38
# Explain grouping using dictionaries.

names=["Sunny","Sonia","Ajay","Anil","Ravi"]

group={}

for name in names:

    first=name[0]

    if first not in group:
        group[first]=[]

    group[first].append(name)

print(group)
# 📘 PART 3 — Google / Amazon Challenge
# Q39
# Given

students={
101:{"name":"Sunny","Math":90,"Science":80},
102:{"name":"Ravi","Math":75,"Science":95},
103:{"name":"Ajay","Math":88,"Science":91}
}

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

highest=None
lowest=None
highest_total=0
highest_student=""
iterations=0

for sid,data in students.items():

    total=0
    subjects=0

    print("Name:",data["name"])

    for key,value in data.items():

        iterations+=1

        if isinstance(value,int):

            total+=value
            subjects+=1

            if highest is None or value>highest:
                highest=value

            if lowest is None or value<lowest:
                lowest=value

            print(key,value)

    average=total/subjects

    print("Total =",total)
    print("Average =",average)

    if total>highest_total:
        highest_total=total
        highest_student=data["name"]

print("Highest Mark =",highest)
print("Lowest Mark =",lowest)
print("Highest Total Student =",highest_student)

print("102 Exists =",102 in students)
print("110 Exists =",110 in students)

print("Iterations =",iterations)
# Q40
# Find frequency of every word.

text="python java python ai java python"

freq={}

for word in text.split():

    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

print(freq)
# Q41
# Reverse a dictionary.

d={
"A":10,
"B":20,
"C":30
}

reverse={}

for key,value in d.items():
    reverse[value]=key

print(reverse)
# Q42
# Merge three dictionaries using **

d1={"A":10}
d2={"B":20}
d3={"C":30}

d={
**d1,
**d2,
**d3
}

print(d)
# Q43
# Create dictionary using zip().

keys=["A","B","C"]
values=[10,20,30]

d=dict(zip(keys,values))

print(d)
# Q44
# Sort dictionary by values.

d={
"A":30,
"B":10,
"C":20
}

print(dict(sorted(d.items(),key=lambda x:x[1])))
# Q45
# Character frequency of "programming"

text="programming"

freq={}

for ch in text:

    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)

