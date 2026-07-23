# STRING INDEXING - MODULE 1
# ============================================
# PART-1 : Coding Questions
# Q1
# Create:
# text = "Python"
# Print the first character.
text = "Python"
print(text[0])

# Q2
# Print the last character.
text = "Python"
print(text[-1])

# Q3
# Print the third character.
text = "Python"
print(text[2])

# Q4
# Print the second last character.
text = "Python"
print(text[-2])

# Q5
# Create
# text = "Programming"
# Print the fifth character.
text = "Programming"
print(text[4])

# Q6
# Create
# text = "Artificial Intelligence"
# Print the first character.
text = "Artificial Intelligence"
print(text[0])

# Q7
# Print the last character.
text = "Artificial Intelligence"
print(text[-1])

# Q8
# Print the tenth character.
text = "Artificial Intelligence"
print(text[9])

# Q9
# Take your name.
# Print the first letter.
name="sannifuddin"
print(name[0])

# Q10
# Take your college name.
# Print the last letter.
college="N.B.K.R"
print(college[-1])


# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# text = "Python"
# print(text[0])

# Predict Output:- P

# Q12
# text = "Python"
# print(text[5])

# Predict Output:-n

# Q13
# text = "Python"
# print(text[-1])

# Predict Output:- n

# Q14
# text = "Python"
# print(text[-3])

# Predict Output:-h

# Q15
# text = "Programming"
# print(text[4])

# Predict Output:- r

# Q16
# text = "Programming"
# print(text[-4])

# Predict Output:-m

# Q17
# text = "AI"
# print(text[1])

# Predict Output:-I

# Q18
# text = "Google"
# print(text[-6])

# Predict Output:-G

# Q19
# text = "Amazon"
# print(text[0], text[-1])

# Predict Output:-A, n

# Q20
# text = "Python"
# print(text[2], text[-2])

# Predict Output:- t, o

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# text = "Python"
# print(text[len(text)-1])

# Predict Output:- n

# Q22
# text = "Python"
# print(text[len(text)-2])

# Predict Output:-o

# Q23
# text = "Data Science"
# print(text[5])

# Predict Output:- S

# Q24
# text = "Machine Learning"
# print(text[-8])

# Predict Output:- L

# Q25
# text = "Python"

# print(text[0])

# print(text[-len(text)])

# Predict Output:- P, P

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26

# Take a string.
# Print
# First character
# Last character
text = "Python"
print(text[0])
print(text[-1])


# Q27

# Take a string.
# Print the middle character.
# (Hint: Use len().)
text = "Sanni"
print(text[len(text)//2])

# Q28

# Take a string.
# Print the second character and second last character.
text = "Python"
print(text[1])
print(text[-2])

# Q29

# Take a word.
# Print every character using indexing only.
# (Do not use loops.)
text = "Python"
print(text[0],text[1],text[2],text[3],text[4],text[5])

# Q30
# Take your full name.
# Print
# First letter
# Last letter
# Length
name="sk.sannifuddin"
print(name[0],name[-1],len(name))
# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31

# Take a string from the user.
# Print:

# First character
# Last character
# Middle character
# Second character
# Second last character
# Length of the string

name="sk.sannifuddin"
print(name[0],name[-1],name[len(name)//2],name[1],name[-2],len(name))