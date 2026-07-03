# TUPLES — MODULE 3
# (Advanced Tuples, Nested Tuples, *args, Functions, Generator Expressions)
# PART 1 — Coding Questions
# Q1

# Create a nested tuple:
# ((10,20),(30,40),(50,60))
# Print every element using nested loops.
t=((10,20),(30,40),(50,60))
for i in t:
    for b in i:
        print(b)

# Q2
# Print only the second inner tuple.
t=((10,20),(30,40),(50,60))
print(t[1])

# Q3
# Print only the value 40 from
# ((10,20),(30,40),(50,60))
t=((10,20),(30,40),(50,60))
print(t[1][1])

# Q4
# Create
# [(10,20),(30,40),(50,60)]
# Print every tuple using a loop.
s=[(10,20),(30,40),(50,60)]
for i in s:
    print(i)
    
# Q5
# Create
# ((10,20),[30,40],(50,60))
# Append 100 to the list and print the tuple.
s=((10,20),[30,40],(50,60))
s[1].append(100)
print(s)

# Q6
# Create a 3×3 matrix using tuples.
# Example
# (
# (1,2,3),
# (4,5,6),
# (7,8,9)
# )
# Print row by row.
matrix=()
for i in range(3):
    row=()
    for j in range(3):
        num=int(input(""))
        row+=(num,)
    matrix+=(row,)
print(matrix)

# Q7
# Print every element of the matrix using nested loops.
matrix=(
(1,2,3),
(4,5,6),
(7,8,9)
)
for i in matrix:
    for j in i:
        print(j)

# Q8
# Find the sum of all elements in the matrix without using sum().
matrix=(
(1,2,3),
(4,5,6),
(7,8,9)
)
total=0
for i in matrix:
    for j in i:
        total+=j
print(total)

# Q9
# Search whether 40 exists without using in.
s=((10,20),[30,40],(50,60))
found=False
for i in s:
    if i==s:
        found = True
        break
print(found)
        

# Q10
# Find the frequency of 20 without using count().
# (10,20,30,20,40,20)
t=(10,20,30,20,40,20)
count=0
for i in t:
    count+=1
print(count)


# Q11
# Find the frequency of every element.
# Example output
# 10 -> 1
# 20 -> 3
# 30 -> 1
# 40 -> 1
t=(10,20,30,20,40,20)
freq={}
for i in t:
    if i in freq:
        freq[i]+=1
    elif i not in freq:
        freq[i]=1
for k,v in freq.items():
    print(f"{k} -> {v}")

# Q12
# Create a tuple of squares from 1 to 10 using a generator expression.
t=tuple(x**2 for x in range(1,11))
print(t)
# Example
# tuple(x*x for x in range(1,11))

# Q13
# Create a tuple containing only even numbers from 1 to 20.
t=tuple()
for i in range(1,21):
    if i%2==0:
        t+=(i,)
print(t)
# Q14
# Create a tuple containing only odd numbers from 1 to 20.
t=tuple()
for i in range(1,21):
    if i%2==0:
        t+=(i,)
print(t)

# Q15

# Create a function
# def add(a,b):
# Return both
# Sum
# Product
# using a tuple.
def add(a,b):
    return a+b,a*b
b=add(1,2)
print(b)


# Q16
# Call the above function and unpack the returned values.
def add(a,b):
    return a+b,a*b
b=add(1,2)
addition,multiply=b
print(addition)
print(multiply)



# PART 2 — Output Prediction
# Q21
# a=((1,2),(3,4))
# print(a[1][0])
# output:- 3
# Q22
# a=((10,20),(30,40))
# for row in a:
#     print(row)
# output:- (10,20)
# (3,4)
# Q23
# a=(x*x for x in range(3))
# print(tuple(a))
# output:- (0,1,4)
# Q24
# def fun():
#     return 10,20

# a,b=fun()
# print(a,b)
# output:- (10,20)
# Q25
# def fun(*x):
#     print(len(x))

# fun(10,20,30)
# output:- 3
# Q26
# def fun(*x):
#     print(x)

# fun(5)
# output:- 5
# Q27
# a=((1,2),(3,4))
# print(len(a))
# output:-2
# Q28
# a=((1,2),(3,4))
# print(a[-1][-1])
# output:-4
# Q29
# a=tuple(x for x in range(5))
# print(a)
# output:-(0,1,2,3,4)
# Q30
# def fun():
#     return ("Python","Java")
# print(fun())
# output:-('Python', 'Java')
# PART 3 — Placement / Interview Questions
# Q31
# Explain the difference between
# (x*x for x in range(5))
# and
# tuple(x*x for x in range(5))
# output:- here ist expressin is generator expression where it prints one value a time where it generator object by printing(next()) and by converting it into tuple it gives the all values at a time 
# Q32

# Explain why this works:
# t=((10,20),[30,40])
# t[1].append(50)
t=((10,20),[30,40])
t[1].append(50)
print(t)
# here because the first inner is the list where appending a list is possible so it is added here list is a mutable

# Q33
# Can a tuple be used as a dictionary key?
# Show with code.

# Q34

# Can a tuple containing a list be used as a dictionary key?
# Explain with code.

# Q35

# Find the largest element from a nested tuple.

# Q36

# Find the smallest element from a nested tuple.

# Q37

# Find the sum of all elements in a nested tuple.

# Q38

# Flatten

# ((1,2),(3,4),(5,6))

# into

# (1,2,3,4,5,6)
# Q39

# Using *args, find

# Sum
# Average

# without using sum().

# Q40

# Write a function that returns three values.

# Receive them using multiple assignment.

# PART 4 — Google / Amazon Challenge
# Q41

# Given

# matrix = (
#     (10,20,30),
#     (40,50,60),
#     (70,80,90)
# )

# Without using

# sum()
# max()
# min()

# perform all of the following:

# Print every row.
# Print every element.
# Find total sum.
# Find average.
# Find largest element.
# Find smallest element.
# Count even numbers.
# Count odd numbers.
# Search whether 50 exists.
# Find the frequency of every element.
# Flatten the matrix into one tuple.
# Create a tuple of squares using a generator expression.
# Create a function using *args to calculate the total of the flattened tuple.
# Return the largest and smallest values from a function and unpack them.
# Print the total number of iterations performed.

# This completes Tuple Module 3. After this, your tuple preparation will be placement-ready, and we'll move on to Sets.