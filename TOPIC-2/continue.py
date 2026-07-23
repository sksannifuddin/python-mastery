
# Q1
# Print numbers from 1 to 10.
# Skip printing 5.
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
for i in range(1,11):
    if i==5:
        continue
    print(i)

# Q2
# Print numbers from 1 to 20.
# Skip all even numbers.
for i in range(1,21):
    if i%2==0:
        continue
    print(i)

# Q3
# Print numbers from 1 to 20.
# Skip all odd numbers.
for i in range(1,21):
    if i%2!=0:
        continue
    print(i)

# Q4
# Print numbers from 1 to 50.
# Skip all numbers divisible by 3.
for i in range(1,51):
    if i%3==0:
        continue
    print(i)

# Q5
# Print the multiplication table of 7.
# Skip the 5th multiple.
#
# Expected
# 7 x 1 = 7
# ...
# 7 x 4 = 28
# 7 x 6 = 42
# ...
n=7
for i in range(1,11):
    if i==5:
        continue
    print(f"{n}x{i}={n*i}")

# Q6
# Print numbers from 1 to 100.
# Skip all multiples of 10.
for i in range(1,101):
    if i%10==0:
        continue
    print(i)

# Q7
# Print all alphabets from A to Z.
# Skip vowels.
for i in range(ord("A"),ord("Z")+1):
    if chr(i).lower() in "aeiou" :
        continue
    print(chr(i))
        

# Q8
# Take 10 numbers from the user.
# Skip negative numbers.
# Print only positive numbers.
number=[]
for i in range(1,11):
    num=int(input())
    if num<0:
        continue
    number.append(num)
print(number)
    

# Q9
# Take 10 numbers.
# Find their sum.
# Ignore negative numbers.
total=0
for i in range(1,11):
    num=int(input())
    if num<0:
        continue
    total+=num
print(total)

# Q10
# Print numbers from 1 to 30.
# Skip numbers divisible by both 2 and 3.
for i in range(1,31):
    if i%2==0 and i%3==0:
        continue
    print(i)


# Q11
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# Output:- 1,2,4,5


# Q12
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

# Output:-1,3


# Q13
for i in range(1,6):
    print(i)
    if i == 2:
        continue
    print("Python")

# Output:-1,python,2, 3,python, 4,python, 5,python


# Q14
i = 1

while i <= 5:

    i += 1

    if i == 4:
        continue

    print(i)

# Output:- 2,3,5,6   #important


# Q15
for ch in "PYTHON":

    if ch == "H":
        continue

    print(ch)

# Output:-pyton


# Q16
for i in range(1,6):

    if i == 5:
        continue

    print(i)

print("Done")

# Output:- 1,2,3,4 done


# Q17
for i in range(1,6):

    if i < 3:
        continue

    print(i)

# Output:-3,4,5


# Q18
i = 0

while i < 5:

    i += 1

    if i == 2:
        continue

    print(i)

# Output:- 1,3,4,5


# Q19
for i in range(5):

    if i:
        continue

    print(i)

# Output:- 0 


# Q20
for i in range(1,8):

    if i % 3 == 0:
        continue

    print(i)

# Output:- 1,2,4,5,7


# Q21

for i in range(5):

    if i == 2:
        continue

else:
    print("Done")

# Output:- done 


# Q22

for i in range(5):

    print(i)

    continue

    print("Python")

# Output:- 0,1,2,3,4 


# Q23

i = 0

while i < 5:

    i += 1

    if i == 3:
        continue

    print(i)

else:
    print("Finished")

# Output:- 1,2,4,5  Finished


# Q24

for i in range(3):

    if i == 1:
        continue

    if i == 2:
        continue

    print(i)

# Output:- 0


# Q25

for i in range(1,6):

    if i != 4:
        continue

    print(i)

# Output:- 4


# Q26
# Print numbers from 1 to 100.
# Skip all multiples of both 4 and 6.
for i in range(1,101):
    if i%4==0 and i%6==0:
        continue
    print(i)

# Q27
# Take 10 numbers from the user.
# Ignore all zeros.
# Print the remaining numbers.
number=[]
for i in range(1,11):
    num=int(input())
    if num==0:
        continue
    number.append(num)
print(number)

# Q28
# Take 10 marks.
# Ignore absent students.
# (Absent = -1)
# Find the average of present students only.
total=0
count=0
for i in range(1,11):
    marks=int(input())
    if marks==-1:
        continue
    total+=marks
    count+=1
avg=total/count
print(avg)

# Q29
# Print all numbers from 1 to 100.
# Skip prime numbers.
# Print only composite numbers.
for i in range(1,101):
    prime=True
    if i>1:
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
    if prime:
        continue
    print(i)

# Q30
# Print numbers from 1 to 50.
# Skip numbers divisible by 5 or 7.
for i in range(1,51):
    if i%5==0 or i%7==0:
        continue
    print(i)



# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================

# Q31
# Take 15 integers from the user.
# Ignore:
# • Negative numbers
# • Zero
# Find the sum of only positive numbers.
# Example
# Input
# 5
# -2
# 0
# 10
# -7
# 15
# Output
# 30

total=0
for i in range(1,16):
    num=int(input())
    if num<=0:
        continue
    total+=num
print(total)