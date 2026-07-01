# PART-1 : Nested Lists / Matrices (20 Questions)
# Q1

# Create the following matrix and print it.

# [
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
# ]
matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        num=int(input())
        row.append(num)
    matrix.append(row)
print(matrix)    

# Q2

# Print the first row.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])
# Q3

# Print the last row.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[-1])
# Q4

# Print the element 5.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][1])

# Q5

# Print the element 9.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[2][2])
# Q6

# Change 5 into 50.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix[1][1]=50
print(matrix)

# Print the matrix.


# Q7

# Print every element using nested loops.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    for j in i:
        print(j)
    
# Q8
# Print every row separately.
# Example
# 1 2 3
# 4 5 6
# 7 8 9
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print(*row)
# Q9

# Print only the first column.

# Output

# 1
# 4
# 7
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    print(matrix[i][0])
    
for row in matrix:
    print(row[0])

# Q10
# Print only the second column.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    print(matrix[i][1])
    
for row in matrix:
    print(row[1])
# Q11

# Print the main diagonal.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    print(matrix[i][i])


# Output

# 1
# 5
# 9

# Q12
# Print the secondary diagonal.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
for i in range(n):
    print(matrix[i][n-1-i])
# Output
# 3
# 5
# 7

# Q13
# Find the sum of every row.
# Example
# Row1 = 6
# Row2 = 15
# Row3 = 24
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    total=0
    for j in range(len(matrix)):
        total+=matrix[i][j]
    print(f"Row{i+1} = {total} ")
    
for i in range(len(matrix)):
        print(f"Row{i+1} = {sum(matrix[i])}")
        
for i,row in enumerate(matrix,start=1):
    print(f"Row{i} = {sum(row)}")
# Q14

# Find the sum of every column.
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
        total=0
        for j in range(3):
            total+=matrix[j][i]
        print(f"Column{i+1} = {total}") 
        
for i in range(3):
    print(f"Column{i+1} = {sum([matrix[j][i] for j in range(3)])}")

# Q15

# Create a 4×4 matrix using list comprehension.

# Initially every value should be 0.
matrix=[[i*0 for i in range(4)] for j in range(4)]
print(matrix) 
# Q16

# Create this matrix using list comprehension.
matrix=[]

for i in range(3):
    row=[]
    for j in range(3):
        row.append(j+1)
    matrix.append(row)
    
matrix=[]
for i in range(3):
    row=[]
    for j in range(1,4):
        num=j*1
        row.append(num)
    matrix.append(row)
print(matrix) 

matrix=[[i*1 for i in range(1,4)]for j in range(3)]
print(matrix) 
# 1 2 3
# 1 2 3
# 1 2 3
# Q17

# Create
matrix=[[i*1 for i in range(3)]for j in range(3)]
print(matrix) 

matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        num=j*1
        row.append(num)
    matrix.append(row)
print(matrix) 
# 0 1 2
# 0 1 2
# 0 1 2

# using list comprehension.

# Q18
# Count how many elements are present in a matrix without using len().
matrix=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for i in matrix:
    for j in i:
        count+=1
print(count)

# Q19

# Find the largest element in the matrix without max().
matrix=[[1,2,3],[4,5,6],[7,8,9]]
largest=matrix[0][0]
for i in matrix:
    for j in i:
        if j>largest:
            largest=j
print(largest)


matrix = [[1,2,3],[4,5,6],[7,8,9]]

great = matrix[0][0]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > great:
            great = matrix[i][j]
print(great)

# Q20 ⭐

# Find

# Largest
# Smallest
# Sum

# of the matrix using one traversal only.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
smallest=matrix[0][0]
largest=matrix[0][0]
total=0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        total+=matrix[i][j]
        if matrix[i][j]>largest:
            largest=matrix[i][j]
        elif matrix[i][j]<smallest:
            smallest=matrix[i][j]
print(smallest)
print(largest)
print(total)


# PART-2 : Copying & Aliasing (10 Questions)
# Q21
# a=[10,20,30]
# b=a
# Append 40 to b.
# Print both lists.
a=[10,20,30]
b=a
b.append(40)
print(a)
print(b)

