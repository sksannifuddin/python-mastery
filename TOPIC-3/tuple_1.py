# TUPLES — MODULE 1
# (Creation, Packing, Unpacking, Indexing, Slicing, Membership, Iteration, len(), count(), index())
# PART-1 : Coding Questions
# Q1
# Create a tuple containing:
# 10,20,30,40,50
# Print the tuple.
numbers=(10,20,30,40,50)
print(numbers)

# Q2

# Create an empty tuple.
# Print its type.
num=()
print(type(num))
num=tuple()
print(type(num))

# Q3

# Create a tuple containing only one element:
number=(100,)
print(type(number))
# 100
# Print the tuple and its type.


# Q4
# Create a tuple containing different data types:
# 10
# "Python"
# 3.14
# True
data=(10,3.14,"Python",True)
print(data)
# Print the tuple.

# Q5

# Create a nested tuple.

# ((1,2),(3,4),(5,6))
numbers=((1,2),(3,4),(5,6))
print(numbers)
# Print it.

# Q6

# Using tuple packing, create
numbers=10,20,30
print(numbers)
# 10,20,30
# without using parentheses.
# Print the tuple.

# Q7
# Unpack the tuple
# (100,200,300)
# into variables
# a,b,c
# Print all three variables.
numbers=(100,200,300)
a,b,c=numbers
print(a)
print(b)
print(c)

# Q8
# Swap two variables using tuple unpacking.
# Example:
# a=10
# b=20
# After swapping
# a=20
# b=10
num=(10,20)
a,b=num
print(a,b)
b,a=a,b
print(a,b)


# Q9
# Create
# ("Python","Java","C++","Go")
# Print the first element.
lang=("Python","Java","C++","Go")
print(lang[0])

# Q10
# Print the last element using negative indexing.
lang=("Python","Java","C++","Go")
print(lang[-1])

# Q11
# Print the second last element.
lang=("Python","Java","C++","Go")
print(lang[-2])



# Q12

# Print elements from index 1 to 3 using slicing.
lang=("Python","Java","C++","Go")
print(lang[1:3])

# Q13
# Print every alternate element using slicing.
lang=("Python","Java","C++","Go")
print(lang[::2])

# Q14

# Reverse the tuple using slicing.
lang=("Python","Java","C++","Go")
print(lang[::-1])

# Q15
# Check whether
# "Python"
# exists in
# ("Java","Python","Go")
l=("Java","Python","Go")
if "Python" in l:
    print("Exists")
else:
    print("Not Exists")

# Q16
# Check whether
# "C"
# does NOT exist.
l = ("Java", "Python", "Go")

if "C" not in l:
    print("C does not exist")
else:
    print("C exists")
    
    
# Q17

# Find the length of
n=(10,20,30,40,50)
print(len(n))
# (10,20,30,40,50)

# Q18

# Print every element using a for loop.
n=(10,20,30,40,50)
for i in n:
    print(i)
    
# Q19
# Print index and value using enumerate().
# Expected format:
# 0 10
# 1 20
# 2 30
# ...
n=(10,20,30,40,50)
for index,value in enumerate(n):
    print(index, value)

# Q20
# Given
# (10,20,20,30,20,40)
# Find how many times
# 20
# appears.
n=(10,20,20,30,20,40)
count=0
for i in n:
    if i == 20:
        count+=1
print(count)

print(n.count(20))

# Q21
# Given
# ("A","B","C","B","D")
# Find the index of the first "B".
n=("A","B","C","B","D")
print(n.index("B"))

# Q22
# Given
# (5,10,15,20,25)
# Print only the even numbers using a loop.
n=(5,10,15,20,25)
for i in n:
    if i%2==0:
        print(i)

# Q23
# Given
# (1,2,3,4,5)
# Find the sum without using sum().
n=(1,2,3,4,5)
total=0
for i in n:
    total+=i
print(total)


# Q24
# Given
# (10,20,30,40)
# Find the largest element without using max().
n=(10,20,30,40)
largest=n[0]
for i in n:
    if i>largest:
        largest=i
print(largest)

# Q25
# Given
# (10,20,30,40)
# Find the smallest element without using min().
n=(10,20,30,40)
smallest=n[0]
for i in n:
    if i<smallest:
        smallest=i
