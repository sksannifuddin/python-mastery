# LISTS - MODULE 8
# (Searching, Calculations & List Comprehension)
# ============================================
# PART-1 : Coding Questions
# Q1

# Create a list of 10 integers.

# Find the sum without using sum().
numbers=[1,2,3,4,5,6,7,8,9,10]
total=0
for i in numbers:
    total+=i
print(total)


# Q2

# Find the average without using sum().
numbers=[1,2,3,4,5,6,7,8,9,10]
total=0
for i in numbers:
    total+=i
average=total/len(numbers)
print(average)


# Q3

# Find the largest element without using max().
numbers=[1,2,3,4,5,6,7,8,9,10]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print(largest)


# Q4

# Find the smallest element without using min().
numbers=[1,2,3,4,5,6,7,8,9,10]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print(smallest)


# Q5

# Search whether 50 exists in the list.
# Print:
# Found
# or
# Not Found
found = False

for i in numbers:
    if i == 50:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")

# Q6
# Count the frequency of 20 without using count().
numbers=[10,20,20,20,20,20,10,30,40,50,60]
count=0
for i in numbers:
    if 20 == i:
        count+=1
print(count)
    
    
# Q7

# Count

# Even numbers
# Odd numbers
# Positive numbers
# Negative numbers
# Zeroes
# using only one loop.
numbers=[1,2,3,4,5,6,7,8,8,50]
counteven=0
countodd=0
countpositive=0
countnegative=0
countzeroes=0
for i in numbers:
    if i%2==0:
        counteven+=1
    else:
        countodd+=1
    if i>0:
        countpositive+=1
    else:
        countnegative+=1
    if i==0:
        countzeroes+=1
print(counteven)
print(countodd)
print(countpositive)
print(countnegative)
print(countzeroes)

# Q8

# Print all elements greater than the average.
numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
average=sum(numbers)/len(numbers)
greatest=[]
for i in numbers:
    if i>average:
        greatest.append(i)
print(greatest) 

# Q9 ⭐ (New Concept)

# Create a list containing the squares of numbers from 1 to 20 using list comprehension.

# Example:

# [1,4,9,16,...]
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers=[x**2 for x in numbers ]
print(numbers)

# Q10
# Create a list containing only the even numbers from 1 to 100 using list comprehension.
even=[x for x in range(1,101) if x%2==0]
print(even)

# Q11
# Create a list containing only the odd numbers from 1 to 100 using list comprehension.
odd=[x for x in range(1,101) if x%2!=0]
print(odd)


# Q12
# Create a list containing the cubes of numbers from 1 to 15.
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numbers=[x**3 for x in numbers ]
print(numbers)

# Q13

# Given
# numbers=[10,15,20,25,30,35]
# Create a new list containing only the even numbers using list comprehension.
numbers=[10,15,20,25,30,35]
evens=[x for x in numbers if x%2==0]
print(evens)

# Q14
# Given
# numbers=[10,15,20,25,30,35]
# Create another list containing only the odd numbers.
numbers=[10,15,20,25,30,35]
odds=[x for x in numbers if x%2!=0]
print(odds)


# Q15
# Given
# names=["Sunny","Ravi","Ajay","Sonia"]
# Create another list containing every name in uppercase.
names=["Sunny","Ravi","Ajay","Sonia"]
upper=[x.upper() for x in names ]
print(upper)

# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q16
# a=[x for x in range(5)]
# print(a)
# output:-[0,1,2,3,4]
# Q17
# a=[x*x for x in range(5)]
# print(a)
# output:-[0,1,4,9,16]
# Q18
# a=[x for x in range(10) if x%2==0]
# print(a)
# output:-[0,2,4,6,8]
# Q19
# a=[x for x in range(10) if x>5]
# print(a)
# output:-[6,7,8,9]
# Q20
# a=[x.upper() for x in ["python","java"]]
# print(a)
# output:-['PYTHON','JAVA']
# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
numbers = [10,20,20,20,20,20,10,30,40,50,60]

largest = numbers[0]
smallest = numbers[0]
total = 0
count = 0

for num in numbers:

    # Sum
    total += num

    # Largest
    if num > largest:
        largest = num

    # Smallest
    if num < smallest:
        smallest = num

    # Count of 20
    if num == 20:
        count += 1

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Count of 20:", count)



