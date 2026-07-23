# ============================================
# STRING METHODS - PART 2
# (find(), index(), count(), startswith(), endswith(), split(), join())
# ============================================

# PART-1 : Coding Questions
# Q1
# Create:
# text = "Python Programming"
# Find the position of "P".
text = "Python Programming"
print(text.find("P"))

# Q2
# Create:
# text = "Python Programming"
# Find the position of "Programming".
text = "Python Programming"
print(text.find("Programming"))

# Q3
# Create:
# text = "Python Programming"
# Find the position of "Java".
text = "Python Programming"
print(text.find("Java"))

# Q4
# Create:
# text = "Python Python Java Python"
# Count how many times "Python" appears.
text = "Python Python Java Python"
print(text.count("Python"))

# Q5
# Create:
# text = "banana"
# Count how many times "a" appears.
text="banana"
print(text.count("a"))

# Q6
# Create:
# text = "Python Programming"
# Check whether it starts with "Python".
text = "Python Programming"
print(text.startswith("Python"))

# Q7
# Create:
# text = "Python Programming"
# Check whether it starts with "Java".
text = "Python Programming"
print(text.startswith("Java"))

# Q8
# Create:
# text = "Python Programming"
# Check whether it ends with "Programming".
text = "Python Programming"
print(text.endswith("Programming"))

# Q9
# Create:
# text = "Python Programming"
# Check whether it ends with "Python".
text = "Python Programming"
print(text.endswith("Python"))

# Q10
# Create:
# text = "Python is easy to learn"
# Split the sentence into individual words.
text = "Python is easy to learn"
print(text.split())



# Q11

text = "Python"

print(text.find("t"))

# Predict Output :- 2


# Q12

text = "Python"

print(text.find("z"))

# Predict Output :- -1


# Q13

text = "banana"

print(text.count("a"))

# Predict Output:- 3


# Q14

text = "banana"

print(text.count("na"))

# Predict Output:- 2


# Q15

text = "Python"

print(text.startswith("Py"))

# Predict Output:- True


# Q16

text = "Python"

print(text.endswith("on"))

# Predict Output:- True


# Q17

text = "Python Java C"

print(text.split())

# Predict Output:- ['Python','Java','C']


# Q18

text = "A,B,C,D"

print(text.split(","))

# Predict Output:- ['A','B','C','D']


# Q19

text = "Python"

print(text.find("P"))

# Predict Output:- 0


# Q20

text = "Python"

print(text.find("Python"))

# Predict Output:- 0



# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================

# Q21

text = "Python Python"

print(text.find("Python", 2))

# Predict Output:- 7


# Q22

text = "banana"

print(text.count("an"))

# Predict Output:- 2


# Q23

text = "Python"

print(text.startswith("python"))

# Predict Output:- False


# Q24

text = "Python Programming"

print(text.endswith("ming"))

# Predict Output:- True


# Q25

text = "apple apple apple"

print(text.upper().count("APPLE"))

# Predict Output:- 3



# Q26
# Take your full name as input.
# Count how many times the letter 'a' appears.
name="sannifudiin"
print(name.count("a"))

# Q27
# Take a sentence as input.
# Check whether it starts with "Python".
sentence="Python is my favorite"
print(sentence.startswith("Python"))

# Q28
# Take a sentence as input.
# Check whether it ends with "." (period).
sentence="Python is my favorite."
print(sentence.endswith("."))

# Q29
# Take a sentence as input.
# Split the sentence into words and print the list.
sentence="Python is my favorite."
print(sentence.split())
# Q30
# Take a comma-separated string.
# Example:
# Apple,Banana,Mango,Orange
# Convert it into a list using split().
string="Apple,Banana,Mango,Orange"
print(string.split())


# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================

# Q31
# Take a sentence from the user.
# Example:
# Python is easy and Python is powerful
# Print:
# 1. Total number of words
# 2. Number of times "Python" occurs
# 3. Whether the sentence starts with "Python"
# 4. Whether the sentence ends with "powerful"
# 5. Position of the first occurrence of "Python"
sentence="Python is easy and Python is powerful"
print(len(sentence.split()))
print(sentence.count("Python"))
print(sentence.startswith("Python"))
print(sentence.endswith("powerful"))
print(sentence.find("Python"))
