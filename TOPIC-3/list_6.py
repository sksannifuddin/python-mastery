# ============================================
# LISTS - MODULE 6
# (Membership, Concatenation, Repetition, Comparison, Identity)
# ============================================
# PART-1 : Coding Questions
# Q1
# # Create:
# # numbers = [10,20,30,40]
# # Check whether 20 is present.
numbers = [10,20,30,40]
print(20 in numbers)

# Q2
# # Create:
# # fruits = ["Apple","Banana","Mango"]
# # Check whether "Orange" is present.
fruits = ["Apple","Banana","Mango"]
print("Orange" in fruits)

# Q3
# # Create:
# # colors = ["Red","Green","Blue"]
# # Check whether "Black" is NOT present.
colors = ["Red","Green","Blue"]
print("Black" not in colors)

# Q4
# # Create:
# # a = [1,2,3]
# # b = [4,5,6]
# # Concatenate both lists.
# # Print the results
a = [1,2,3]
b = [4,5,6]
print(a+b)

# Q5
# # Create:
# # letters = ["A","B"]
# # Repeat the list 3 times.
# # Print the result.
letters = ["A","B"]
print(letters*3)


# Q6
# # Create:
# # a = [10,20]
# # b = [10,20]
# # Compare using ==
# # Print the result.
a = [10,20]
b = [10,20]
print(a==b)

# Q7
# # Create:
# # a = [10,20]
# # b = a
# # Compare using is
# # Print the result.
a=[10,20]
b=a
print(b is a)

# a = [10,20]
# b = a
# Q8
# # Create:
# # a = [10,20]
# # b = [10,20]
# # Compare using is
# # Print the result.
a = [10,20]
b = [10,20]
print(a is b)

# Q9
# # Create:
# # marks = [70,80,90]
# # Check whether 100 is in the list.
marks = [70,80,90]
print(100 in marks)


# Q10
# # Create:
# # names = ["Sunny","Ravi","Ajay"]
# # Check whether "Sunny" is NOT in the list.
names = ["Sunny","Ravi","Ajay"]
print("Sunny" not in names)


# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# a = [1,2,3]
# print(2 in a)
# Predict Output:- True

# Q12
# a = [1,2,3]
# print(5 in a)
# Predict Output:- False

# Q13
# a = [1,2]
# b = [3,4]
# print(a+b)
# Predict Output:- [1,2,3,4]

# Q14
# a = [10]
# print(a*3)
# Predict Output:- [10,10,10]

# Q15
# a = [1,2]
# b = [1,2]
# print(a==b)
# Predict Output: True

# Q16
# a = [1,2]
# b = [1,2]
# print(a is b)
# Predict Output:- False

# Q17
# a = [1,2]
# b = a
# print(a is b)
# Predict Output:- True

# Q18
# a = ["Python"]
# print("Python" in a)
# Predict Output:- True

# Q19
# a = [10,20]
# print(30 not in a)
# Predict Output:- True

# Q20
# a = [1]
# print(a+a)
# Predict Output:- [1,1]

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# a = [1,2]

# b = a.copy()

# print(a is b)

# Predict Output:- False

# Q22
# a = [1,2]

# b = a.copy()

# print(a==b)

# Predict Output:-True

# Q23
# a = []

# print(bool(a))

# Predict Output:- False

# Q24
# a = [0]

# print(bool(a))

# Predict Output:True

# Q25
# a = [1,2]

# print(a*0)

# Predict Output:-[]

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26
# # Create two lists.
# # Concatenate them.
# # Print the final list.
a=[1,2,3]
b=[4,5,6]
print(a+b)

# Q27
# # Create a list of programming languages.
# # Check whether "Python" exists.
a = ["Python","Java","C"]
print("Python" in a)

# Q28
# # Create a list:
# # [10,20,30]
# # Repeat it four times.
a=[10,20,30]
print(a*4)

# Q29
# # Create two identical lists.
# # Print:
# # a == b
# # a is b
a=[10,20,30]
b=[10,20,30]
print(a==b)
print(a is b)

# Q30
# # Create a list of five cities.
# # Check whether "Delhi" is present.
# # Check whether "London" is not present.
cities = ["Delhi","Mumbai","Chennai","Hyderabad"]
print("Delhi" in cities)
print("London" not in cities)


# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31
# # Create two lists.

# # a = [10,20,30]
# # b = [40,50,60]


# # Perform the following:

# # Concatenate both lists
# # Repeat the result twice
# # Check whether 20 is present
# # Check whether 100 is absent
# # Create a copy
# # Compare:
# # ==
# # is

# # Finally print:

# # Final list
# # Length
# # First element
# # Last element
# # Sum of elements
# # Maximum
# # Minimum
# # Whether copy == original
# # Whether copy is original
# 📌 Interview Concepts Covered in Module 6

a = [10,20,30]
b = [40,50,60]
c=a+b
print(c*2)
print(20 in c)
print(100 not in c)
d=c.copy()
print(c==d)
print(c is d)

print(c)
print(len(c))
print(c[0])
print(c[-1])
print(sum(c))
print(max(c))
print(min(c))