print(smallest)

# PART-2 : Output Prediction
# Q26
# a=(10,20,30)
# print(a[1])
# output:- 20
# Q27
# a=(1,2,3)
# print(a[-1])
# output:- 3
# Q28
# a=(10,20,30,40)
# print(a[1:3])
# output:-20,30
# Q29
# a=(10,20,30)
# print(len(a))
# output:- 3
# Q30
# a=(1,2,2,3)
# print(a.count(2))
# output:- 2
# Q31
# a=("Python","Java","C")
# print(a.index("Java"))
# output:- 1
# Q32
# a=(1,2,3,4)
# print(a[::-1])
# output:- 4,3,2,1
# Q33
# a=(10,)
# print(type(a))
# output:- <class 'tuple'>
# Q34
# a=(10)
# print(type(a))
# output:- <class 'int'>
# Q35
# a=(10,20,30)
# for x in a:
#     print(x)
#  output:- 10 
# 20
# 30
# PART-3 : FAANG / Placement Questions

# Q36
# Without using len(), count the number of elements in a tuple.
s=(10,20,30,40,50,60)
count=0
for i in s:
    count+=1
print(count)
    

# Q37
# Without using max(), find the largest element.
n=(10,20,30,40)
largest=n[0]
for i in n:
    if i>largest:
        largest=i
print(largest)


# Q38
# Without using min(), find the smallest element.
n=(10,20,30,40)
smallest=n[0]
for i in n:
    if i<smallest:
        smallest=i
print(smallest)


# Q39
# Without using count(), find the frequency of 20.
n=(10,20,30,40,20,20,20,20)
freq=0
for i in n:
    if i == 20:
        freq+=1
print(freq)


# Q40
# Without using the in operator, search whether 50 exists in a tuple.
n=(10,20,30,40,50,50,50)
for i in n:
    if i == 50:
        print("Exists")
        break
else:
    print("Not Exists")
        
# Q41
# Traverse the tuple in reverse order using indexing (not slicing).
n=(10,20,30,40,50,50,50)
for i in range(len(n)-1,-1,-1):
    print(n[i])

# Q42
# Print only elements present at even indexes.
n=(10,20,30,40,50,50,50)
for i in range(0,len(n),2):
    print(n[i])
    
for i,val in enumerate(n):
    if i%2==0:
        print(val)
        
n = (10,20,30,40,50,60)
i = 0
while i < len(n):
    print(n[i])
    i += 2
    

# Q43

# Print only elements present at odd indexes.
n=(10,20,30,40,50,50,50)
for i in range(1,len(n),2):
    print(n[i])
    
for i,val in enumerate(n):
    if i%2!=0:
        print(val)
    
i=1
while i < len(n):
    print(n[i])
    i+=2
    
    
# Q44

# Unpack
# student=("Sunny",21,"AIDS")

# into three variables and print them separately.
student=("Sunny",21,"AIDS")
name,age,branch=student
print(name)
print(age)
print(branch)


# Q45
# Create a tuple inside another tuple and print only the second inner tuple.
# Example:
# ((10,20),(30,40),(50,60))
# Output:
# (30,40)
n=((10,20),(30,40),(50,60))
print(n[1])


# PART-4 : Google / Amazon Challenge
# Q46
# Given
# numbers=(10,20,30,40,50,60,70,80,90,100)
# Without using:
# sum()
# max()
# min()
# count()
# Find in one program:
# Total
# Average
# Largest
# Smallest
# Even count
# Odd count
# Search whether 70 exists
# Reverse traversal
# Print index and value together
# Number of iterations

numbers=(10,20,30,40,50,60,70,80,90,100)
total=0
largest=numbers[0]
smallest=numbers[0]
even_count=0
odd_count=0
iterations=0
for i in numbers:
    total+=i
    if i>largest:
        largest=i
    elif i<smallest:
        smallest=i
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
average=total/len(numbers)
print(total)
print(average)
print(largest)
print(smallest)
print(even_count)
print(odd_count)
if 70 in numbers:
    print("70 exists")
else:
    print("not exists")
for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])
for i,v in enumerate(numbers):
    print(i,v)
for i in numbers:
    iterations+=1
print(iterations)