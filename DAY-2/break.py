# Q1 Print numbers from 1 to 10.
# Stop printing when the number becomes 5.
# Expected Output:
# 1
# 2
# 3
# 4
# 5
for i in range(1,11):
    print(i)
    if i == 5:
        break
# Q2 Print numbers from 10 to 1.
# Stop when the number becomes 6.
for i in range(10,1,-1):
    print(i)
    if i == 6:
        break

# Q3 Print numbers from 1 to 100.
# Stop when you reach the first number divisible by 13.
for i in range(1,101):
    print(i)
    if i%13==0:
        break
        
# Q4 Take a number n.
# Print its multiplication table.
# Stop after printing the 5th multiple.
# Example (n = 7)

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
n=10
for i in range(1,n+1):
    print(f"{n}x{i}={n*i}")
    if i==5:
        break

# Q5 Print numbers from 1 onwards.
# Stop when the number becomes 20.
# Use a while loop.
i=1
while i:
    print(i)
    if i==20:
        break
    i+=1
# Q6 Take a password from the user repeatedly.
# Correct password:
# python123
# Keep asking until the correct password is entered.
# Then print:
# Login Successful
correct_password="python123"
while True:
    password=input("enter the password: ")
    if password==correct_password:
        print("Login Successful")
        break
    else:
       print("wrong password! Try again")
    

# Q7 Take integers from the user.
# Stop when the user enters:
# 0
# Print:
# Input Stopped
while True:
    num=int(input("enter the numbers"))
    if num==0:
        print("Input Stopped")
        break
    print(num)

# Q8 Take numbers from the user.
#Find their sum.
# Stop when the user enters:
# -1
# Print the final sum.
sum=0
while True:
    num=int(input("enter the numbers"))
    if num==-1:
        break
    sum+=num
print(sum)


# Q9
# Print numbers from 1 to 100.
# Stop when you encounter the first multiple of 17.
for i in range(1,101):
    print(i)
    if i%17==0:
        break


# Q10
# Print the alphabet from A to Z.
# Stop after printing M.
# (Hint: use chr() and range().)
for i in range(ord("A"),ord("Z")+1):
    print(chr(i))
    if ord("M")==i:
        break
    
# Q11
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# output:- 1,2,3,4

# Q12
for i in range(10):
    print(i)
    if i == 3:
        break
# output:- 0,1,2,3

# Q13
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
# output:- 1,2,3

# Q14
i = 5
while i > 0:
    if i == 2:
        break
    print(i)
    i -= 1
# output:-5,4,3

# Q15
for i in range(1, 6):
    if i == 1:
        break
    print(i)
# output:- no output

# Q16
for i in range(1, 6):
    print(i)
    if i == 5:
        break
print("Done")
# output:- 1,2,3,4,5 done

# Q17
i = 1
while True:
    print(i)
    if i == 4:
        break
    i += 1
# output:- 1,2,3,4

# Q18
for i in range(5):
    if i == 2:
        break
    print(i)
print("End")
# output:- 0,1 end

# Q19
i = 10
while i:
    if i == 7:
        break
    print(i)
    i -= 1
# output:- 10,9,8

# Q20
for ch in "PYTHON":
    if ch == "H":
        break
    print(ch)
# output:- p y,t



# Q21
for i in range(5):
    if i == 2:
        break
else:
    print("Done") #important
# output:-  no output

# Q22
for i in range(5):
    print(i)
else:
    print("Done")
# output:- 0,1,2,3,4 done

# Q23
i = 1
while True:
    if i == 3:
        break
    print(i)
    i += 1
print("Finished")
# output:- 1,2 Finished

# Q24
while True:
    print("Python")
    break
print("Done")
# output:- Python  Done

# Q25
for i in range(1, 100):
    if i % 9 == 0:
        break
    print(i)
# output:- 1,2,3,4,5,6,7,8

# Q26
# Print numbers from 1 to 100.
# Stop at the first multiple of 11.
for i in range(1,101):
    if i%11==0:
        break
    print(i)
    
# Q27
# Take numbers from the user.
# Stop when a negative number is entered.
while True:
    num=int(input("enter the number"))
    if num<0:
        break
    print(num)
    
# Q28
# Keep asking the user for a PIN.
# Correct PIN:
# 1234
# Stop when the correct PIN is entered.
correct_pin=1234
while True:
    pin=int(input("enter the pin"))
    if pin==correct_pin:
        break
    else:
        print("wrong pin! try again")
        
# Q29
# Print numbers from 1 to 50.
# Stop when you reach the first number divisible by both 4 and 6.
for i in range(1,51):
    if i%4==0 and i%6==0:
        break
    print(i)
    
# Q30
# Take integers from the user.
# Keep adding them.
# Stop when the total becomes 100 or more.
# Print the final total.
total=0
while True:
    num=int(input("enter a number"))
    total+=num
    if total>=100:
        break
print(total)

# 🚀 Google / Amazon Challenge
# Q31
# Take numbers continuously from the user.
# Stop when the user enters the same number twice in a row.
# Example:
# Input:
# 5
# 8
# 10
# 10
# Output:
# Duplicate Found
nums=None
while True:
    num=int(input("enter the numbers"))
    print(num)
    if num==nums:
        break
    nums=num
print("Duplicate Found")