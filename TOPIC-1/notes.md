# VARIABLES IN PYTHON – COMPLETE PLACEMENT NOTES

## What is a Variable?

A variable is a name (reference) that points to an object stored in memory.

Example:

```python
x = 10
```

Here:

* x → variable name
* 10 → object/value
* = → assignment operator

Python creates an integer object 10 and x refers to it.

---

## Variables Are References, Not Boxes

Many beginners think:

```python
x = 10
```

means x stores 10.

Technically:

```text
x → reference
10 → object
```

x refers to the object 10.

Example:

```python
x = 10
y = x

print(x)
print(y)
```

Output:

```python
10
10
```

Both variables refer to the same object.

---

## Memory Representation

```python
x = 10
y = x
```

Memory:

```text
x ──► 10
y ──► 10
```

After:

```python
x = 20
```

Memory:

```text
x ──► 20
y ──► 10
```

Output:

```python
print(y)
```

```python
10
```

This is one of the most common interview questions.

---

## Variable Assignment

Assigning a value to a variable.

```python
name = "Sunny"
age = 20
cgpa = 8.5
```

---

## Variable Reassignment

Changing the value of a variable.

```python
x = 10
x = 20
```

Output:

```python
20
```

The old reference is replaced.

---

## Dynamic Typing

Python is dynamically typed.

Meaning:

```python
x = 10
x = "Sunny"
x = True
```

Same variable can refer to different datatypes.

Unlike Java/C++:

```java
int x = 10;
```

Datatype must be declared.

Python does not require datatype declaration.

---

## Strong Typing

Python is dynamically typed but strongly typed.

Example:

```python
"10" + 10
```

Output:

```python
TypeError
```

Python does not automatically convert incompatible types.

---

## Multiple Assignment

Assign multiple variables in one line.

```python
a = b = c = 10
```

Output:

```python
a = 10
b = 10
c = 10
```

---

## Multiple Value Assignment

```python
x, y, z = 1, 2, 3
```

Output:

```python
x = 1
y = 2
z = 3
```

---

## Variable Unpacking

```python
name, age, city = ("Sunny", 20, "Nellore")
```

Output:

```python
Sunny
20
Nellore
```

Very important for Data Science interviews.

---

## Swapping Variables

### Traditional Method

```python
a = 10
b = 20

temp = a
a = b
b = temp
```

---

### Pythonic Method

```python
a = 10
b = 20

a, b = b, a
```

Most asked interview question.

---

## Naming Rules

### Valid

```python
name
student_name
_marks
cgpa2026
```

### Invalid

```python
2name
student-name
for
class
```

Reasons:

* Cannot start with digit
* Cannot contain special characters
* Cannot use keywords

---

## Case Sensitive

```python
name = "Sunny"
Name = "Python"
```

Different variables.

Output:

```python
print(name)
```

```python
Sunny
```

Output:

```python
print(Name)
```

```python
Python
```

---

## Keywords Cannot Be Variable Names

Invalid:

```python
for = 10
```

```python
class = 20
```

Use:

```python
for_count
class_name
```

---

## id() Function

Returns memory identity.

```python
x = 10

print(id(x))
```

Output:

Memory address-like integer.

---

## Important Interview Question

```python
a = 10
b = 10

print(id(a) == id(b))
```

Output:

```python
True
```

Python reuses small integer objects.

This optimization is called:

```text
Integer Interning
```

---

## Variable Scope (Preview)

### Global Variable

```python
x = 10
```

Accessible everywhere.

### Local Variable

```python
def fun():
    x = 20
```

Accessible only inside function.

You will study this later in Functions.

---

## Common Placement Questions

### Q1

```python
x = 10
y = x
x = 20

print(y)
```

Output:

```python
10
```

---

### Q2

```python
a = b = c = 10

b = 20

print(a,b,c)
```

Output:

```python
10 20 10
```

---

### Q3

```python
x, y = 10, 20

x, y = y, x

print(x,y)
```

Output:

```python
20 10
```

---

### Q4

```python
name = "Python"
name = "Java"

print(name)
```

Output:

```python
Java
```

---

### Q5

