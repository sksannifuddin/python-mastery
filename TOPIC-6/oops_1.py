

# # 📘 OOP — MODULE 1
# # PART 1 — Coding Questions (Q21–Q25)

# # Q21
# # Use delattr().

# # Delete the attribute age.

# # Print the remaining attributes.

# class Student:

#     def __init__(self):
#         self.name = "Sunny"
#         self.age = 21
#         self.college = "NBKR"

# s1 = Student()

# delattr(s1, "age")

# print(s1.name)
# print(s1.college)

# # print(s1.age)
# # AttributeError: 'Student' object has no attribute 'age'


# Q22
# Create a class variable.

# Print it using:

# Class name
# Object
# Answer
# class Student:

#     college = "NBKR"

# s1 = Student()

# print(Student.college)
# print(s1.college)

# Output

# NBKR
# NBKR
# Q23
# Create both:
# Class Variable
# Instance Variable

# Print both.

# Answer
# class Student:

#     college = "NBKR"      # Class Variable

#     def __init__(self, name, age):
#         self.name = name      # Instance Variable
#         self.age = age        # Instance Variable

# s1 = Student("Sunny", 21)

# print(Student.college)
# print(s1.college)

# print(s1.name)
# print(s1.age)
# Q24
# Count how many Student objects are created using a class variable.
# Answer
# class Student:

#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# s1 = Student("Sunny")
# s2 = Student("Ravi")
# s3 = Student("Ajay")
# s4 = Student("Sonia")

# print("Total Objects:", Student.count)

# Output

# Total Objects: 4
# Q25 — Google Mini Challenge
# Create a Student class.

# Store:

# Name
# Roll No
# Branch
# Marks

# Create three students.

# Print:

# Student Details
# Total Marks
# Average
# Highest Marks
# Lowest Marks

# Without using

# sum()
# max()
# min()
# Answer
# class Student:

#     def __init__(self, name, roll, branch, marks):
#         self.name = name
#         self.roll = roll
#         self.branch = branch
#         self.marks = marks

#     def report(self):

#         total = 0
#         highest = self.marks[0]
#         lowest = self.marks[0]

#         for mark in self.marks:
#             total += mark

#             if mark > highest:
#                 highest = mark

#             if mark < lowest:
#                 lowest = mark

#         average = total / len(self.marks)

#         print("Name      :", self.name)
#         print("Roll No   :", self.roll)
#         print("Branch    :", self.branch)
#         print("Marks     :", self.marks)
#         print("Total     :", total)
#         print("Average   :", average)
#         print("Highest   :", highest)
#         print("Lowest    :", lowest)
#         print("-" * 30)


# s1 = Student("Sunny", 101, "AIDS", [90, 80, 95, 100, 85])
# s2 = Student("Ravi", 102, "CSE", [75, 82, 91, 70, 88])
# s3 = Student("Ajay", 103, "ECE", [60, 72, 68, 80, 75])

# s1.report()
# s2.report()
# s3.report()

# 📘 PART 2 — Output Prediction (Q26–Q30)
# Q26
# class Student:
#     pass

# s = Student()

# print(type(s))
# Output
# <class '__main__.Student'>
# Q27
# class Student:

#     def display(self):
#         print("Hello")

# s = Student()

# s.display()
# Output
# Hello
# Q28
# class Student:

#     college = "NBKR"

# s = Student()

# print(s.college)
# Output
# NBKR
# Q29
# class Student:
#     pass

# s = Student()

# s.name = "Sunny"

# print(hasattr(s, "name"))
# Output
# True
# Q30
# class Student:
#     pass

# s = Student()

# print(hasattr(s, "age"))
# Output
# False


# 📘 OOP — MODULE 1
# PART 2 — Output Prediction (Q31–Q35)
# Q31
# class Student:
#     pass

# s = Student()

# setattr(s, "age", 21)

# print(s.age)
# Output
# 21
# Explanation

# setattr() creates a new attribute named age and assigns the value 21.

# Q32
# class Student:
#     pass

# s = Student()

# setattr(s, "age", 21)

# delattr(s, "age")

# print(hasattr(s, "age"))
# Output
# False
# Explanation
# setattr() creates the attribute.
# delattr() deletes it.
# hasattr() returns False.
# Q33
# class Student:

#     def __init__(self):
#         print("Constructor Called")

# s = Student()
# Output
# Constructor Called
# Explanation

# __init__() is automatically called whenever an object is created.

# Q34
# class Student:

#     def __init__(self, name):
#         self.name = name

# s = Student("Sunny")

# print(s.name)
# Output
# Sunny
# Q35
# class Student:

#     college = "NBKR"

