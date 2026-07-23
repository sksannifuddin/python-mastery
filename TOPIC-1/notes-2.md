# INPUT / OUTPUT IN PYTHON – COMPLETE PLACEMENT NOTES

## What is Input?

Input means accepting data from the user during program execution.

Example:

```python
name = input("Enter your name: ")
```

User enters:

```text
Sunny
```

Stored as:

```python
"Sunny"
```

---

## What is Output?

Output means displaying information to the user.

Example:

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

## Why Input and Output Are Important?

Without Input and Output:

```text
No User Interaction
No Data Collection
No Result Display
```

Every real-world application uses Input and Output.

Examples:

```text
ATM Machine
Banking Application
Amazon Website
Food Delivery App
Machine Learning Projects
```

---

## input() Function

Used to take input from the user.

Syntax:

```python
variable = input()
```

Example:

```python
name = input("Enter Name: ")
```

---

## Internal Working of input()

When Python executes:

```python
name = input()
```

Steps:

```text
1. Program waits for input.
2. User enters value.
3. Python receives value as text.
4. String object is created.
5. Variable references that object.
```

Memory:

```text
name ───► "Sunny"
```

---

## Most Important Rule

## input() Always Returns String

Example:

```python
age = input()
```

User enters:

```text
20
```

Datatype:

```python
type(age)
```

Output:

```python
<class 'str'>
```

---

## Why input() Returns String?

Python cannot determine whether:

```text
20
```

should become:

```python
int
float
str
```

Therefore Python safely stores all input as string.

---

## Taking Integer Input

Example:

```python
age = int(input())
```

Input:

```text
20
```

Datatype:

```python
<class 'int'>
```

---

## Taking Float Input

Example:

```python
salary = float(input())
```

Input:

```text
50000.50
```

Datatype:

```python
<class 'float'>
```

---

## Taking Multiple Inputs

## Method 1

```python
a = int(input())
b = int(input())
```

---

## Method 2 (Interview Favorite)

```python
a,b = map(int,input().split())
```

Input:

```text
10 20
```

Output:

```python
a = 10
b = 20
```

---

## print() Function

Used to display output.

Example:

```python
print("Python")
```

Output:

```text
Python
```

---

## Printing Multiple Values

Example:

```python
name = "Sunny"
age = 20

print(name, age)
```

Output:

```text
Sunny 20
```

---

## sep Parameter

Used to change separator between values.

Example:

```python
print("A","B")
```

Output:

```text
A B
```

Custom Separator:

```python
print("A","B",sep="-")
```

Output:

```text
A-B
```

---

## end Parameter

Used to change line ending.

Default:

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

Custom:

```python
print("Hello",end=" ")
print("World")
```

Output:

```text
Hello World
```

---

## f-Strings

Modern way of formatting strings.

Example:

```python
name = "Sunny"

print(f"Hello {name}")
```

Output:

```text
Hello Sunny
```

---

## Multiple Variables with f-Strings

```python
name = "Sunny"
age = 20

print(f"My name is {name} and I am {age} years old")
```

Output:

```text
My name is Sunny and I am 20 years old
```

---

## Number Formatting

Example:

```python
pi = 3.14159265

print(f"{pi:.2f}")
```

Output:

```text
3.14
```

---

## String Concatenation vs Addition

## String Concatenation

```python
a = "10"
b = "20"

print(a+b)
```

Output:

```text
1020
```

---

## Numeric Addition

```python
a = 10
b = 20

print(a+b)
```

Output:

```text
30
```

---

## Memory Concept

Example:

```python
x = input()
```

User enters:

```text
100
```

Memory:

```text
x ───► "100"
```

Python stores user input as a string object.

---

## Common Mistakes

## Mistake 1

```python
age = input()

print(age + 10)
```

Output:

```python
TypeError
```

Reason:

```text
str + int is not allowed
```

---

## Mistake 2

```python
num = input()

print(num * 3)
```

Input:

```text
5
```

Output:

```text
555
```

String repetition occurs.

---

## Mistake 3

```python
a = input()
b = input()

print(a+b)
```

