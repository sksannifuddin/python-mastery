# Q1 Create an integer and convert it into a float.
# Print:
# Original value
# Original datatype
# Converted value
# Converted datatype
num=25
num1=float(num)
print(num, type(num))
print(num1, type(num1))

# Q2 Create a float and convert it into an integer.
# Observe what happens to the decimal part.
num=25.5
num1=int(num)
print(num1)

# Q3 Create an integer and convert it into a string.
# Print datatype before and after conversion.
num=25
num1=str(num)
print(num, type(num))
print(num1, type(num1))

# Q4 Create:
# num = "100"
# Convert it into an integer and add 50.
num = "100"
num1=int(num)
num1+=50
print(num1)

# Q5 Create:
# price = "199.99"
# Convert it into a float and add GST of 18%.
price = "199.99"
price=float(price)
gst=18
amount=price+(price*gst)/100
print(amount)
final_price = price * 1.18
print(final_price)

# Q6 Convert:
# True
# False
# into integers.
print(int(True))
print(int(False))

# Q7 Convert:
# 0
# 1
# 100
# into booleans.
print(bool(0))
print(bool(1))
print(bool(100))

# Q8 Convert your age into:
# float
# string
# boolean
# Print all datatypes.
age=20
print(age)
print(type(age))
age=float(20)
print(age)
print(type(age))
age=str(20)
print(age)
print(type(age))
age=bool(20)
print(age)
print(type(age))

# Q9 Create:
# height = "168.5"
# Convert it into float and calculate:
# height + 10
height = "168.5"
height=float(height)
height += 10
print(height)

# Q10 Create:
# quantity = "5"
# price = "250"
# Convert and calculate total bill.
quantity = "5"
quantity=int(quantity)
price = "250"
price=int(price)
total_bill=price*quantity
print(total_bill)



# Q11 
print(int(10.9))
# output:- 10
# Q12
print(float(10))
# output:- 10.0
# Q13
print(str(100))
# output:- 100
# Q14
print(bool(0))
# output:- False
# Q15
print(bool(1))
# output:- True
# Q16
print(bool(""))
# output:- False
# Q17
print(bool("Python"))
# output:- True
# Q18
print(int(True))
# output:- 1
# Q19
print(int(False))
# output:- 0
# Q20
print(float("10.5"))
# output:- 10.5
# Tricky Interview Questions
# Q21
print(bool("False"))
# output:- True
# Q22
print(bool("0"))
# output:- True
# Q23
print(bool([]))
# output:- False
# Q24
print(bool([1]))
# output:- True
# Q25
print(int("10.5"))
# output:- ValueError
# Bonus FAANG Question

# Predict without running:

x = "100"
y = 50

print(int(x) + y)
print(str(y) + x)
# output:- 150 , 50100