# print(Student.college)
# Output
# NBKR
# 📘 PART 3 — Placement / Interview Questions (Q36–Q40)
# Q36
# What is a Class?
# Answer

# A Class is a blueprint (template) used to create objects.

# It defines:

# Variables (Attributes)
# Functions (Methods)
# Example
# class Student:
#     pass

# Real World Example

# Blueprint of a House → Class
# Built House → Object
# Q37
# What is an Object?
# Answer

# An Object is an instance of a class.

# It stores actual data and can use the methods of the class.

# Example
# class Student:
#     pass

# s1 = Student()

# Here,

# Student → Class
# s1 → Object
# Q38
# Difference between Class Variable and Instance Variable
# Class Variable	Instance Variable
# Shared by all objects	Different for each object
# Defined inside class	Defined using self
# One copy	Separate copy for every object
# Example
# class Student:

#     college = "NBKR"

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Sunny")
# s2 = Student("Ravi")

# print(Student.college)

# print(s1.name)
# print(s2.name)
# Q39
# Difference between __init__() and a Normal Method
# Constructor	Normal Method
# Runs automatically	Called manually
# Initializes object	Performs a task
# Executes once per object	Can execute many times
# Example
# class Student:

#     def __init__(self):
#         print("Constructor")

#     def display(self):
#         print("Display Method")

# s = Student()

# s.display()

# Output

# Constructor
# Display Method
# Q40
# Why is self required?
# Answer

# self refers to the current object.

# It allows Python to know which object's variables and methods are being used.

# Without self, Python cannot access instance variables.

# Example
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(self.name)

# s = Student("Sunny")

# s.display()

# Output

# Sunny



# 📘 OOP — MODULE 1
# PART 3 — Placement Questions (Q41–Q45)
# Q41
# Difference between type() and isinstance()
# Answer

# type() tells the exact type of an object.

# isinstance() checks whether an object belongs to a class or any parent class.

# class Student:
#     pass

# s = Student()

# print(type(s))
# print(isinstance(s, Student))
# Output
# <class '__main__.Student'>
# True
# Main difference
# type(s) == Student

# checks the exact class.

# isinstance(s, Student)

# also works with inheritance.

# Q42
# Difference between hasattr(), getattr(), setattr(), and delattr()
# Answer
# hasattr() checks whether an attribute exists.
# getattr() gets an attribute value.
# setattr() creates or updates an attribute.
# delattr() deletes an attribute.
# class Student:
#     pass

# s = Student()

# setattr(s, "name", "Sunny")
# setattr(s, "age", 21)

# print(hasattr(s, "name"))
# print(getattr(s, "name"))

# setattr(s, "age", 25)
# print(s.age)

# delattr(s, "age")
# print(hasattr(s, "age"))
# Output
# True
# Sunny
# 25
# False
# Q43
# Can we create an object without writing a constructor?
# Answer

# Yes.

# If we do not write __init__(), Python provides a default constructor automatically.

# class Student:
#     pass

# s = Student()

# print(s)

# The object is created successfully even without a user-defined constructor.

# Q44
# What happens if we do not use self inside an instance method?
# Answer

# Python automatically sends the current object as the first argument when an instance method is called.

# If the method does not accept self, Python raises a TypeError.

# class Student:

#     def display():
#         print("Hello")

# s = Student()

# # s.display()
# # TypeError:
# # display() takes 0 positional arguments but 1 was given

# Correct version:

# class Student:

#     def display(self):
#         print("Hello")

# s = Student()
# s.display()
# Q45
# Difference between Class and Object with a real-world example
# Answer

# A class is a blueprint.

# An object is an actual instance created from that blueprint.

# Real-world example
# Car is a class.
# BMW, Audi, and Tesla are objects.
# class Car:
#     pass

# car1 = Car()
# car2 = Car()
# car3 = Car()

# car1.name = "BMW"
# car2.name = "Audi"
# car3.name = "Tesla"

# print(car1.name)
# print(car2.name)
# print(car3.name)
# 📘 PART 4 — Google / Amazon Challenges (Q46–Q50)
# Q46
# Employee Salary Analyzer

# Create an Employee class.

# Store:

# ID
# Name
# Salary

# Create five employees.

# Find:

# Highest salary
# Lowest salary
# Average salary

# without using sum(), max(), or min().

# class Employee:

#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary


# employees = [
#     Employee(101, "Sunny", 50000),
#     Employee(102, "Ravi", 65000),
#     Employee(103, "Ajay", 45000),
#     Employee(104, "Sonia", 80000),
#     Employee(105, "Mahesh", 70000)
# ]

