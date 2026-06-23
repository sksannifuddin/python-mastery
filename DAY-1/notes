need to learn about what is isinstance


isinstance() is a built-in Python function used to check whether a variable belongs to a particular data type.
isinstance(variable,datatype)


print(type(None))
<class 'NoneType'>

Why?

None is a special object in Python whose type is NoneType.



{}        # Dictionary
set()     # Empty Set





## Bonus Interview Question

```python
a = True

print(type(a))
print(isinstance(a, int))
print(a + 5)
Answers
type(a)
Output:
<class 'bool'>

Reason:
True is of bool datatype.

isinstance(a, int)

Output:
True

Reason:
bool is a subclass of int in Python.

a + 5

Output:
6

Reason:
True is treated as 1.

True + 5 = 1 + 5 = 6

Important Points

True = 1
False = 0

True + True = 2

False + 10 = 10

isinstance(True, int) → True
isinstance(False, int) → True


### One-Line Revision

- `type(True)` → `<class 'bool'>`
- `isinstance(True, int)` → `True`
- `True + 5` → `6`
- `False + 5` → `5`
- `True == 1` → `True`
- `False == 0` → `True`





Good question. This is a very common placement aptitude and coding trick.

When GST is 18%, it means:

100% (original price) + 18% (GST)
= 118%

Now convert 118% to decimal:

118 / 100 = 1.18

So,

Final Price = Original Price × 1.18
Example: ₹200

Method 1:

GST = 18% of 200
    = 36

Final Price = 200 + 36
            = 236

Method 2:

Final Price = 200 × 1.18
            = 236

Same answer ✅

Why 1.18?
GST %	Multiplier
5%	1.05
12%	1.12
18%	1.18
28%	1.28
Interview Trick

Instead of:

price = 200
final_price = price + (price * 18 / 100)

You can write:

price = 200
final_price = price * 1.18

Much shorter and faster.

Reverse Question (FAANG Style)

If the final price is ₹236 including 18% GST, what was the original price?

Original Price = 236 / 1.18
               = 200

This reverse calculation is often asked in aptitude and coding interviews.