# Q22

# Without using in,

# search whether 75 exists.
found = False

for x in numbers:
    if x == 75:
        found = True
        break

print("Exists" if found else "Not Exists")

# Q23
# Without using count(),
# find the frequency of every element.
numbers=[10,20,20,20,20,20,10,30,40,50,60,75]
numbers1={}
for x in numbers:
    if x in numbers1:
        numbers1[x]+=1
    else:
        numbers1[x]=1
for i,value in numbers1.items():
    print(f"{i} -> {value}")
    
        
# Example:
# 10 -> 2
# 20 -> 3
# 30 -> 1

# Q24
# Using one loop only,
# calculate
# Sum
# Average
# Even count
# Odd count
# Largest
# Smallest
numbers = [1,2,3,4,5,6,7,8,9,10]

total = 0
even_count = 0
odd_count = 0
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    # Sum
    total += num

    # Even / Odd Count
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # Largest
    if num > largest:
        largest = num

    # Smallest
    if num < smallest:
        smallest = num

# Average (after the loop)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Largest:", largest)
print("Smallest:", smallest)

# Q25 ⭐

# Given

# numbers=[10,20,30,40]

# Create

# [20,40,60,80]

# using only list comprehension.
numbers=[10,20,30,40]
numbers=[x*2 for x in numbers]
print(numbers)


# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26

# Find the largest and smallest numbers without built-in functions.
numbers=[1,2,3,4,5,6,7,8,9,10]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print(largest)

numbers=[1,2,3,4,5,6,7,8,9,10]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print(smallest)
# Q27

# Find all numbers greater than the average.
numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
average=sum(numbers)/len(numbers)
greatest=[]
for i in numbers:
    if i>average:
        greatest.append(i)
print(greatest) 

# Q28

# Create a list of squares using list comprehension.
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers=[x**2 for x in numbers ]
print(numbers)

# Q29

# Convert every string to lowercase using list comprehension.
names=["SUNNY","RAVI","AJAY","SONIA"]
lower=[x.lower() for x in names ]
print(lower)


# Q30

# Count the frequency of every element.
numbers=[10,20,20,20,20,20,10,30,40,50,60,75]
numbers1={}
for x in numbers:
    if x in numbers1:
        numbers1[x]+=1
    else:
        numbers1[x]=1
for i,value in numbers1.items():
    print(f"{i} -> {value}")
# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31

# Create a list containing 30 integers.

# Without using:

# sum()
# max()
# min()
# count()

# Perform everything in one program:

# Total Sum
# Average
# Largest
# Smallest
# Even Count
# Odd Count
# Positive Count
# Negative Count
# Zero Count
# Elements Greater Than Average
# Search whether 50 exists
# Search whether 100 exists
# Frequency of every element
# Create another list containing only even numbers (list comprehension)
# Create another list containing only odd numbers (list comprehension)
# Create another list containing the squares of every number (list comprehension)


numbers = [10, 20, -5, 0, 50, 20, 30, -10, 100, 40,
           50, 60, 70, 0, -20, 80, 90, 10, 5, 15,
           25, 35, 45, 55, 65, 75, 85, 95, -30, 100]

total = 0
largest = numbers[0]
smallest = numbers[0]

even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0
zero_count = 0

search_50 = False
search_100 = False

frequency = {}

for num in numbers:
    # total
    total += num

    # largest
    if num > largest:
        largest = num

    # smallest
    if num < smallest:
        smallest = num

    # even / odd count
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # positive / negative / zero count
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

    # search
    if num == 50:
        search_50 = True

    if num == 100:
        search_100 = True

    # frequency
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

average = total / len(numbers)

greater_than_average = []

for num in numbers:
    if num > average:
        greater_than_average.append(num)

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
squares = [num ** 2 for num in numbers]

print("Total Sum:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)

print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Zero Count:", zero_count)

print("Elements Greater Than Average:", greater_than_average)

print("50 exists:", search_50)
print("100 exists:", search_100)

print("Frequency of every element:")
for key, value in frequency.items():
    print(f"{key} -> {value}")

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
print("Squares:", squares)