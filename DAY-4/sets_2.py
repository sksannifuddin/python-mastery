# SETS — MODULE 2
# (Union, Intersection, Difference, Symmetric Difference, Subset, Superset, Disjoint, Frozen Set)
# PART 1 — Coding Questions
# Q1

# Create two sets:

# a={10,20,30}
# b={30,40,50}


# Find their union using |.
a={10,20,30}
b={30,40,50}
print(a|b)

# Q2

# Find the union using union().
a={10,20,30}
b={30,40,50}
c=a.union(b)
print(c)

# Q3
# Find the intersection using &.
a={10,20,30}
b={30,40,50}
print(a&b)

# Q4
# Find the intersection using intersection().
a={10,20,30}
b={30,40,50}
c=a.intersection(b)
print(c)

# Q5
# Find the difference:
# a-b
a={10,20,30}
b={30,40,50}
print(a-b)

# Q6
# Find the difference using
# difference()
a={10,20,30}
b={30,40,50}
c=a.difference(b)
print(c)

# Q7
# Find
# b-a
a={10,20,30}
b={30,40,50}
print(b-a)

# Q8
# Find the symmetric difference using
# ^
a={10,20,30}
b={30,40,50}
print(b^a)

# Q9
# Find the symmetric difference using
# symmetric_difference()
a={10,20,30}
b={30,40,50}
c=a.symmetric_difference(b)
print(c)

# Q10
# Update
# a={10,20}
# using
# update({30,40})
a={10,20}
a.update({30,40})
print(a)

# Q11
# Update a set using
# intersection_update()
a={10,20}
b={10,20,30,40}
a.intersection_update(b)
print(a)

# Q12
# Update a set using
# difference_update()
a={10,20,30,40,50,60}
b={10,20,30,40,70,80,90}
a.difference_update(b)
print(a)

# Q13
# Update a set using
# symmetric_difference_update()
a={10,20,30,40,50,60}
b={10,20,30,40,70,80,90}
a.symmetric_difference_update(b)
print(a)

# Q14
# Check whether
# {10,20}
# is a subset of
# {10,20,30,40}
# using
# issubset()
a={10,20}
b={10,20,30,40}
print(a.issubset(b))

# Q15
# Check the same using
# <=
a={10,20}
b={10,20,30,40}
print(a<=b)

# Q16
# Check whether
# {10,20,30,40}
# is a superset of
# {10,20}
# using
# issuperset()
a={10,20,30,40}
b={10,20}
print(a.issuperset(b))

# Q17
# Check the same using
# >=
a={10,20,30,40}
b={10,20}
print(a>=b)

# Q18
# Check whether
# {10,20}
# and
# {30,40}
# are disjoint.
a={10,20}
b={30,40}
print(a.isdisjoint(b))



# Q19

# Create a frozenset.
a=frozenset([1,2,3])
print(a)
# Print it.

# Q20
# Try adding an element into the frozenset.
# Write the code and comment the error.
a=frozenset([1,2,3])

# a.add(20)
# AttributeError: 'frozenset' object has no attribute 'add'

# Q21

# Convert a list into a frozenset.
a=frozenset([1,2,3])
print(a)

# Q22
# Convert a set into a frozenset.
a=frozenset({1,2,3})
print(a)

# Q23
# Find the length of a frozenset.
a=frozenset({1,2,3})
print(len(a))

# Q24
# Find the minimum, maximum and sum of a frozenset.
a=frozenset({1,2,3,4,5,6})
print(min(a))
print(max(a))
print(sum(a))

# Q25
# Traverse a frozenset using a loop.
a=frozenset({1,2,3,4,5,6})
for i in a:
    print(i)


# PART 2 — Output Prediction
# Q26
# a={1,2}
# b={2,3}
# print(a|b)
# output:- {1,2,3}
# Q27
# a={1,2}
# b={2,3}
# print(a&b)
# output:- {2}
# Q28
# a={1,2}
# b={2,3}
# print(a-b)
# output:- {1}

# Q29
# a={1,2}
# b={2,3}
# print(a^b)
# output:- {1,3}

# Q30
# a={1,2}
# b={1,2,3}
# print(a<=b)
# output:- True
# Q31
# a={1,2,3}
# b={1,2}
# print(a>=b)
# output:- True
# Q32
# a={1,2}
# b={3,4}
# print(a.isdisjoint(b))
# output:- True
# Q33
# a=frozenset([1,2,3])
# print(type(a))
# output:- <class 'frozenset'>
# Q34
# a=frozenset([10,20,30])
# print(len(a))
# output:- 3
# Q35
# a=frozenset([10,20,30])
# print(sum(a))
# output:- 60
# PART 3 — Placement / Interview Questions
# Q36

