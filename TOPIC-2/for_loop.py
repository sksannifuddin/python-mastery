
# Q1 Print numbers from 1 to 10.
for i in range(1,11):
    print(i)
    
# Q2 Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)
    
# Q3 Print all even numbers from 1 to 100.
for i in range(1,101):
    if i%2==0:
        print(i)
        
for i in range(2,101,2):
    print(i)

# Q4 Print all odd numbers from 1 to 100.
for i in range(1,101):
    if i%2!=0:
        print(i)
        
for i in range(1,101,2):
    print(i)
    
# Q5 Take a number n.
# Print the multiplication table.
# Example:
# Input:
# 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
num=5
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

# Q6 Take n.
# Find the sum of numbers from 1 to n.
# Example:
# Input:
# 5
# Output:
# 15
num=5
total=0
for i in range(1,num+1):
    total+=i
print(total)
    

# Q7 Take n.
# Find the factorial.
# Example:
# Input:
# 5
# Output:
# 120
num=5
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

# Q8 Take n.
# Count how many numbers are divisible by 3 between 1 and n.
num=10
count=0
for i in range(1,num+1):
    if i%3==0:
        count+=1
print(count)

# Q9 Take n.
# Print squares of numbers from 1 to n.
# Example:
# 1
# 4
# 9
# 16
# 25
num=5
for i in range(1,num+1):
    print(i**2)

# Q10 Take n.
# Print cubes from 1 to n.
num=5
for i in range(1,num+1):
    print(i**3)
    



# Q11
for i in range(5):
    print(i)
# output:-0,1,2,3,4


# Q12
for i in range(1,6):
    print(i)
# output:-1,2,3,4,5

# Q13
for i in range(2,11,2):
    print(i)
# output:- 2,4,6,8,10

# Q14
for i in range(10,0,-2):
    print(i)
# output:-10,8,6,4,2

# Q15
s = 0
for i in range(1,6):
    s += i
print(s)
# output:-15

# Q16
fact = 1
for i in range(1,5):
    fact *= i
print(fact)
# output:-24

# Q17
for i in range(3):
    print("Python")
# output:- Python,Python,Python

# Q18
for i in range(1):
    print(i)
# output:- 0

# Q19
for i in range(5,0,-1):
    print(i)
# output:- 5,4,3,2,1

# Q20
for i in range(1,10,3):
    print(i)
# output:- 1,4,7

# Q21
for i in range(5):
    print(i)
else:
    print("Done")
# output:- 0,1,2,3,4,done

# Q22
total = 0
for i in range(2,8):
    total += i
print(total)
# output:- 27

# Q23
for i in range(1,6):
    if i % 2 == 0:
        print(i)
# output:- 2,4

# Q24
count = 0
for i in range(10):
    count += 1
print(count)
# output:-  10

# Q25
for i in range(5):
    print(i*i)
# output:-0,1,4,9,16

# Q26 Take n.
# Count how many even numbers are between 1 and n.
n=20
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print(count)
        
    
# Q27 Take n.
# Count how many odd numbers are between 1 and n.
n=20
count=0
for i in range(1,n+1):
    if i%2!=0:
        count+=1
print(count)

# Q28 Take n.
# Find the sum of all even numbers from 1 to n.
n=50
total=0
for i in range(1,n+1):
    if i%2==0:
        total+=i
print(total)

# Q29 Take n.
# Find the sum of all odd numbers from 1 to n.
n=50
total=0
for i in range(1,n+1):
    if i%2!=0:
        total+=i
print(total)

# Q30 Take n.
# Print all numbers divisible by 7 from 1 to n.
n=42
for i in range(1,n+1):
    if i%7==0:
        print(i)
        

# 🚀 Bonus Challenge (Google Level)
# Q31 Take n.
# Print numbers from 1 to n, but:
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by 3 and 5, print "FizzBuzz".
# Example:
# Input:
# 15
# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
n=20
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)