# highest = employees[0]
# lowest = employees[0]
# total = 0
# count = 0

# for employee in employees:
#     total += employee.salary
#     count += 1

#     if employee.salary > highest.salary:
#         highest = employee

#     if employee.salary < lowest.salary:
#         lowest = employee

# average = total / count

# print("Highest Salary:")
# print(highest.emp_id, highest.name, highest.salary)

# print("Lowest Salary:")
# print(lowest.emp_id, lowest.name, lowest.salary)

# print("Average Salary:", average)
# Q47
# Bank Account System

# Create a BankAccount class.

# Store:

# Name
# Balance

# Implement:

# Deposit
# Withdraw
# Check balance
# class BankAccount:

#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposited:", amount)
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid withdrawal amount")
#         elif amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print("Withdrawn:", amount)

#     def check_balance(self):
#         print("Account Holder:", self.name)
#         print("Current Balance:", self.balance)


# account = BankAccount("Sunny", 10000)

# account.check_balance()
# account.deposit(5000)
# account.withdraw(3000)
# account.withdraw(20000)
# account.check_balance()
# Q48
# Car Price Analyzer

# Create a Car class.

# Store:

# Brand
# Model
# Price

# Create four cars.

# Find:

# Most expensive car
# Cheapest car
# class Car:

#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price


# cars = [
#     Car("BMW", "X5", 9000000),
#     Car("Audi", "Q7", 8500000),
#     Car("Tesla", "Model 3", 6000000),
#     Car("Toyota", "Fortuner", 4500000)
# ]

# expensive = cars[0]
# cheapest = cars[0]

# for car in cars:
#     if car.price > expensive.price:
#         expensive = car

#     if car.price < cheapest.price:
#         cheapest = car

# print("Most Expensive:")
# print(expensive.brand, expensive.model, expensive.price)

# print("Cheapest:")
# print(cheapest.brand, cheapest.model, cheapest.price)
# Q49
# College Student Filter

# Create a College class.

# Store:

# Student name
# Branch
# CGPA

# Print students whose CGPA is greater than 8.5.

# class College:

#     def __init__(self, name, branch, cgpa):
#         self.name = name
#         self.branch = branch
#         self.cgpa = cgpa


# students = [
#     College("Sunny", "AIDS", 9.1),
#     College("Ravi", "CSE", 8.2),
#     College("Ajay", "ECE", 8.8),
#     College("Sonia", "AIDS", 9.4)
# ]

# for student in students:
#     if student.cgpa > 8.5:
#         print(student.name, student.branch, student.cgpa)
# # Q50
# # Student Management System

# # Create a Student class.

# # Store:

# # Name
# # Roll number
# # Branch
# # Five subject marks

# # For every student, calculate:

# # Total
# # Average
# # Highest mark
# # Lowest mark
# # Pass or fail
# # Grade

# # Do not use sum(), max(), or min().

# class Student:

#     def __init__(self, name, roll_no, branch, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.branch = branch
#         self.marks = marks

#     def calculate_report(self):
#         total = 0
#         count = 0
#         highest = self.marks[0]
#         lowest = self.marks[0]
#         failed = False

#         for mark in self.marks:
#             total += mark
#             count += 1

#             if mark > highest:
#                 highest = mark

#             if mark < lowest:
#                 lowest = mark

#             if mark < 35:
#                 failed = True

#         average = total / count

#         if failed:
#             result = "Fail"
#         else:
#             result = "Pass"

#         if failed:
#             grade = "F"
#         elif average >= 90:
#             grade = "A+"
#         elif average >= 80:
#             grade = "A"
#         elif average >= 70:
#             grade = "B"
#         elif average >= 60:
#             grade = "C"
#         elif average >= 35:
#             grade = "D"
#         else:
#             grade = "F"

#         return total, average, highest, lowest, result, grade

#     def display_report(self):
#         total, average, highest, lowest, result, grade = (
#             self.calculate_report()
#         )

#         print("Name       :", self.name)
#         print("Roll No    :", self.roll_no)
#         print("Branch     :", self.branch)
#         print("Marks      :", self.marks)
#         print("Total      :", total)
#         print("Average    :", average)
#         print("Highest    :", highest)
#         print("Lowest     :", lowest)
#         print("Result     :", result)
#         print("Grade      :", grade)
#         print("-" * 35)


# students = [
#     Student("Sunny", 101, "AIDS", [90, 85, 95, 88, 92]),
#     Student("Ravi", 102, "CSE", [75, 65, 80, 70, 72]),
#     Student("Ajay", 103, "ECE", [60, 32, 70, 55, 68])
# ]

# for student in students:
#     student.display_report()