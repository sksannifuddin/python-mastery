# PART-1 : Coding Questions
# Q1 Print numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print(i)
    i+=1
    
# Q2 Print numbers from 10 to 1.
i=10
while i>0:
    print(i)
    i-=1
    
# Q3 Print all even numbers from 1 to 100.
i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1
    
# Q4 Print all odd numbers from 1 to 100.
i=1
while i<=100:
    if i%2!=0:
        print(i)
    i+=1

# Q5
# Take a number n.
# Print its multiplication table.
# Example
# Input:
# 5
# Output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50
n=6
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1

# Q6
# Take n.
# Find the sum of numbers from 1 to n.
# Example
# Input:
# 5
# Output:
# 15
n=5
sum=0
while n>0:
    sum+=n
    n-=1
print(sum)
    
# Q7
# Take n.
# Find the factorial.
# Example
# Input:
# 5
# Output:
# 120
n=5
factorial=1
while n>0:
    factorial*=n
    n-=1
print(factorial)

# Q8
# Take n.
# Count how many numbers are divisible by 3 between 1 and n.
n=12
count=0
while n>0:
    if n%3==0:
        count+=1
    n-=1
print(count)

# Q9
# Take n.
# Print squares from 1 to n.
n=5
i=1
while i<=n:
    print(i**2)
    i+=1

# Q10
# Take n.
# Print cubes from 1 to n.
n=5
i=1
while i<=n:
    print(i**3)
    i+=1


# Q11
i = 1
while i <= 5:
    print(i)
    i += 1
# output:- 1,2,3,4,5

# Q12
i = 5
while i >= 1:
    print(i)
    i -= 1
# output:- 5,4,3,2,1    

# Q13
i = 1
s = 0
while i <= 5:
    s += i
    i += 1
print(s)
# output:- 15


# Q14
i = 1
fact = 1
while i <= 4:
    fact *= i
    i += 1
print(fact)
# output:- 24

# Q15
i = 1
while i < 1:
    print(i)
print("Done")
# output:-   Done

# Q16
i = 2
while i <= 10:
    print(i)
    i += 2
# output:- 2,4,6,8,10

# Q17
i = 1
while i <= 5:
    print(i * i)
    i += 1
# output:- 1,4,9,16,25

# Q18
i = 10
while i > 0:
    print(i)
    i -= 3
# output:- 10,7,4,1

# Q19
i = 1
while i <= 3:
    print("Python")
    i += 1
# output:- Python Python Python

# Q20
i = 1
while i <= 5:
    print(i)
    i += 2
# output:- 1,3,5

# Q21

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Done")
# output:- 1,2,3,4,5 Done

# Q22
i = 0
while i:
    print(i)
print("Finished")
# output:-  Finished

# Q23
i = 5
while i:
    print(i)
    i -= 2
# output:-  5,3,1

# Q24
i = 1
while i <= 3:
    print(i)
    i += 1
print(i)
# output:- 1,2,3,4

# Q25
i = 1
while i <= 5:
    if i % 2 == 0:
        print(i)
    i += 1
# output:- 2,4

# Q26

# Take n.
# Count how many even numbers are between 1 and n.
n=15
count=0
while n>0:
    if n%2==0:
        count+=1
    n-=1
print(count)
# Q27
# Take n.
# Count how many odd numbers are between 1 and n.
n=15
count=0
while n>0:
    if n%2!=0:
        count+=1
    n-=1
print(count)
# Q28
# Take n.
# Find the sum of all even numbers from 1 to n.
n=15
sum=0
while n>0:
    if n%2==0:
        sum+=n
    n-=1
print(sum)
        
# Q29
# Take n.
# Find the sum of all odd numbers from 1 to n.
n=15
sum=0
while n>0:
    if n%2!=0:
        sum+=n
    n-=1
print(sum)

# Q30
# Take n.
# Print all numbers divisible by 7 from 1 to n.
n=1
while n<50:
    if n%7==0:
        print(n)
    n+=1


# 🚀 Google / Amazon Challenge
# Q31
# Take n.
# Print numbers from 1 to n.
# If divisible by 3, print "Fizz"
# If divisible by 5, print "Buzz"
# If divisible by 3 and 5, print "FizzBuzz"
# Otherwise print the number.
n=1
while n<=20:
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
            print("Fizz")
    elif n%5==0:
            print("Buzz")
    else:
        print(n)
    n+=1