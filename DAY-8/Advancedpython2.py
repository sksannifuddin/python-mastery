# 📘 ADVANCED PYTHON — MODULE 2
# (Lambda, map(), filter(), zip(), enumerate(), any(), all(), eval(), exec())
# PART 1 — 30 Coding Questions with Answers

---

## Q1
### Create a lambda function to find the square of a number.

### Answer

```python
square = lambda x: x ** 2

print(square(5))
```

---

## Q2
### Create a lambda function to find the cube.

### Answer

```python
cube = lambda x: x ** 3

print(cube(4))
```

---

## Q3
### Create a lambda function to add two numbers.

### Answer

```python
add = lambda a, b: a + b

print(add(10, 20))
```

---

## Q4
### Create a lambda function to find the largest of two numbers.

### Answer

```python
largest = lambda a, b: a if a > b else b

print(largest(10, 25))
```

---

## Q5
### Create a lambda function to check even or odd.

### Answer

```python
even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even(12))
```

---

## Q6
### Use `map()` to square every number.

### Answer

```python
numbers = [1,2,3,4,5]

result = list(map(lambda x: x**2, numbers))

print(result)
```

---

## Q7
### Use `map()` to convert names into uppercase.

### Answer

```python
names = ["sunny","ravi","ajay"]

result = list(map(str.upper, names))

print(result)
```

---

## Q8
### Use `map()` to calculate string lengths.

### Answer

```python
names = ["Sunny","Ajay","Ravi"]

result = list(map(len, names))

print(result)
```

---

## Q9
### Use `filter()` to get even numbers.

### Answer

```python
numbers = [1,2,3,4,5,6,7,8]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

---

## Q10
### Use `filter()` to get odd numbers.

### Answer

```python
numbers = [1,2,3,4,5,6,7,8]

result = list(filter(lambda x: x % 2 != 0, numbers))

print(result)
```

---

## Q11
### Filter names having length greater than 5.

### Answer

```python
names = ["Sunny","Ravi","Machine","Python"]

result = list(filter(lambda x: len(x) > 5, names))

print(result)
```

---

## Q12
### Use `map()` and `filter()` together.

### Answer

```python
numbers = [1,2,3,4,5,6]

result = list(
    map(
        lambda x: x**2,
        filter(lambda x: x%2==0, numbers)
    )
)

print(result)
```

---

## Q13
### Use `zip()` to combine two lists.

### Answer

```python
names = ["Sunny","Ajay","Ravi"]

marks = [95,88,91]

result = list(zip(names, marks))

print(result)
```

---

## Q14
### Create a dictionary using `zip()`.

### Answer

```python
keys = ["A","B","C"]

values = [10,20,30]

d = dict(zip(keys, values))

print(d)
```

---

## Q15
### Use `enumerate()`.

### Answer

```python
names = ["Sunny","Ajay","Ravi"]

for index, name in enumerate(names):
    print(index, name)
```

---

## Q16
### Start `enumerate()` from 1.

### Answer

```python
names = ["Sunny","Ajay","Ravi"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

---

## Q17
### Demonstrate `any()`.

### Answer

```python
numbers = [0,0,0,5]

print(any(numbers))
```

---

## Q18
### Demonstrate `all()`.

### Answer

```python
numbers = [1,2,3,4]

print(all(numbers))
```

---

## Q19
### Difference between `any()` and `all()`.

### Answer

```python
print(any([0,0,5]))

print(all([1,2,3]))

print(all([1,0,3]))
```

---

## Q20
### Use `eval()`.

### Answer

```python
expression = "10+20*3"

print(eval(expression))
```

---

## Q21
### Use `exec()`.

### Answer

```python
code = """
a = 10
b = 20
print(a+b)
"""

exec(code)
```

---

## Q22
### Create a lambda for sorting.

### Answer

```python
students = [
    ("Sunny",95),
    ("Ajay",80),
    ("Ravi",90)
]

students.sort(key=lambda x:x[1])

print(students)
```

---

## Q23
### Sort descending using lambda.

### Answer

```python
numbers = [5,1,9,2,8]

numbers.sort(key=lambda x:x, reverse=True)

print(numbers)
```

---

## Q24
### Filter positive numbers.

### Answer

```python
numbers = [-2,4,-6,8,10]

result = list(filter(lambda x:x>0, numbers))

print(result)
```

---

## Q25
### Find total using `reduce()`.

### Answer

```python
from functools import reduce

numbers = [1,2,3,4,5]

print(reduce(lambda x,y:x+y, numbers))
```

---

## Q26
### Find product using `reduce()`.

### Answer

```python
from functools import reduce

numbers = [1,2,3,4]

print(reduce(lambda x,y:x*y, numbers))
```

---

## Q27
### Use `zip()` with three lists.

### Answer

```python
names = ["Sunny","Ajay"]

ages = [21,22]

cities = ["Hyderabad","Chennai"]

print(list(zip(names, ages, cities)))
```

---

## Q28
### Create a dictionary using dictionary comprehension.

### Answer

```python
d = {x:x*x for x in range(1,6)}

print(d)
```

---

## Q29
### Create a list using list comprehension.

### Answer

```python
numbers = [x*x for x in range(1,11)]

print(numbers)
```

---

## Q30 — Google/Amazon Challenge

### Student Data Analyzer

Requirements:

- Use lambda
- map()
- filter()
- reduce()
- zip()
- enumerate()
- any()
- all()

Find:

- Squares
- Even numbers
- Total marks
- Student dictionary
- Student ranking
- Check if any student failed
- Check if all students passed

### Answer

```python
from functools import reduce

names = ["Sunny","Ajay","Ravi"]

marks = [95,88,91]

print("Squares")

print(list(map(lambda x:x*x, marks)))

print()

print("Passed Students (>90)")

print(list(filter(lambda x:x>90, marks)))

print()

print("Total")

print(reduce(lambda x,y:x+y, marks))

print()

student = dict(zip(names, marks))

print(student)

print()

print("Ranking")

ranking = sorted(student.items(), key=lambda x:x[1], reverse=True)

for rank, value in enumerate(ranking,1):
    print(rank, value)

print()

print("Any Failed")

print(any(mark<35 for mark in marks))

print()

print("All Passed")

print(all(mark>=35 for mark in marks))
```

---

# ✅ Advanced Python Module 2 Completed

Topics Covered

- ✅ Lambda
- ✅ map()
- ✅ filter()
- ✅ reduce()
- ✅ zip()
- ✅ enumerate()
- ✅ any()
- ✅ all()
- ✅ eval()
- ✅ exec()
- ✅ Dictionary Comprehension
- ✅ List Comprehension
- ✅ Sorting using Lambda
- ✅ Google/Amazon Challenge

---

# 🎉 Python Core Status

You have now completed:

- ✅ Python Basics
- ✅ Strings
- ✅ Lists
- ✅ Tuples
- ✅ Sets
- ✅ Dictionaries
- ✅ Functions
- ✅ OOP
- ✅ File Handling
- ✅ Exception Handling
- ✅ Advanced Python

**Python is now placement-ready.** The next phase in your roadmap is **NumPy**.