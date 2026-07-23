

# Q1
# Print numbers from 1 to 10.
# Do nothing when the number is 5.
# (Use pass)
for i in range(1,11):
    if i==5:
        pass
    print(i)

# Q2
# Print numbers from 1 to 20.
# If the number is even,
# write pass.
# Otherwise print the number.
for i in range(1,21):
    if i%2==0:
        pass
    else:
        print(i)

# Q3
# Print numbers from 1 to 20.
# If the number is divisible by 3,
# use pass.
# Otherwise print the number.
for i in range(1,21):
    if i%3==0:
        pass
    else:
        print(i)

# Q4
# Print all alphabets from A to Z.
# If the alphabet is a vowel,
# use pass.
# Otherwise print the alphabet.
for i in range(ord("A"),ord("Z")+1):
    if chr(i).lower() in "aeiou":
        pass
    else:
        print(chr(i))

# Q5
# Take 10 numbers.
# If the number is negative,
# use pass.
# Otherwise print it.
s=[1,2,3,4,5,6,-7,-8,-9,0]
for num in s:
    if num <0:
        pass
    else:
        print(num)

# Q6
# Print numbers from 1 to 15.
# If the number is divisible by both 2 and 3,
# use pass.
# Otherwise print it.
for i in range(1,16):
    if i%2==0 and i%3==0:
        pass
    else:
        print(i)


# Q7
# Create an empty if block using pass.
# Example
# if True:
#     pass
# print("Python")

if False:
    pass
else:
    print("Python")


# Q8
# Create an empty function named greet().
# Use pass.
def greet():
    pass

# Q9
# Create an empty class named Student.
# Use pass.
class Student:
    pass


# Q10
# Create an infinite while loop.
# Use pass inside the loop.
#
# (Don't run this code.)
while True:
    pass


# Q11
for i in range(5):
    if i == 2:
        pass
    print(i)

# Output:-0,1,2,3,4


# Q12
for i in range(5):

    if i == 3:
        pass

print("Done")

# Output:- done


# Q13
if True:
    pass

print("Python")

# Output:- "Python"


# Q14
if False:
    pass

print("Java")

# Output:-  java


# Q15
for i in range(3):

    pass

print("Finished")

# Output:- Finished


# Q16
i = 1

while i <= 3:

    pass

    print(i)

    i += 1

# Output:- 1,2,3


# Q17
if 10 > 5:

    pass

else:

    print("Hello")

print("Python")

# Output:- Python


# Q18
class Student:

    pass

print("Class Created")

# Output:- Class Created


# Q19
def demo():

    pass

print("Function Ready")

# Output:-Function Ready


# Q20
for ch in "AI":

    pass

print("Done")

# Output:- Done




# Q21

for i in range(5):

    if i == 3:
        pass

    print(i)

else:
    print("Done")

# Output:- 0,1,2,3,4 done


# Q22

if True:

    pass

    print("Google")

# Output:- Google


# Q23

for i in range(3):

    if i == 1:

        pass

    print(i)

# Output:- 0,1,2


# Q24

if []:

    pass

else:

    print("Amazon")

# Output:- Amazon


# Q25

while False:

    pass

print("Microsoft")

# Output:- Microsoft



# Q26
# Create a login system.
# If username is "admin",
# leave the block empty using pass.
# Otherwise print "Invalid User".
username="admin"
user=input("enter the username: ")
if user==username:
    pass
else:
    print("invalid user")

# Q27
# Take a number.
# If it is positive,
# write pass.
# Otherwise print "Negative Number".
n=10
if n>0:
    pass
else:
    print("negative number")

# Q28
# Create a function named calculate_salary().
# Keep it empty using pass.
def calculate_salary():
    pass

# Q29
# Create a class named Employee.
# Keep it empty using pass.
class Employee:
    pass

# Q30
# Create an empty for loop body using pass.
# Print "Loop Finished" after the loop.
for i in range(20):
    pass
print("Loop finished")


# ============================================
# GOOGLE / AMAZON INTERVIEW QUESTION
# ============================================

# Q31
# Which statement is correct?
# A) pass stops the loop.
# B) pass skips the current iteration.
# C) pass does nothing. It is simply a placeholder.
# D) pass exits the program.
# Explain why.
# c- the pass do nothing it is used as a place holder where there is no any function do it there 