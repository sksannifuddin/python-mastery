# ============================================
# LISTS - MODULE 4
# (remove(), pop(), clear(), del)
# ============================================
# PART-1 : Coding Questions
# Q1
# # Create:
# # numbers = [10,20,30,40,50]
# # Remove 30 using remove().
# # Print the list.
numbers = [10,20,30,40,50]
numbers.remove(30)
print(numbers)

# Q2
# # Create:
# # fruits = ["Apple","Banana","Mango","Orange"]
# # Remove "Banana".
# # Print the list.
fruits = ["Apple","Banana","Mango","Orange"]
fruits.remove("Banana")
print(fruits)

# Q3
# # Create:
# # colors = ["Red","Green","Blue"]
# # Remove "Green".
# # Print the list.
colors = ["Red","Green","Blue"]
colors.remove("Green")
print(colors)

# Q4
# # Create:
# # numbers = [10,20,30,40]
# # Remove the last element using pop().
# # Print the list.
numbers = [10,20,30,40]
numbers.pop()
print(numbers)

# Q5
# # Create:
# # numbers = [10,20,30,40]
# # Remove the first element using pop().
# # Print the list.
numbers = [10,20,30,40]
numbers.pop(0)
print(numbers)

# Q6
# # Create:
# # letters = ["A","B","C","D"]
# # Remove the element at index 2.
# # Print the list.
letters = ["A","B","C","D"]
letters.pop(2)
print(letters)


# Q7
# # Create:
# # marks = [70,80,90,100]
# # Store the removed value from pop().
# # Print the removed value.
# # Print the remaining list.
marks = [70,80,90,100]
x=marks.pop()
print(x)
print(marks)

# Q8
# # Create:
# # cities = ["Delhi","Mumbai","Chennai"]
# # Remove all elements using clear().
# # Print the list.
cities = ["Delhi","Mumbai","Chennai"]
cities.clear()
print(cities)

# Q9
# # Create:
# # numbers = [10,20,30]
# # Delete the list using del.
numbers = [10,20,30]
del numbers 

# Q10
# # Create:
# # fruits = ["Apple","Banana","Mango"]
# # Delete the second element using del.
# # Print the list.
fruits = ["Apple","Banana","Mango"]
del fruits[1]
print(fruits)

# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# # a = [10,20,30]
# # a.remove(20)
# # print(a)
# # Predict Output:- [10,30]
# Q12
# # a = [10,20,30]
# # print(a.pop())

# # Predict Output:- 30
# Q13
# # a = [10,20,30]
# # print(a)

# # Predict Output:- [10,20,30]
# Q14
# # a = [1,2,3]
# # a.pop(0)
# # print(a)

# # Predict Output:-[2,3]
# Q15
# # a = [10,20,30]
# # x = a.pop()
# # print(x)

# # Predict Output:30
# Q16
# # a = [1,2,3]
# # a.clear()
# # print(a)

# # Predict Output:[]
# Q17
# # a = [10,20]
# # del a[1]
# # print(a)

# # Predict Output:[10]
# Q18
# # a = [1,2,3]
# # a.remove(1)
# # print(len(a))

# # Predict Output:2
# Q19
# # a = [10]
# # a.pop()
# # print(a)

# # Predict Output:-[]
# Q20
# # a = ["A","B","C"]
# # print(a.pop(1))

# # Predict Output:-B

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# # a = [10,20,20,30]
# # a.remove(20)
# # print(a)

# # Predict Output:-[10,20,30]

# Q22
# # a = [1,2,3]
# # print(a.pop(-1))
# # Predict Output:-3

# Q23
# # a = [10,20,30]
# # del a
# # print(a)
# # Predict Output: name error: a is not defined

# Q24
# # a = [1,2,3]
# # a.clear()
# # print(bool(a))
# # Predict Output:False

# Q25
# # a = [10,20,30]
# # x = a.pop(1)
# # print(a, x)
# # Predict Output:-[10,30],20

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26
# # Create a list:
# # [10,20,30,40,50]
# # Remove:
# # 20
# # 40
# # Print the list.
l=[10,20,30,40,50]
l.remove(20)
l.remove(40)
print(l)

# Q27
# # Create:
# # ["Python","Java","C++","Go"]
# # Remove "Java"
# # Print the list.
program=["Python","Java","C++","Go"]
program.remove("Java")
print(program)

# Q28
# # Create:
# # [100,200,300,400,500]
# # Remove the third element using pop().
# # Print the list.
l=[100,200,300,400,500]
l.pop(2)
print(l)

# Q29
# # Create a list of five fruits.
# # Remove the first fruit using pop().
# # Print the list.
fruits = ["Apple","Banana","Mango","kiwi","Guava"]
fruits.pop(0)
print(fruits)

# Q30
# # Create:
# # [10,20,30,40]
# # Clear the list.
# # Print the list.
l=[10,20,30,40]
l.clear()
print(l)

# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31
# # Create:
# # [10,20,30,40,50,60,70,80]
# #
# # Perform the following:
# #
# # Remove 30
# # Pop the last element
# # Pop the first element
# # Remove 50
# # Append 100
# # Insert 15 at index 1
# # Extend [200,300]
# #
# # Finally print:
# #
# # Final list
# # Length
# # First element
# # Last element
# # Middle element
# # Sum of all numeric values
# # Largest value
# # Smallest value

l=[10,20,30,40,50,60,70,80]
l.remove(30)
l.pop()
l.pop(0)
l.remove(50)
l.append(100)
l.insert(1,15)
l.extend([200,300])
print(l)
print(len(l))
print(l[0])
print(l[-1])
print(l[len(l)//2])
print(sum(l))
print(max(l))
print(min(l))
