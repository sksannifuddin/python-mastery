# 📘 OOP — MODULE 2
# PART 1 — Coding Questions
## Encapsulation (Q1–Q10)



## Q1
### Create a class with one public variable.

# Print it using an object.

### Answer


class Student:

    def __init__(self):
        self.name = "Sunny"

s = Student()

print(s.name)




## Q2
### Create a class with one protected variable (`_name`).

# Print it using an object.

### Answer


class Student:

    def __init__(self):
        self._name = "Sunny"

s = Student()

print(s._name)


## Q3
### Create a class with one private variable (`__name`).

# Try printing it directly.

# Observe the error.

### Answer


class Student:

    def __init__(self):
        self.__name = "Sunny"

s = Student()

# print(s.__name)

# AttributeError:
# 'Student' object has no attribute '__name'


## Q4
### Access the private variable using Name Mangling.

### Answer


class Student:

    def __init__(self):
        self.__name = "Sunny"

s = Student()

print(s._Student__name)


## Q5
### Create a getter method to access a private variable.

### Answer


class Student:

    def __init__(self):
        self.__name = "Sunny"

    def get_name(self):
        return self.__name

s = Student()

print(s.get_name())


## Q6
### Create a setter method to modify a private variable.

### Answer


class Student:

    def __init__(self):
        self.__name = "Sunny"

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

s = Student()

s.set_name("Ravi")

print(s.get_name())


## Q7
### Create a BankAccount class.

# Store balance as a private variable.

# Create a getter method.

### Answer


class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def get_balance(self):
        return self.__balance

b = BankAccount()

print(b.get_balance())

## Q8
### Add a `deposit()` method.

# Increase the balance.

### Answer

# ```python
class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

b = BankAccount()

b.deposit(2000)

print(b.get_balance())


## Q9
### Add a `withdraw()` method.

# Reduce the balance only if sufficient balance exists.

### Answer


class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

b = BankAccount()

b.withdraw(3000)

print(b.get_balance())

b.withdraw(5000)


## Q10 — Google Mini Challenge

### Create an Employee class.

# Private Variables:

# - Name
# - Salary

# Create:

# - Getter
# - Setter

# Increase salary by **10%**.

# Print updated salary.

### Answer


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def increment_salary(self):
        self.__salary += self.__salary * 0.10


e = Employee("Sunny", 50000)

print(e.get_name())
print(e.get_salary())

e.increment_salary()

print(e.get_salary())



# 📘 OOP — MODULE 2
# PART 1 — Coding Questions
## Inheritance (Q11–Q20)



## Q11
### Create a Parent class.

# Create a Child class that inherits from Parent.

# Call the Parent method using the Child object.

### Answer


class Parent:

    def display(self):
        print("I am Parent")

class Child(Parent):
    pass

c = Child()

c.display()


## Q12
### Create a Parent class with a constructor.

# Create a Child class.

# Create an object of Child.

# Observe that the Parent constructor is automatically called.

### Answer

class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    pass

c = Child()


## Q13
### Access Parent variables from Child.

### Answer


class Parent:

    def __init__(self):
        self.name = "Sunny"

class Child(Parent):
    pass

c = Child()

print(c.name)


## Q14
### Create Parent and Child constructors.

# Use `super()` to call the Parent constructor.

### Answer


class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child()


## Q15
### Create a Parent method.

# Override it in Child.

# Call the method.

### Answer


class Parent:

    def display(self):
        print("Parent Method")

class Child(Parent):

    def display(self):
        print("Child Method")

c = Child()

c.display()


## Q16
### Call both Parent and Child methods using `super()`.

### Answer


class Parent:

    def display(self):
        print("Parent Method")

class Child(Parent):

    def display(self):
        super().display()
        print("Child Method")

c = Child()

c.display()


## Q17
### Create Multilevel Inheritance.

# A → B → C

# Print all methods.

### Answer

class A:

    def first(self):
        print("Class A")

class B(A):

    def second(self):
        print("Class B")

class C(B):

    def third(self):
        print("Class C")

obj = C()

obj.first()
obj.second()
obj.third()


## Q18
### Create Multiple Inheritance.

### Answer


class Father:

    def father(self):
        print("Father")

class Mother:

    def mother(self):
        print("Mother")

class Child(Father, Mother):
    pass

c = Child()

c.father()
c.mother()


## Q19
### Create Hierarchical Inheritance.

# One Parent

# Two Children

### Answer

class Parent:

    def display(self):
        print("Parent")