# Q22
# Predict the output.

# a=[1,2]
# b=a
# print(a is b):- True
# Q23

# Predict the output.

# a=[1,2]
# b=a.copy()
# print(a is b)
# False
# Q24

# Predict the output.

# a=[1,2]
# b=a.copy()
# print(a==b) True
# Q25

# Create a list.
# Make a copy.
# Append a value only to the copied list.
# Print both lists.
a=[10,20,30]
b=a.copy()
b.append(40)
print(a)
print(b)

# Q26
# Predict.
# a=[[1,2],[3,4]]
# b=a.copy()
# b[0][0]=100
# print(a):-[[100,2],[3,4]]

# Q27
# Create
import copy

a=[[10],[20],[30]]

b=copy.deepcopy(a)

b[0][0]=100

print(a)
print(b)
# Create another independent copy.

# Modify the copy.

# Verify whether the original changed.

# Q28

# Print the memory addresses of

print(id(a))
print(id(b))

# using id().

# Q29

# Explain the difference between

# ==
# where ""=="" is used for the comparison between the objects with their values , where is used where it check the memeory addresses 
# and

# is
a=[30,40]
b=a.copy()
print(a==b)
print(a is b)
#here check the difference between them
# using code.

# Q30 ⭐

# Predict the output.

# a=[1,2,3]

# b=a

# c=a.copy()

# print(a is b) True

# print(a is c) False

# print(a==c) True

# PART-3 : Advanced List Comprehension (20 Questions)
# Q31

# Create

# [2,4,6,8,...,100]
even=[x for x in range(1,101) if x%2==0]
print(even)
# using list comprehension.

# Q32

# Create

# [1,8,27,...]
cube=[x**3 for x in range(1,21)]
print(cube)
# (cubes from 1–20)

# Q33

# Given

numbers=[10,15,20,25,30]
largest=[]
for num in numbers:
    if num>20:
        largest.append(num)
print(largest)

# Create another list containing only numbers greater than 20.

# Q34

# Create

# ["EVEN","ODD","EVEN"...]

# from

numbers=[1,2,3,4,5]
ev_od=[]
for i in numbers:
    if i%2==0:
        ev_od.append("EVEN")
    else:
        ev_od.append("ODD")
print(ev_od)

ev_od=[ "EVEN" if i%2==0 else "ODD" for i in numbers]
print(ev_od)
        
# Q35

# Convert

# ["python","java","go"]
# into
# ["Python","Java","Go"]
pro=["python","java","go"]
pro1=[]
for i in pro:
    pro1.append(i.capitalize())
print(pro1)

# Q36

# Remove all vowels.
# Example
# Python
# ↓
# Pythn
# using list comprehension.
vowels="Aeiou"
s=["PYTHON"]
result=[]
for i in s:
    new_word=""
    for j in i:
        if j.lower() not in vowels:
            new_word+=j
    result.append(new_word)
print(result)

vowels="Aeiou"
s="PYTHON"
result="".join([j for j in s if j.lower() not in vowels])
print(result)


# Q37
# Given
# names=["Ajay","Sunny","Aman","Ravi"]

# Create another list containing only names starting with A.
names=["Ajay","Sunny","Aman","Ravi"]
names1=[]
for i in names:
        if i[0] =="A":
            names1.append(i)
        
print(names1)


names = ["Ajay", "Sunny", "Aman", "Ravi"]

names1 = []

for name in names:
    if name.startswith("A"):
        names1.append(name)

print(names1)
        
names = ["Ajay", "Sunny", "Aman", "Ravi"]
names1=[i for i in names if i[0]=="A"]
print(names1)


# Q38
# Given
# numbers=[-5,-2,0,4,-8,7]
# Create another list containing only positive numbers.
numbers=[-5,-2,0,4,-8,7]
result=[]
for i in numbers:
    if i>0:
        result.append(i)
print(result)

result=[i for i in numbers if i>0]
print(result)
# Q39


# Create