# Remove duplicates from two different lists and find their union.
a=[1,2,3,3,2,1,4,4,4,5]
b=[1,2,4,5,6,7,8,3,2,1,1,2,3]
c=set(a)
d=set(b)
print(c|d)

# Q37

# Find common elements between two lists using sets.
a=[1,2,3,3,2,1,4,4,4,5]
b=[1,2,4,5,6,7,8,3,2,1,1,2,3]
c=set(a)
d=set(b)
print(c&d)

# Q38
# Find elements present only in the first set.
a={1,2,3,4,5}
b={1,2,3,4,5,6,7,8}
print(a-b)
# Q39
# Find elements present only in the second set.
a={1,2,3,4,5}
b={1,2,3,4,5,6,7,8}
print(b-a)
# Q40
# Explain the difference between:
# remove()
# discard()
# pop()
# with code.
# remove(x) → removes x, gives KeyError if absent.
# discard(x) → removes x, no error if absent.
# pop() → removes an arbitrary/random element (because sets are unordered).


# Q41

# Explain the difference between:

# union()
# update()
# where update is used to add the element in the original set it modifies the set by adding the elements
# where union means it combines the two sets into one set
a={10,20,30}
b={30,40,50}

print(a.union(b))      # returns a new set
print(a)               # original unchanged

a.update(b)            # modifies original set
print(a)

# with examples.

# Q42

# Why is frozenset immutable?
f = frozenset([1,2,3])

# f.add(4)
# AttributeError: 'frozenset' object has no attribute 'add'
# Explain with code.

# Q43
# Can a frozenset be used as a dictionary key?
# Show with code.

key = frozenset([1,2,3])

d = {
    key: "This is a frozenset key"
}

print(d)
print(d[key])
# PART 4 — Google / Amazon Challenge
# Q44

# Given:

# a={10,20,30,40,50}
# b={30,40,50,60,70}

# Without using duplicate code, find:

# Union
# Intersection
# Difference (a-b)
# Difference (b-a)
# Symmetric Difference
# Is Subset
# Is Superset
# Is Disjoint
# Total Elements in Union
# Largest Element in Union
# Smallest Element in Union
# Sum of Union
# Even Count
# Odd Count

a={10,20,30,40,50}
b={30,40,50,60,70}

union_set = a | b
intersection_set = a & b
diff_ab = a - b
diff_ba = b - a
sym_diff = a ^ b

total = 0
count = 0
even_count = 0
odd_count = 0

for i in union_set:
    largest = i
    smallest = i
    break

for num in union_set:
    total += num
    count += 1

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference a-b:", diff_ab)
print("Difference b-a:", diff_ba)
print("Symmetric Difference:", sym_diff)
print("Is Subset:", a <= b)
print("Is Superset:", a >= b)
print("Is Disjoint:", a.isdisjoint(b))
print("Total Elements in Union:", count)
print("Largest Element in Union:", largest)
print("Smallest Element in Union:", smallest)
print("Sum of Union:", total)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
# Q45

# Given:

# data=[10,20,20,30,30,40,40,50,60,70,70]

# Perform all:

# Convert to set
# Convert to frozenset
# Print unique elements
# Print total unique elements
# Find largest
# Find smallest
# Find total
# Find average
# Count even numbers
# Count odd numbers
# Traverse using loop
# Search whether 50 exists
# Search whether 100 exists
# Explain why duplicates disappeared

data=[10,20,20,30,30,40,40,50,60,70,70]

s = set(data)
f = frozenset(s)

total = 0
count = 0
even_count = 0
odd_count = 0
found_50 = False
found_100 = False

for i in s:
    largest = i
    smallest = i
    break

for num in s:
    print(num)

    total += num
    count += 1

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if num == 50:
        found_50 = True

    if num == 100:
        found_100 = True

average = total / count

print("Set:", s)
print("Frozen Set:", f)
print("Unique Elements:", s)
print("Total Unique Elements:", count)
print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)
print("Average:", average)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("50 Exists:", found_50)
print("100 Exists:", found_100)
print("Duplicates disappeared because set stores only unique elements.")