class Child1(Parent):

    def first(self):
        print("Child 1")

class Child2(Parent):

    def second(self):
        print("Child 2")

c1 = Child1()
c2 = Child2()

c1.display()
c1.first()

c2.display()
c2.second()


## Q20 — Google Mini Challenge

### Create a Person class.

# Create Student and Teacher classes inheriting from Person.

# Store:

# - Name
# - Age

# Student:

# - Branch

# Teacher:

# - Subject

# Print complete details.

### Answer


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):

    def __init__(self, name, age, branch):
        super().__init__(name, age)
        self.branch = branch

    def display(self):
        print("Student")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Branch :", self.branch)

class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print("Teacher")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Subject :", self.subject)

s = Student("Sunny", 21, "AIDS")
t = Teacher("Ramesh", 40, "Python")

s.display()
print()

t.display()




# 📘 OOP — MODULE 2
# PART 1 — Coding Questions
## Advanced Inheritance (Q21–Q30)



## Q21
### Override the Parent constructor without using `super()`.

# Observe the output.

### Answer


class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):
        print("Child Constructor")

c = Child()


**Output**

```
Child Constructor
```

---

## Q22
### Override the Parent constructor using `super()`.

### Answer

```python
class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child()
```

**Output**

```
Parent Constructor
Child Constructor
```

---

## Q23
### Check whether Child is a subclass of Parent using `issubclass()`.

### Answer

```python
class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))
```

**Output**

```
True
```

---

## Q24
### Check whether an object belongs to Child using `isinstance()`.

### Answer

```python
class Parent:
    pass

class Child(Parent):
    pass

c = Child()

print(isinstance(c, Child))
print(isinstance(c, Parent))
```

**Output**

```
True
True
```

---

## Q25
### Print the Method Resolution Order (MRO).

### Answer

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
```

---

## Q26
### Create Multiple Inheritance.

Print the MRO.

### Answer

```python
class A:

    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

---

## Q27
### Demonstrate Method Resolution Order.

### Answer

```python
class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("B")

class C(A):

    def show(self):
        print("C")

class D(B, C):
    pass

d = D()

d.show()
```

**Output**

```
B
```

---

## Q28
### Create Hybrid Inheritance.

### Answer

```python
class A:

    def first(self):
        print("A")

class B(A):

    def second(self):
        print("B")

class C(A):

    def third(self):
        print("C")

class D(B, C):

    def fourth(self):
        print("D")

obj = D()

obj.first()
obj.second()
obj.third()
obj.fourth()
```

---

## Q29
### Check inheritance using `isinstance()`.

### Answer

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))
print(isinstance(d, Animal))
```

**Output**

```
True
True
```

---

## Q30 — Google Mini Challenge

### Create the following inheritance structure.

```
Person
   │
 ┌───────┐
 │       │
Student Teacher
      │
 AssistantProfessor
```

Print complete details of every object.

### Answer

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch

    def display(self):
        print("Student")
        print(self.name)
        print(self.branch)


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("Teacher")
        print(self.name)
        print(self.subject)


class AssistantProfessor(Teacher):

    def __init__(self, name, subject, experience):
        super().__init__(name, subject)
        self.experience = experience

    def display(self):
        print("Assistant Professor")
        print(self.name)
        print(self.subject)
        print(self.experience)


s = Student("Sunny", "AIDS")
t = Teacher("Ramesh", "Python")
a = AssistantProfessor("Mahesh", "AI", 8)

s.display()
print()

t.display()
print()

a.display()




# 📘 OOP — MODULE 2
# PART 1 — Coding Questions
## Polymorphism (Q31–Q40)

---

## Q31
### Create a Parent class with a method `sound()`.

Override it in Child.

### Answer

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

d = Dog()

d.sound()
```

---

## Q32
### Create two child classes.

Dog → Bark

Cat → Meow

Call both methods.

### Answer

```python
class Animal:

    def sound(self):
        print("Animal")

class Dog(Animal):

    def sound(self):
        print("Bark")

class Cat(Animal):

    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
```

---

## Q33
### Demonstrate Runtime Polymorphism using overriding.

### Answer

```python
class Shape:

    def area(self):
        print("Area")

class Square(Shape):

    def area(self):
        print("Square Area")

class Circle(Shape):

    def area(self):
        print("Circle Area")

s = Square()
c = Circle()

s.area()
c.area()
```

---

## Q34
### Demonstrate Duck Typing.

### Answer