Input:

```text
10
20
```

Output:

```text
1020
```

Because both are strings.

---

## FAANG Interview Traps

## Trap 1

```python
num = input()

print(num + num)
```

Input:

```text
10
```

Output:

```text
1010
```

---

## Trap 2

```python
num = int(input())

print(num + num)
```

Input:

```text
10
```

Output:

```text
20
```

---

## Trap 3

```python
x = input()

print(bool(x))
```

Input:

```text
0
```

Output:

```python
True
```

Reason:

```text
"0" is a non-empty string
```

---

## Trap 4

```python
x = input()

print(type(x))
```

Input:

```text
True
```

Output:

```python
<class 'str'>
```

---

## Trap 5

```python
x = input()

print(x * 3)
```

Input:

```text
5
```

Output:

```text
555
```

---

## Real World Examples

## User Registration

```python
name = input("Enter Name: ")
age = int(input("Enter Age: "))
```

---

## Product Billing

```python
price = float(input())
quantity = int(input())

bill = price * quantity
```

---

## Student Marks

```python
marks = float(input())

print(marks)
```



---

## One-Line Revision

```text
input() always returns string.
Use int() or float() for numerical calculations.
print() displays output.
f-strings are preferred for formatting.
sep changes separator.
end changes line ending.
map() and split() help take multiple inputs.
```


--------------------------------------------------------------------------------------------------------------------------


# OPERATORS IN PYTHON – COMPLETE PLACEMENT NOTES

## What are Operators?

Operators are special symbols used to perform operations on variables and values.

Example:

```python
a = 10
b = 20

print(a+b)
```

Output:

```text
30
```

---

## Why Operators Are Important?

Operators are used in:

```text
Calculations
Decision Making
Conditions
Loops
Data Processing
Machine Learning Algorithms
```

Without operators, programs cannot perform computations.

---

## Classification of Operators

Python operators are divided into:

```text
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
```

---

## ARITHMETIC OPERATORS

## What are Arithmetic Operators?

Used to perform mathematical calculations.

| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| //       | Floor Division |
| %        | Modulus        |
| **       | Exponent       |

---

## Addition (+)

```python
a = 10
b = 20

print(a+b)
```

Output:

```text
30
```

---

## Subtraction (-)

```python
print(20-5)
```

Output:

```text
15
```

---

## Multiplication (*)

```python
print(10*5)
```

Output:

```text
50
```

---

## Division (/)

```python
print(10/2)
```

Output:

```text
5.0
```

Division always returns float.

---

## Floor Division (//)

Returns only integer part.

```python
print(10//3)
```

Output:

```text
3
```

---

## Modulus (%)

Returns remainder.

```python
print(10%3)
```

Output:

```text
1
```

---

## Exponent (**)

Used for powers.

```python
print(2**3)
```

Output:

```text
8
```

---

## Arithmetic Operator Memory Concept

```python
a = 10
b = 5

c = a+b
```

Memory:

```text
a ───► 10
b ───► 5
c ───► 15
```

---

## ASSIGNMENT OPERATORS

## What are Assignment Operators?

Used to assign values.

---

## Basic Assignment

```python
x = 10
```

---

## Add Assignment

```python
x = 10

x += 5
```

Equivalent:

```python
x = x + 5
```

Output:

```text
15
```

---

## Subtract Assignment

```python
x -= 3
```

---

## Multiply Assignment

```python
x *= 2
```

---

## Divide Assignment

```python
x /= 2
```

---

## Modulus Assignment

```python
x %= 3
```

---

## COMPARISON OPERATORS

## What are Comparison Operators?

Used to compare values.

Result:

```text
True
False
```

---

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal                 |
| !=       | Not Equal             |
| >        | Greater Than          |
| <        | Less Than             |
| >=       | Greater Than or Equal |
| <=       | Less Than or Equal    |

---

## Equal To (==)

```python
print(10 == 10)
```

Output:

```text
True
```

---

## Not Equal To (!=)

```python
print(10 != 5)
```

Output:

```text
True
```

---