# [-1,-2,-3,-4,-5]
numbers=[]
for i in range(-1,-6,-1):
    numbers.append(i)
print(numbers)

numbers=[i for i in range(-1,-6,-1)]
print(numbers)
# using list comprehension.

# Q40

# Create
# [100,99,98,...,1]

# using list comprehension.
numbers=[]
for i in range(100,0,-1):
    numbers.append(i)
print(numbers)

numbers=[ i for i in range(100,0,-1)]
print(numbers)  
# Q41

# Flatten

# [[1,2],[3,4],[5,6]]

# into

# [1,2,3,4,5,6]
flat=[[1,2],[3,4],[5,6]]
result=[]
for i in flat:
    for j in i:
        result.append(j)
print(result)

result=[j for i in flat for j in i]
print(result)

# Q42

# Create

# [[0,0],[0,0]]

# using list comprehension.
[[0,0],[0,0]]
matrix=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(0)
    matrix.append(row)
print(matrix)

matrix=[[0 for i in range(2)]for j in range(2)]
print(matrix)
# Q43

# Create

# [[1,2],[3,4],[5,6]]

# using list comprehension only.
[[1,2],[3,4],[5,6]]
matrix=[]
num=1
for i in range(3):
    row=[]
    for j in range(2):
        row.append(num)
        num+=1
    matrix.append(row)
print( matrix)


matrix=[[i*2+j+1 for j in range(2)] for i in range(3)]
print( matrix)
# Q44

# Create a multiplication table of 5 using list comprehension.

# Output

# 5
# 10
# 15
# ...
# 50
n=5
for i in range(1,11):
    print(n*i)
    
table=[n*i for i in range(1,11)]
for i in table:
    print(i)
    
    
# Q45
# Given
# ["apple","banana","mango"]
# Convert every word into uppercase.
s=["apple","banana","mango"]
result=[]
for i in s:
    result.append(i.upper())
print(result)


# Q46
# Given
# numbers=[12,15,18,21,24]
# Create another list containing numbers divisible by both 2 and 3.
numbers=[12,15,18,21,24]
result=[]
for i in numbers:
    if i%2==0 and i%3==0:
        result.append(i)
print(result)
        
result=[i for i in numbers if i%2==0 and i%3==0]
print(result)


# Q47
# Create
# [False,True,False,True]
# for
# numbers=[1,2,3,4]
# where each element indicates whether the number is even.
numbers=[1,2,3,4]
result=[]
for i in numbers:
    if i%2==0:
        result.append(True)
    else:
        result.append(False)
print(result)


# Q48
# Create
# [10,20,30]
# from
# ["10","20","30"]
# using list comprehension.

n=["10","20","30"]
s=[]
for i in n:
    s.append(int(i))
print(s)

s=[int(i) for i in n]
print(s)

# Q49

# Create a 3×3 identity matrix using list comprehension.
# Output:
# 1 0 0
# 0 1 0
# 0 0 1
matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
for i in matrix:
    print(*i)
    
matrix=[[1 if i == j else 0 for j in range(3)] for i in range(3)]
for i in matrix:
    print(*i)

# Q50 ⭐ (Final Challenge)

# Given

# matrix=[
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
matrix=[]
num=10
for i in range(3):
    row=[]
    for j in range(3):
        row.append(num)
        num+=10
    matrix.append(row)
print(matrix)

# Find the largest element
# Find the smallest element
# Find the total sum
# Find the average
# Flatten the matrix into a single list
# Create another list containing only values greater than 40 using list comprehension

matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

greatest = matrix[0][0]
smallest = matrix[0][0]
total = 0
count = 0

for row in matrix:
    for value in row:
        if value > greatest:
            greatest = value

        if value < smallest:
            smallest = value

        total += value
        count += 1

average = total / count

print("Largest:", greatest)
print("Smallest:", smallest)
print("Total:", total)
print("Average:", average)

flat = [value for row in matrix for value in row]
print("Flattened Matrix:", flat)

greater_than_40 = [value for row in matrix for value in row if value > 40]
print("Values Greater Than 40:", greater_than_40)