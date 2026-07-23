# ============================================
# LISTS - MODULE 2
# (Indexing & Slicing)
# ============================================
# PART-1 : Coding Questions
# Q1
# Create a list:
# numbers = [10,20,30,40,50]
# Print the first element.
numbers = [10,20,30,40,50]
print(numbers[0])

# Q2
# Print the last element.
numbers = [10,20,30,40,50]
print(numbers[-1])

# Q3
# Print the third element.
numbers = [10,20,30,40,50]
print(numbers[2])

# Q4
# Print the second last element.
numbers = [10,20,30,40,50]
print(numbers[-2])

# Q5
# Create
# fruits = ["Apple","Banana","Mango","Orange","Kiwi"]
# Print "Mango".
fruits = ["Apple","Banana","Mango","Orange","Kiwi"]
print(fruits[2])

# Q6
# Create
# colors = ["Red","Green","Blue","Black","White"]
# Print "White" using negative indexing.
colors = ["Red","Green","Blue","Black","White"]
print(colors[-1])

# Q7
# Print the first three elements.
colors = ["Red","Green","Blue","Black","White"]
print(colors[0:3])

# Q8
# Print the last three elements.
colors = ["Red","Green","Blue","Black","White"]
print(colors[-3:])

# Q9
# Print every element except the first one.
colors = ["Red","Green","Blue","Black","White"]
print(colors[1:])

# Q10
# Print every element except the last one.
colors = ["Red","Green","Blue","Black","White"]
print(colors[0:-1])


# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# a = [10,20,30,40]
# print(a[0])

# Predict Output.:- 10

# Q12
# a = [10,20,30,40]
# print(a[-1])

# Predict Output.:- 40

# Q13
# a = [5,10,15,20,25]
# print(a[2])

# Predict Output.:- 15

# Q14
# a = ["A","B","C","D"]
# print(a[-2])

# Predict Output.:- C

# Q15
# a = [1,2,3,4,5]
# print(a[1:4])

# Predict Output.:- [2,3,4]

# Q16
# a = [1,2,3,4,5]
# print(a[:3])

# Predict Output.:- [1,2,3]

# Q17
# a = [1,2,3,4,5]
# print(a[2:])

# Predict Output.:- [3,4,5]

# Q18
# a = [10,20,30,40,50]
# print(a[::-1])

# Predict Output.:- [50,40,30,20,10]

# Q19
# a = [10,20,30,40,50]
# print(a[::2])

# Predict Output.:-[10,30,50]

# Q20
# a = [10,20,30,40,50]
# print(a[1::2])

# Predict Output.:- [20,40]

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# a = [10,20,30,40,50]
# print(a[-5])

# Predict Output.:-10

# Q22
# a = [10,20,30,40,50]
# print(a[len(a)-1])

# Predict Output.:- 50

# Q23
# a = [1,2,3,4,5]
# print(a[3:3])

# Predict Output.:- []

# Q24
# a = [1,2,3,4,5]
# print(a[-4:-1])

# Predict Output.:- [2,3,4]

# Q25
# a = [1,2,3,4,5]
# print(a[4:1:-1])

# Predict Output.:-5,4,3

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26

# Take a list.
# Print:
# First element
# Last element
s=[1,2,3,4]
print(s[0])
print(s[-1])

# Q27
# Take a list.
# Print the middle element.
# (Hint: len())
s=[1,2,3,4]
print(s[len(s)//2])


# Q28
# Take a list.
# Print:
# Second element
# Second last element
s=[1,2,3,4]
print(s[1])
print(s[-2])

# Q29

# Take a list.
# Print every alternate element using slicing.
s=[1,2,3,4,5,6,7,8]
print(s[::2])

# Q30

# Take a list of 10 numbers.
# Print:
# First five numbers
# Last five numbers
s=[1,2,3,4,5,6,7,8,9,10]
print(s[0:5])
print(s[-5:])

# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31

# Create a list containing 20 integers.
# Using slicing only, print:
# First 5 elements
# Last 5 elements
# Middle 6 elements
# Every alternate element
# Reverse the list
# List without the first and last element
# Every third element
# Reverse every alternate element


s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(s[0:5])
print(s[-5:])
mid=len(s)//2
print(s[mid-3:mid+3])
print(s[::2])
print(s[::-1])
print(s[1:-1])
print(s[::3])
print(s[::-2])