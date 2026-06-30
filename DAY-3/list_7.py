# ============================================
# LISTS - MODULE 7
# (Iteration using for loop, len(), range(), enumerate())
# ============================================
# PART-1 : Coding Questions
# # Q1
# # Create:
# # numbers = [10,20,30,40,50]
# # Print every element using a for loop.
numbers = [10,20,30,40,50]
for i in numbers:
    print(i)

# # Q2
# # Create:
# # fruits = ["Apple","Banana","Mango","Orange"]
# # Print every fruit using a for loop.
fruits = ["Apple","Banana","Mango","Orange"]
for i in fruits:
    print(i)
    
# # Q3
# # Create:
# # colors = ["Red","Green","Blue"]
# # Print every color on a new line.
colors = ["Red","Green","Blue"]
for i in colors:
    print(i)
# # Q4
# # Create:
# # numbers = [10,20,30,40]
# # Print the index and value using range().
numbers = [10,20,30,40]
for i in range(len(numbers)):
    print(i,numbers[i])


# # Q5
# # Create:
# # numbers = [5,10,15,20]
# # Print every element using len() and indexing.
numbers = [5,10,15,20]
for i in range(len(numbers)):
    print(numbers[i])


# # Q6
# # Create:
# # names = ["Sunny","Ajay","Ravi"]
# # Print:
# # Student : Sunny
# # Student : Ajay
# # Student : Ravi
names = ["Sunny","Ajay","Ravi"]
for  i in names:
    print(f"Student : {i}")


# # Q7
# # Create:
# # numbers = [1,2,3,4,5]
# # Print every number multiplied by 2.
numbers = [1,2,3,4,5]
for i in numbers:
    print(i*2)


# # Q8
# # Create:
# # numbers = [10,20,30]
# # Find the sum using a for loop.
numbers = [10,20,30]
sum=0
for i in numbers:
    sum+=i
print(sum)

# # Q9
# # Create:
# # numbers = [5,10,15,20]
# # Count how many elements are present without using len().
count=0
numbers = [5,10,15,20]
for i in numbers:
    count+=1
print(count)


# # Q10
# # Create:
# # letters = ["A","B","C","D"]
# # Print index and letter using enumerate().
letters = ["A","B","C","D"]
for index,letter in enumerate(letters):
    print(index,letter)

# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# # Q11
# # a = [10,20,30]
# # for i in a:
# #     print(i)

# # Predict Output:-  10
# 20 
# 30

# # Q12
# # a = [1,2]
# # for i in a:
# #     print(i*2)

# # Predict Output:- 2
# 4

# # Q13
# # a = ["A","B"]
# # for i in a:
# #     print(i,end=" ")

# # Predict Output:- A B

# # Q14
# # a = [10,20,30]
# # for i in range(len(a)):
# #     print(i)

# # Predict Output:- 0
1
2


# # Q15
# # a = [10,20,30]
# # for i in range(len(a)):
# #     print(a[i])

# # Predict Output:- 10
# 20
# 30

# # Q16
# # a = [5,10]
# # total = 0
# # for i in a:
# #     total += i
# # print(total)

# # Predict Output:-   15

# # Q17
# # a = [1,2,3]
# # count = 0
# # for i in a:
# #     count += 1
# # print(count)

# # Predict Output:- 3

# # Q18
# # a = ["Python"]
# # for index,value in enumerate(a):
# #     print(index,value)

# # Predict Output:- 0 Python

# # Q19
# # a = [10]
# # for i in range(len(a)):
# #     print(i,a[i])

# # Predict Output:- 0  10

# # Q20
# # a = [1,2,3]
# # for i in range(0,len(a),2):
# #     print(a[i])

# # Predict Output:-  1
# 3

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# # Q21
# # a = []
# # for i in a:
# #     print(i)
# # print("Done")

# # Predict Output:- 
#Done

# # Q22
# # a = [10,20,30]
# # for i in range(len(a)-1):
# #     print(a[i])

# # Predict Output:- 10
#20

# # Q23
# # a = [1,2,3]
# # for i in range(len(a)):
# #     a[i] *= 2
# # print(a)

# # Predict Output:- [2,4,6]

# # Q24
# # a = [10,20]
# # for index,value in enumerate(a):
# #     print(index*value)

# # Predict Output:- 0
# 20

# # Q25
# # a = ["A","B","C"]
# # for i in range(-1,-len(a)-1,-1):
# #     print(a[i])
# # Predict Output:- 'C'
# 'B'
#'A'


# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# # Q26
# # Create a list of 10 numbers.
# # Print every element.
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i)

# # Q27
# # Create a list of five fruits.
# # Print only their indexes.
fruits = ["Apple","Banana","Mango","Orange","Kiwi"]
for i,fruit in enumerate(fruits):
    print(i)

# # Q28
# # Create a list:
# # [10,20,30,40,50]
# # Print:
# # Index 0 -> 10
# # Index 1 -> 20
# # ...
numbers=[10,20,30,40,50]
for i,number in enumerate(numbers):
    print(f"Index {i} -> {number}")

# # Q29
# # Create a list of marks.
# # Find the total marks using a loop.
marks=[80,90,70,60,50]
total=0
for  i in marks:
    total+=i
print(total)

# # Q30
# # Create a list:
# # [5,10,15,20,25]
# # Count how many elements are greater than 10.
l=[5,10,15,20,25]
count=0
for i in l:
    if i>10:
        count+=1
print(count)
        

# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# # Q31

# # Create a list of 20 integers.

# # Print:

# # Every element
# # Every index
# # Index and value together
# # Sum of all elements
# # Average
# # Largest element (without max())
# # Smallest element (without min())
# # Count of even numbers
# # Count of odd numbers
# # Elements greater than average
# # Reverse traversal using indexing
# # Every alternate element
# # Every third element
# # Number of iterations performed
numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i)

numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers)):
    print(i)
    
numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
for i,number in enumerate(numbers):
    print(i,number)
    
  
numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
sum=0
for i in numbers:
    sum+=i
print(sum) 


numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
sum=0
for i in numbers:
    sum+=i
average=sum//len(numbers)
print(average)


numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
numbers.sort()
print(f"largest number = {numbers[-1]}")

numbers = [10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]

greatest = numbers[0]

for i in numbers:
    if i > greatest:
        greatest = i

print(greatest)


numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
numbers.sort()
print(f"smallest number = {numbers[0]}")

numbers = [10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print(smallest)


numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
count=0
for i in numbers:
    if i%2==0:
        count+=1
print(count)

numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
count=0
for i in numbers:
    if i%2!=0:
        count+=1
print(count)


numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
total=0
greatest=[]
for i in numbers:
    total+=i
average=total//len(numbers)
for i in numbers:
    if i>average:
        greatest.append(i)
print(greatest) 


numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
average=sum(numbers)/len(numbers)
greatest=[]
for i in numbers:
    if i>average:
        greatest.append(i)
print(greatest) 

numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
for i in numbers[::-1]:
    print(i)
    
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])
        
numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
print(numbers[::2])
print(numbers[::3])

numbers=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
count=0
for i in numbers:
    count+=1
print(count)



# # ✔ Traversal
# # ✔ Summation
# # Largest element (without max())
# # Smallest element (without min())
# # Count of even numbers
# # Count of odd numbers
# # Elements greater than average
# # Reverse traversal using indexing
# # Every alternate element
# # Every third element
# # Number of iterations performed