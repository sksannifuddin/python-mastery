# SETS — MODULE 1
# (Creation, Methods, Membership, Iteration, Built-in Functions)
# PART 1 — Coding Questions
# Q1
# Create a set containing:
# 10,20,30,40,50
# Print the set.
s={10,20,30,40,50}
print(s)

# Q2
# Create an empty set.
# Print its type.
s=set()
print(type(s))

# Q3
# Create
# {10,20,20,30,30,40}
# Print the set.
# Observe the output.
s={10,20,20,30,30,40}
print(s)
# {40, 10, 20, 30}

# Q4
# Create a set containing:
# 10
# "Python"
# 3.14
# True
s={10,"Python", 3.14, True}
print(s)
# Print it.

# Q5
# Create
# {"Apple","Banana","Mango"}
# Add "Orange" using add().
s={"Apple","Banana","Mango"}
s.add("Orange")
print(s)

# Q6
# Create
# {10,20,30}
# Use update() to add:
# 40,50,60
s={10,20,30}
t={40,50,60}
s.update(t)
print(s)

# Q7
# Remove 20 using remove().
s={10,20,20,30,30,40}
s.remove(20)
print(s)

# Q8
# Remove 100 using discard().
# Observe whether an error occurs.
s={10,20,20,30,30,40}
s.discard(100)
print(s)
# did not got any errors

# Q9
# Use pop() on
# {10,20,30,40}
# Print the removed element and the remaining set.
s={10,20,20,30,30,40}
b=s.pop()
print(b)
print(s)

# Q10
# Use clear() on a set.
# Print the result.
s={10,20,20,30,30,40}
s.clear()
print(s)

# Q11
# Copy a set using copy().
# Print both sets.
s={10,20,20,30,30,40}
b=s.copy()
print(b)
print(s)

# Q12
# Check whether
# 30
# exists using in.
s={10,20,20,30,30,40}
if 30 in s:
    print("exists")
else:
    print("not exists")

# Q13
# Check whether
# 100
# does not exist using not in.
s={10,20,20,30,30,40}
if 100 not in s:
    print("not exists")
else:
    print("exists")

# Q14
# Print every element using a for loop.
s={10,20,20,30,30,40}
for i in s:
    print(i)

# Q15
# Print every element with enumerate().
s={10,20,20,30,30,40}
for i,v in enumerate(s):
    print(i,v)

# Q16
# Print the length using len().
s={10,20,20,30,30,40}
print(len(s))

# Q17
# Find
# minimum
# maximum
# sum
# using built-in functions.
s={10,20,20,30,30,40}
print(max(s))
print(min(s))
print(sum(s))

# Q18
# Count even numbers using a loop.
s={10,20,20,30,30,40,15}
count=0
for i in s:
    if i%2==0:
        count+=1
print(count)

# Q19
# Count odd numbers using a loop.
s={10,20,20,30,30,40,15}
count=0
for i in s:
    if i%2!=0:
        count+=1
print(count)


# Q20
# Find the largest element without using max().
s={10,20,20,30,30,40,15}
for i in s:
   largest=i
   break
for i in s:
    if i >largest:
        largest=i
print(largest)

# Q21

# Find the smallest element without using min().
s={10,20,20,30,30,40,15}
for i in s:
   smallest=i
   break
for i in s:
    if i<smallest:
        smallest=i
print(smallest)

# Q22
# Find the sum without using sum().
s={10,20,20,30,30,40,15}
total=0
for i in s:
    total+=i
print(total)

# Q23
# Search whether 50 exists without using in.
s={10,20,20,30,30,40,15}
for i in s:
    if 50 == i :
        print("exists")
        break
else:
    print("not exists")

# Q24
# Count total elements without using len().
s={10,20,20,30,30,40,15}
count=0
for i in s:
    count+=1
print(count)

# Q25
# Create a set from this list.
# [10,20,20,30,40,40]
# Observe the output.
l=[10,20,20,30,40,40]
s=set(l)
print(s)