```python
class Dog:

    def speak(self):
        print("Bark")

class Cat:

    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()

d = Dog()
c = Cat()

animal_sound(d)
animal_sound(c)
```

---

## Q35
### Create another Duck Typing example.

### Answer

```python
class Car:

    def start(self):
        print("Car Started")

class Bike:

    def start(self):
        print("Bike Started")

def vehicle(v):
    v.start()

vehicle(Car())
vehicle(Bike())
```

---

## Q36
### Operator Overloading using `__add__()`.

### Answer

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a + b)


## Q37
### Operator Overloading using `__eq__()`.

### Answer


class Student:

    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(90)
s2 = Student(90)

print(s1 == s2)


## Q38
### Simulate Method Overloading in Python using default arguments.

### Answer


class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(10))
print(obj.add(10,20))
print(obj.add(10,20,30))


## Q39
### Simulate Method Overloading using `*args`.

### Answer


class Calculator:

    def add(self, *args):

        total = 0

        for i in args:
            total += i

        return total

obj = Calculator()

print(obj.add(10))
print(obj.add(10,20))
print(obj.add(10,20,30,40))


## Q40 — Google Mini Challenge

### Create a Payment System.

# Classes:

# - Payment
# - CreditCard
# - UPI
# - Cash

# Each class should override `pay()`.

# Use one loop to process all payment methods.

### Answer


class Payment:

    def pay(self):
        print("Payment")

class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):

    def pay(self):
        print("Paid using UPI")

class Cash(Payment):

    def pay(self):
        print("Paid using Cash")

payments = [
    CreditCard(),
    UPI(),
    Cash()
]

for payment in payments:
    payment.pay()



# 📘 OOP — MODULE 2
# PART 1 — Coding Questions
## Abstraction (Q41–Q50)



## Q41
### Create an Abstract Class with one abstract method.

### Answer

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Q42
### Create a Child class that implements the abstract method.

### Answer

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()

d.sound()
```

---

## Q43
### Try creating an object of the Abstract Class.

Observe the error.

### Answer

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# a = Animal()

# TypeError:
# Can't instantiate abstract class Animal
# with abstract method sound
```

---

## Q44
### Create an abstract class Shape.

Create two child classes:

- Circle
- Square

Override the `area()` method.

### Answer

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        print("Area of Circle")


class Square(Shape):

    def area(self):
        print("Area of Square")


c = Circle()
s = Square()

c.area()
s.area()
```

---

## Q45
### Create an abstract class Vehicle.

Implement it using:

- Car
- Bike

### Answer

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")


c = Car()
b = Bike()

c.start()
b.start()
```

---

## Q46
### Create an abstract class Employee.

Methods:

- salary()

Child classes:

- Manager
- Developer

### Answer

```python
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):

    def salary(self):
        print("Manager Salary = 90000")


class Developer(Employee):

    def salary(self):
        print("Developer Salary = 70000")


m = Manager()
d = Developer()

m.salary()
d.salary()
```

---

## Q47
### Create an abstract class Payment.

Child classes:

- UPI
- CreditCard

Override `pay()`.

### Answer

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


u = UPI()
c = CreditCard()

u.pay()
c.pay()


## Q48
### Create an abstract class Account.

# Methods:

# - deposit()
# - withdraw()

# Implement in BankAccount.

### Answer


from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class BankAccount(Account):

    def deposit(self):
        print("Amount Deposited")

    def withdraw(self):
        print("Amount Withdrawn")


b = BankAccount()

b.deposit()
b.withdraw()


## Q49
### Create an abstract class Animal.

# Methods:

# - eat()
# - sleep()

# Implement both in Dog.

### Answer

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):

    def eat(self):
        print("Dog Eats")

    def sleep(self):
        print("Dog Sleeps")


d = Dog()

d.eat()
d.sleep()


## Q50 — Google Mini Challenge

### Design a Banking System.

# Abstract Class:

# **Bank**

# Methods:

# - deposit()
# - withdraw()
# - check_balance()

# Implement:

# - SBI
# - HDFC

# Print complete banking operations.

### Answer


from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SBI(Bank):

    def __init__(self):
        self.balance = 10000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("SBI Balance:", self.balance)


class HDFC(Bank):

    def __init__(self):
        self.balance = 5000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("HDFC Balance:", self.balance)


s = SBI()

s.deposit(2000)
s.withdraw(3000)
s.check_balance()

print()

h = HDFC()

h.deposit(500)
h.withdraw(1000)
h.check_balance()



