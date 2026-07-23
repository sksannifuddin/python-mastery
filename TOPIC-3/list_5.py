# ============================================
# LISTS - MODULE 5
# (sort(), reverse(), copy(), count(), index())
# ============================================
# PART-1 : Coding Questions
# Q1
# # Create:
# # numbers = [40,10,50,20,30]
# # Sort the list in ascending order.
# # Print the list.
numbers = [40,10,50,20,30]
numbers.sort()
print(numbers)

# Q2
# # Create:
# # numbers = [40,10,50,20,30]
# # Sort the list in descending order.
# # Print the list.
numbers = [40,10,50,20,30]
numbers.sort(reverse=True)
print(numbers)
# Q3
# # Create:
# # fruits = ["Mango","Apple","Orange","Banana"]
# # Sort the list alphabetically.
# # Print the list.
fruits = ["Mango","Apple","Orange","Banana"]
fruits.sort()
print(fruits)
# Q4
# # Create:
# # numbers = [10,20,30,40,50]
# # Reverse the list.
# # Print the list.
numbers = [10,20,30,40,50]
numbers.reverse()
print(numbers)

# Q5
# # Create:
# # colors = ["Red","Green","Blue"]
# # Make a copy of the list.
# # Print the copied list.
colors = ["Red","Green","Blue"]
a=colors.copy()
print(a)

# Q6
# # Create:
# # numbers = [10,20,30,20,40,20]
# # Count how many times 20 appears.
numbers = [10,20,30,20,40,20]
print(numbers.count(20))

# Q7
# # Create:
# # fruits = ["Apple","Banana","Mango","Orange"]
# # Find the index of "Mango".
fruits = ["Apple","Banana","Mango","Orange"]
print(fruits.index("Mango"))

# Q8
# # Create:
# # letters = ["A","B","C","B","D"]
# # Count how many times "B" appears.
letters = ["A","B","C","B","D"]
print(letters.count("B"))

# Q9
# # Create:
# # cities = ["Delhi","Mumbai","Chennai","Hyderabad"]
# # Find the index of "Hyderabad".
cities = ["Delhi","Mumbai","Chennai","Hyderabad"]
print(cities.index("Hyderabad"))

# Q10
# # Create:
# # marks = [90,85,75,95,80]
# # Reverse the list.
# # Print the list.
marks = [90,85,75,95,80]
marks.reverse()
print(marks)

# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================


# Q11
# # a = [30,10,20]
# # a.sort()
# # print(a)

# # Predict Output:- [10,20,30]
# Q12
# # a = [30,10,20]
# # a.reverse()
# # print(a)

# # Predict Output:- [20,10,30]
# Q13
# # a = [1,2,3]
# # b = a.copy()
# # print(b)

# # Predict Output:-[1,2,3]

# Q14
# # a = [10,20,20,30]
# # print(a.count(20))

# # Predict Output:- 2
# Q15
# # a = ["Python","Java","C"]
# # print(a.index("Java"))

# # Predict Output:- 1
# Q16
# # a = [5,4,3,2,1]
# # a.sort()
# # print(a)

# # Predict Output:- [1,2,3,4,5]
# Q17
# # a = ["C","A","B"]
# # a.sort()
# # print(a)

# # Predict Output:- ["A","B","C"]
# Q18
# # a = [10]
# # print(a.count(10))

# # Predict Output:- 1
# Q19
# # a = [10,20,30]
# # print(a.index(30))

# # Predict Output:-2
# Q20
# # a = [1,2,3]
# # a.reverse()
# # print(a)

# # Predict Output:- [3,2,1]
# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# # a = [10,20,10,30]
# # print(a.index(10))

# # Predict Output:- 0
# Q22
# # a = [10,20,30]
# # b = a.copy()
# # b.append(40)
# # print(a)

# # Predict Output:- [10,20,30]
# Q23
# # a = [5,4,3,2,1]
# # print(sorted(a))

# # Predict Output:-[1,2,3,4,5]
# Q24
# # a = [1,2,3]
# # print(a[::-1])

# # Predict Output:-[3,2,1]
# Q25
# # a = [3,1,2]
# # print(sorted(a, reverse=True))

# # Predict Output:- [3,2,1]


# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26
# # Create:
# # [50,40,30,20,10]
# #
# # Sort the list.
# #
# # Print it.
n=[50,40,30,20,10]
n.sort()
print(n)

# Q27
# # Create:
# # ["Python","Java","C++","Go"]
# #
# # Reverse the list.
# #
# # Print it.
p=["Python","Java","C++","Go"]
p.reverse()
print(p)

# Q28
# # Create:
# # [10,20,30,20,40,20]
# #
# # Print:
# # Number of times 20 appears.
n=[10,20,30,20,40,20]
print(n.count(20))

# Q29
# # Create:
# # ["Red","Blue","Green","Black"]
# # Print the index of "Green".
c=["Red","Blue","Green","Black"]
print(c.index("Green"))


# Q30
# # Create:
# # [90,80,70,60]
# # Make a copy.
# # Reverse only the copied list.
# #
# # Print:
# # Original list
# # Copied list
s=[90,80,70,60]
a=s.copy()
a.reverse()
print(s)
print(a)



# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31
# # Create:
# # [40,20,50,10,60,30,20,10]
# # Perform the following:
# # Sort ascending
# # Reverse the list
# # Count occurrences of 20
# # Count occurrences of 10
# # Find index of 50
# # Make a copy
# # Sort the copied list in descending order

# # Finally print:

# # Original list
# # Copied list
# # Length
# # Largest element
# # Smallest element
# # Sum of all elements
# # Average
# 📌 Interview Concepts Covered

s=[40,20,50,10,60,30,20,10]
s.sort()
s.reverse()
a=s.count(20)
b=s.count(10)
c=s.index(50)
d=s.copy()
d.sort(reverse=True)

print(s)
print(d)
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sum(s)//len(s))