```python
x = 5

x += 3

x *= 2

print(x)
```

Output:

```python
16
```

---

## One-Line Revision

```text
Variables are references to objects in memory.
Python is dynamically typed and strongly typed.
Assignment creates references.
Reassignment changes references.
Variables do not store values directly.
id() returns object identity.
Python supports multiple assignment and unpacking.
```



--------------------------------------------------------------------------------------------------------------------------

# DATA TYPES IN PYTHON – COMPLETE PLACEMENT NOTES


## What is a Data Type?

A Data Type defines:

* What kind of value is stored
* How much memory is used
* What operations can be performed

Example:

```python
x = 10
```

Python automatically identifies:

```python
type(x)
```

Output:

```python
<class 'int'>
```

---

## Why Data Types Are Important?

Without data types, Python cannot know:

```python
10 + 20
```

Should perform:

```text
Addition
```

or

```python
"10" + "20"
```

Should perform:

```text
Concatenation
```

Data types determine behavior.

---

## Classification of Data Types

## Numeric Types

```python
int
float
complex
bool
```

---

## Sequence Types

```python
str
list
tuple
range
```

---

## Set Types

```python
set
frozenset
```

---

## Mapping Type

```python
dict
```

---

## Special Type

```python
NoneType
```

---

## INTEGER (int)

Stores whole numbers.

Examples:

```python
a = 10
b = -20
c = 5000
```

Valid:

```python
10
0
-50
999999
```

Invalid:

```python
10.5
```

because that is float.

---

## Interview Question

```python
type(10)
```

Output:

```python
<class 'int'>
```

---

## FLOAT

Stores decimal numbers.

Examples:

```python
salary = 55000.50
cgpa = 8.2
```

---

## Interview Question

```python
type(10.0)
```

Output:

```python
<class 'float'>
```

---

## COMPLEX

Used in scientific computing.

Structure:

```python
a + bj
```

Example:

```python
x = 2 + 3j
```

Output:

```python
<class 'complex'>
```

---

## Interview Question

```python
print(type(2+3j))
```

Output:

```python
<class 'complex'>
```

---

## BOOLEAN

Stores:

```python
True
False
```

Internally:

```python
True = 1
False = 0
```

---

## Examples

```python
is_logged_in = True
is_admin = False
```

---

## Interview Questions

```python
True + True
```

Output:

```python
2
```

---

```python
False + 10
```

Output:

```python
10
```

---

## Most Important Interview Question

```python
isinstance(True, int)
```

Output:

```python
True
```

Reason:

```text
bool is a subclass of int
```

---

## STRING

Stores text.

Examples:

```python
name = "Sunny"
college = 'NBKR'
```

---

## String is Immutable

Cannot modify directly.

Example:

```python
name = "Python"

name[0] = "J"
```

Output:

```python
TypeError
```

---

## Interview Question

```python
type("Python")
```

Output:

```python
<class 'str'>
```

---

## LIST

Ordered collection.

Mutable.

Allows duplicates.

Examples:

```python
numbers = [1,2,3]
```

---

## Features

### Ordered

```python
a = [10,20,30]
```

Index exists.

---

### Mutable

```python
a[0] = 100
```

Allowed.

---

### Duplicates Allowed

```python
[1,1,1]
```

Valid.

---

## Interview Question

```python
type([1,2,3])
```

Output:

```python
<class 'list'>
```

---

## TUPLE

Ordered collection.

Immutable.

Duplicates allowed.

Example:

```python
a = (1,2,3)
```

---

## Difference from List

Cannot modify.

```python
a[0] = 100
```

Output:

```python
TypeError
```

---

## Interview Question

```python
type((1,2,3))
```

Output:

```python
<class 'tuple'>
```

---

## SET

Unordered collection.

Unique values only.

Example:

```python
a = {1,2,3}
```

---

## Duplicate Removal

```python
a = {1,1,1,2,2}
```

Output:

```python
{1,2}
```

---

## Interview Trap

```python
a = {}
```

Output:

```python
<class 'dict'>
```

NOT set.

---

Correct:

```python
a = set()
```

Output:

