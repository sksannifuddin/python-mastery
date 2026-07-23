# 1. Create variables for your name, age, college, branch, and print them.
name="sunny"
age=20
college="N.B.K.R Institute of Science and  Technology"
branch="Artificial Intelligence & Data Science"
print(name)
print(age)
print(college)
print(branch)

# 2. Store two numbers in variables a and b, then print their sum, difference, product, and division.
a=10
b=5
addition=a+b
difference=a-b
multiplication=a*b
division=a/b
print(f"addition:{addition}")
print(f"difference:{difference}")
print(f"multiplication:{multiplication}")
print(f"division:{division}")

# 3. Swap two variables using a third variable.
a=20
b=15
print("Before swapping")
print(f"a:{a}, b:{b}")
c=a
a=b
b=c
print("After swapping")
print(f"a:{a}, b:{b}")

# 4. Swap two variables without using a third variable.
a=10
b=5
print("Before swapping")
print(f"a:{a}, b:{b}")
a,b=b,a
print("After swapping")
print(f"a:{a}, b:{b}")

# 5. Store your first name and last name in two variables and print your full name.
first_name="Sannifuddin"
last_name="Shaik"
print(first_name,last_name)#only variables

# 6. Store marks of 3 subjects in variables and calculate total and average.
python_marks=100
java_marks=75
c_marks=50
total=python_marks+java_marks+c_marks
average=total/3
print(f"Total: {total}")
print(f"Average: {average}")

# 7. Create variables for product name, price, quantity, and calculate total bill.
product="iphone 17 pro max"
price=154000
quantity=3
total_bill=price*quantity
print(f"Total_bill: {total_bill}")

# 8. Store length and width of a rectangle and calculate area.
length=15
breadth=10
area=length*breadth
print(f"Area of a Rectangle: {area}cm²")

# 9. Store radius of a circle and calculate area.
import math
radius=10
area=math.pi*radius**2
print(f"Area of a Circle: {area:.2f}cm²")

# 10. Store principal, rate, and time and calculate simple interest.
principal=50
rate=40
time=60
simple_interest=(principal*rate*time)/100
print(f"simple interest: {simple_interest}")


# 11. What will be the output?
x = 10
y = x
x = 20
print(x)
print(y)
# output:- 20,10
# 12. What will be the output?
a = 5
b = 10
a, b = b, a
print(a, b)
# output:- 10,5
# 13. What will be the output?
x = 100
x = x + 50
x = x - 25
print(x)
# output:- 125
# 14. What will be the output?
a = b = c = 10
b = 20
print(a, b, c)
# output:- 10,20,10
# 15. What will be the output?
x, y, z = 1, 2, 3
x, y = y, x
z = x + y
print(x, y, z)
# output:- 2,1,3
# 16. What will be the output?
name = "Python"
name = "Java"
print(name)
# output:- Java
# 17. What will be the output?
x = 10
print(id(x))
x = 20
print(id(x))
# output:- two different memory addresses
# 18. What will be the output?
a = 10
b = 10
print(id(a) == id(b))
# output:- True
# 19.What will be the output?
x = 5
x += 3
x *= 2
print(x)
# output:- 16
# 20.What will be the output?
a = 10
b = 20
c = a
a = b
b = c
print(a, b)
# output:- 20,10