# PART 2 — Output Prediction
# Q26
# a={10,20,20,30}
# print(a)
# output:- {10,20,30}
# Q27
# a=set()
# print(type(a))
# output:- <class 'set'>
# Q28
# a={}
# print(type(a))
# output:- <class 'dict'>
# Q29
# a={10,20}
# a.add(30)
# print(a) 
# output:- {10,20,30}
# Q30
# a={10,20}
# a.update([30,40])
# print(a)
# output:- {40, 10, 20, 30}
# Q31
# a={10,20,30}
# a.remove(20)
# print(a)
# output:- {10,30}
# Q32
# a={10,20}
# a.discard(50)
# print(a)
# output:- {10,20}
# Q33
# a={10,20}
# print(len(a))
# output:- 2
# Q34
# a={5,10,15}
# print(sum(a))
# output:- 30
# Q35
# a={5,10,15}
# print(min(a),max(a))
# output:- 5,15

# PART 3 — Placement Questions
# Q36
# Remove duplicates from
# [10,20,20,30,30,40]
# using a set.
l=[10,20,20,30,30,40]
s=set(l)
print(s)

# Q37
# Without using len(), count the number of elements in a set.
s={10,20,20,30,30,40,15}
count=0
for i in s:
    count+=1
print(count)

# Q38
# Without using sum(), find the total.
s={10,20,20,30,30,40,15}
total=0
for i in s:
    total+=i
print(total)

# Q39
# Without using max(), find the largest element.
s={10,20,20,30,30,40,15}
for i in s:
   largest=i
   break
for i in s:
    if i >largest:
        largest=i
print(largest)

# Q40

# Without using min(), find the smallest element.
s={10,20,20,30,30,40,15}
for i in s:
   smallest=i
   break
for i in s:
    if i <smallest:
        smallest=i
print(smallest)

# Q41

# Explain the difference between

# {}

# and

# set()

# {} creates an empty dictionary.

# set() creates an empty set.

# Example:

# a={}
# print(type(a))      # dict

# b=set()
# print(type(b))      # set
# Q42

# Why does a set automatically remove duplicates?

# Explain with an example.
#  Sets store only unique (hashable) values. Whenever duplicate values are inserted, Python automatically keeps only one copy.
s={1,2,3,3,2,1}
print(s)
# output:- {1,2,3}
# Q43

# Why can't we access a set using indexing?
# Sets are unordered collections. Since elements do not have fixed positions, indexing is not supported.
# Explain with code.
s={1,2,3,3,2,1}
print(s)

# PART 4 — Google / Amazon Challenge
# Q44

# Given

# numbers={10,20,30,40,50,60,70,80,90,100}

# Without using

# sum()
# max()
# min()
# len()

# Find:

# Total
# Average
# Largest
# Smallest
# Even count
# Odd count
# Search whether 70 exists
# Number of iterations
numbers={10,20,30,40,50,60,70,80,90,100}

total=0
count=0
even_count=0
odd_count=0
found_70=False

for i in numbers:
    largest=i
    smallest=i
    break

for num in numbers:
    total+=num
    count+=1

    if num>largest:
        largest=num

    if num<smallest:
        smallest=num

    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

    if num==70:
        found_70=True

average=total/count

print("Total:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("70 Exists:", found_70)
print("Number of Iterations:", count)
# Q45

# Given

# data=[10,20,20,30,30,40,40,50,60,60]

# Perform:

# Convert to set
# Print unique elements
# Print total unique elements
# Find largest
# Find smallest
# Find sum
# Count even numbers
# Count odd numbers
# Search whether 50 exists
# Traverse using a loop
data=[10,20,20,30,30,40,40,50,60,60]

s=set(data)

total=0
count=0
even_count=0
odd_count=0
found_50=False

for i in s:
    largest=i
    smallest=i
    break

for num in s:
    print(num)

    total+=num
    count+=1

    if num>largest:
        largest=num

    if num<smallest:
        smallest=num

    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

    if num==50:
        found_50=True

print("Unique Elements:", s)
print("Total Unique Elements:", count)
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("50 Exists:", found_50)

# This module covers 100% of the basic Set concepts. After completing it, you'll be ready for Module 2 (Set Operations: Union, Intersection, Difference, Symmetric Difference, Subset, Superset, Disjoint, frozenset, etc.) without missing any foundational topic.