```python
<class 'set'>
```

---

## DICTIONARY

Stores key-value pairs.

Example:

```python
student = {
    "name":"Sunny",
    "age":20
}
```

---

## Features

Mutable.

Keys must be unique.

Values can repeat.

---

## Interview Question

```python
type({})
```

Output:

```python
<class 'dict'>
```

---

## NONE TYPE

Represents absence of value.

Example:

```python
x = None
```

---

## Interview Question

```python
type(None)
```

Output:

```python
<class 'NoneType'>
```

---

## type() Function

Returns datatype.

Example:

```python
print(type(100))
```

Output:

```python
<class 'int'>
```

---

## isinstance()

Checks datatype.

Example:

```python
isinstance(100,int)
```

Output:

```python
True
```

---

## Mutable vs Immutable

## Mutable

Can change after creation.

```python
list
set
dict
```

---

## Immutable

Cannot change after creation.

```python
int
float
bool
str
tuple
complex
```

---

## Memory Concept

```python
a = [1,2]
b = a
```

Memory:

```text
a ──► [1,2]
b ──► [1,2]
```

Both refer to same object.

---

## FAANG Interview Traps

## Trap 1

```python
type(type(10))
```

Output:

```python
<class 'type'>
```

---

## Trap 2

```python
type(None)
```

Output:

```python
<class 'NoneType'>
```

---

## Trap 3

```python
a = {}
```

Output:

```python
<class 'dict'>
```

---

## Trap 4

```python
a = set()
```

Output:

```python
<class 'set'>
```

---

## Trap 5

```python
isinstance(True,int)
```

Output:

```python
True
```

---

## Trap 6

```python
True + True
```

Output:

```python
2
```

---

## Trap 7

```python
False + 100
```

Output:

```python
100
```

---

## Trap 8

```python
bool([])
```

Output:

```python
False
```

---

## Trap 9

```python
bool([1])
```

Output:

```python
True
```

---

## Trap 10

```python
type(2+3j)
```

Output:

```python
<class 'complex'>
```

---


## One-Line Revision

```text
Data Types define how Python stores, manages, and processes data.
int, float, bool, complex → Numeric
str, list, tuple → Sequence
set → Unique collection
dict → Key-value mapping
None → Absence of value
Mutable: list, set, dict
Immutable: int, float, bool, str, tuple, complex
```

--------------------------------------------------------------------------------------------------------------------------


# TYPE CASTING IN PYTHON – COMPLETE PLACEMENT NOTES

## What is Type Casting?

Type Casting means converting a value from one datatype to another datatype.

Example:

```python
age = "20"

age = int(age)

print(age)
```

Output:

```python
20
```

Datatype changed:

```text
str → int
```

---

## Why Type Casting Is Important?

Input from user:

```python
age = input()
```

User enters:

```text
20
```

Python stores:

```python
"20"
```

Datatype:

```python
str
```

To perform calculations:

```python
age = int(input())
```

---

## Types of Type Casting

## 1. Implicit Type Casting

Python automatically converts smaller datatype to larger datatype.

Example:

```python
a = 10
b = 5.5

print(a+b)
```

Output:

```python
15.5
```

Internally:

```text
10 → 10.0
```

Python converts int to float automatically.

---

## 2. Explicit Type Casting

Programmer manually converts datatype.

Example:

```python
x = "100"

x = int(x)
```

---

## int() Function

Converts compatible values into integer.

Example:

```python
int(10.9)
```

Output:

```python
10
```

Decimal part removed.

---

### Examples

```python
int(20.5)
```

Output:

```python
20
```

---

```python
int(True)
```

Output:

```python
1
```

---

```python
int(False)
```

Output:

```python
0
```

---

```python
int("100")
```

Output:

```python
100
```

---

## Most Important Interview Trap

```python
int("10.5")
```

Output:

```python
ValueError
```

Reason:

```text
"10.5" is float string
int() expects integer string
```

Correct:

```python
int(float("10.5"))
```

Output:

```python
10
```

---

## float() Function

Converts values into float.

Example:

```python
float(10)
```

Output:

```python
10.0
```

---

### Examples