## Greater Than (>)

```python
print(10 > 5)
```

Output:

```text
True
```

---

## Less Than (<)

```python
print(10 < 5)
```

Output:

```text
False
```

---

## LOGICAL OPERATORS

## What are Logical Operators?

Used to combine conditions.

---

## AND Operator

Returns True only if both conditions are True.

```python
print(True and True)
```

Output:

```text
True
```

---

```python
print(True and False)
```

Output:

```text
False
```

---

## OR Operator

Returns True if at least one condition is True.

```python
print(True or False)
```

Output:

```text
True
```

---

## NOT Operator

Reverses the result.

```python
print(not True)
```

Output:

```text
False
```

---

## IDENTITY OPERATORS

## What are Identity Operators?

Used to compare memory locations.

Operators:

```text
is
is not
```

---

## is Operator

```python
a = [1,2,3]
b = a

print(a is b)
```

Output:

```text
True
```

Same memory location.

---

## is not Operator

```python
a = [1,2,3]
b = [1,2,3]

print(a is not b)
```

Output:

```text
True
```

Different memory locations.

---

## == vs is

### == compares values

```python
a = [1,2,3]
b = [1,2,3]

print(a == b)
```

Output:

```text
True
```

---

### is compares memory location

```python
print(a is b)
```

Output:

```text
False
```

---

## MEMBERSHIP OPERATORS

## What are Membership Operators?

Used to check membership.

Operators:

```text
in
not in
```

---

## in Operator

```python
languages = ["Python","Java","C"]

print("Python" in languages)
```

Output:

```text
True
```

---

## not in Operator

```python
print("Go" not in languages)
```

Output:

```text
True
```

---

## OPERATOR PRECEDENCE

## What is Operator Precedence?

Determines execution order.

Priority:

```text
()
**
*, /, //, %
+, -
Comparison
not
and
or
```

---

## Example

```python
print(10 + 5 * 2)
```

Output:

```text
20
```

Reason:

```text
5*2 = 10
10+10 = 20
```

---

## Example

```python
print((10+5)*2)
```

Output:

```text
30
```

---

## SHORT CIRCUIT EVALUATION

## AND Short Circuit

```python
print(False and 10/0)
```

Output:

```text
False
```

No error.

Reason:

```text
First condition already False.
```

---

## OR Short Circuit

```python
print(True or 10/0)
```

Output:

```text
True
```

No error.

---

## COMMON MISTAKES

## Mistake 1

```python
print(10 = 10)
```

Invalid.

Use:

```python
print(10 == 10)
```

---

## Mistake 2

Confusing:

```python
==
```

with

```python
=
```

---

## Mistake 3

Confusing:

```python
is
```

with

```python
==
```

---

## FAANG INTERVIEW TRAPS

## Trap 1

```python
print(10 + 5 * 2)
```

Output:

```text
20
```

---

## Trap 2

```python
print(2 ** 3 ** 2)
```

Output:

```text
512
```

Reason:

```text
Exponent evaluates Right to Left.
```

---

## Trap 3

```python
print(True + True)
```

Output:

```text
2
```

---

## Trap 4

```python
print(False + 10)
```

Output:

```text
10
```

---

## Trap 5

```python
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

---

## Trap 6

```python
print(True and False or True)
```

Output:

```text
True
```

---

## Trap 7

```python
print(not True and False)
```

Output:

```text
False
```

---

## REAL WORLD EXAMPLES

## Login System

```python
username == "admin"
password == "123"
```

Uses comparison operators.

---

## Age Verification

```python
age >= 18
```

Uses comparison operator.

---

## Product Search

```python
"iPhone" in products
```

Uses membership operator.

---

## Bank Balance Check

```python
balance > withdrawal_amount
```

Uses comparison operator.

---



---

## ONE-LINE REVISION

```text
Arithmetic → Calculations
Assignment → Assign Values
Comparison → True/False Results
Logical → Combine Conditions
Identity → Compare Memory
Membership → Check Presence
Operator Precedence Controls Execution Order
== Compares Values
is Compares Memory Locations
```