```python
float(True)
```

Output:

```python
1.0
```

---

```python
float(False)
```

Output:

```python
0.0
```

---

```python
float("10.5")
```

Output:

```python
10.5
```

---

```python
float("100")
```

Output:

```python
100.0
```

---

## str() Function

Converts value into string.

Example:

```python
str(100)
```

Output:

```python
"100"
```

---

### Examples

```python
str(True)
```

Output:

```python
"True"
```

---

```python
str(10.5)
```

Output:

```python
"10.5"
```

---

## bool() Function

Converts values into boolean.

Output always:

```python
True
False
```

---

## Boolean Conversion Rules

## False Values

Only these become False:

```python
0
0.0
''
[]
{}
set()
None
False
```

Everything else becomes True.

---

## Examples

```python
bool(0)
```

Output:

```python
False
```

---

```python
bool(100)
```

Output:

```python
True
```

---

```python
bool(-1)
```

Output:

```python
True
```

---

```python
bool("")
```

Output:

```python
False
```

---

```python
bool("Python")
```

Output:

```python
True
```

---

## Most Important Interview Traps

## Trap 1

```python
bool("False")
```

Output:

```python
True
```

Reason:

```text
Non-empty string
```

---

## Trap 2

```python
bool("0")
```

Output:

```python
True
```

Reason:

```text
Non-empty string
```

---

## Trap 3

```python
bool(" ")
```

Output:

```python
True
```

Reason:

Space is still a character.

---

## Trap 4

```python
bool("")
```

Output:

```python
False
```

Empty string.

---

## Trap 5

```python
bool([])
```

Output:

```python
False
```

Empty list.

---

## Trap 6

```python
bool([0])
```

Output:

```python
True
```

List is not empty.

---

## Trap 7

```python
bool({})
```

Output:

```python
False
```

Empty dictionary.

---

## Trap 8

```python
bool({"a":1})
```

Output:

```python
True
```

Dictionary is not empty.

---

## Boolean Internals

Python internally treats:

```python
True = 1
False = 0
```

---

## Examples

```python
True + True
```

Output:

```python
2
```

---

```python
True + False
```

Output:

```python
1
```

---

```python
False + 10
```

Output:

```python
10
```

---

## Data Type Conversion Table

| Original | Conversion | Result     |
| -------- | ---------- | ---------- |
| int      | float      | 10 → 10.0  |
| float    | int        | 10.9 → 10  |
| int      | str        | 10 → "10"  |
| str      | int        | "10" → 10  |
| bool     | int        | True → 1   |
| bool     | float      | True → 1.0 |
| int      | bool       | 0 → False  |
| int      | bool       | 100 → True |

---

## Real-World Examples

## User Age

```python
age = int(input("Enter age: "))
```

---

## Product Price

```python
price = float(input("Enter price: "))
```

---

## Quantity

```python
qty = int(input("Enter quantity: "))
```

---

## Bill Calculation

```python
qty = int(input())
price = float(input())

bill = qty * price
```

---

## FAANG Interview Questions

### Q1

```python
print(int(True))
```

Output:

```python
1
```

---

### Q2

```python
print(float(False))
```

Output:

```python
0.0
```

---

### Q3

```python
print(bool("False"))
```

Output:

```python
True
```

---

### Q4

```python
print(bool("0"))
```

Output:

```python
True
```

---

### Q5

```python
print(bool(""))
```

Output:

```python
False
```

---

### Q6

```python
print(bool([]))
```

Output:

```python
False
```

---

### Q7

```python
print(bool([1]))
```

Output:

```python
True
```

---

### Q8

```python
print(int(float("10.9")))
```

Output:

```python
10
```

---

### Q9

```python
print(type(str(100)))
```

Output:

```python
<class 'str'>
```

---

### Q10

```python
print(type(bool(100)))
```

Output:

```python
<class 'bool'>
```

---

## One-Line Revision

```text
Type Casting converts one datatype into another.
Implicit = automatic conversion.
Explicit = manual conversion.
Only empty values become False.
Non-empty strings always become True.
True = 1, False = 0.
int("10.5") gives ValueError.
```

