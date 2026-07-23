# ============================================
# STRING SLICING - MODULE 2
# ============================================
# PART-1 : Coding Questions
# Q1
# # Create:
# # text = "Python Programming"
# # Print the first 6 characters.
text = "Python Programming"
print(text[0:6])

# Q2
# # Create:
# # text = "Python Programming"
# # Print only "Programming".
text = "Python Programming"
print(text[7:])

# Q3
# # Create:
# # text = "Artificial Intelligence"
# # Print "Artificial".
text = "Artificial Intelligence"
print(text[0:10])

# Q4
# # Create:
# # text = "Artificial Intelligence"
# # Print "Intelligence".
text = "Artificial Intelligence"
print(text[11:])

# Q5
# # Create:
# # text = "Programming"
# # Print the first five characters.
text = "Programming"
print(text[0:5])

# Q6
# # Create:
# # text = "Programming"
# # Print the last five characters using slicing.
text = "Programming"
print(text[-5:])

# Q7
# # Create:
# # text = "Python"
# # Print every character except the first.
text="Python"
print(text[1:])

# Q8
# # Create:
# # text = "Python"
# # Print every character except the last.
text="Python"
print(text[0:5])
# Q9
# # Create:
# # text = "Python Programming"
# # Print the complete string using slicing.
text = "Python Programming"
print(text[:])

# Q10
# # Create:
# # text = "Python Programming"
# # Print every second character.
text = "Python Programming"
print(text[::2])

# ============================================
# PART-2 : OUTPUT PREDICTION
# ============================================
# Q11
# text = "Python"
# print(text[1:4])
# Predict Output:-yth

# Q12
# text = "Python"
# print(text[:3])
# Predict Output:- Pyt

# Q13
# text = "Python"
# print(text[3:])
# Predict Output:-hon

# Q14
# text = "Programming"
# print(text[-5:])
# Predict Output:mming

# Q15
# text = "Programming"
# print(text[:-3])
# Predict Output:Programm

# Q16
# text = "Python"
# print(text[::2])
# Predict Output:- Pto

# Q17
# text = "Python"
# print(text[::-1])
# Predict Output:- nohtyP

# Q18
# text = "Artificial"
# print(text[2:8])
# Predict Output:-tifici

# Q19
# text = "Google"
# print(text[-4:-1])
# Predict Output:- ogl

# Q20
# text = "Amazon"
# print(text[1:6:2])
# Predict Output:- mzn

# ============================================
# PART-3 : FAANG TRICKY QUESTIONS
# ============================================
# Q21
# text = "Python Programming"
# print(text[:])
# Predict Output:-Python Programming

# Q22
# text = "Python"
# print(text[::-2])
# Predict Output:- nhy

# Q23
# text = "Programming"
# print(text[3:3])
# Predict Output: empty string

# Q24
# text = "Machine Learning"
# print(text[-8:-1])

# Predict Output:- earnin

# Q25
# text = "Python"

# print(text[5:1:-1])

# Predict Output:- noht

# ============================================
# PART-4 : PLACEMENT QUESTIONS
# ============================================
# Q26
# # Take a string.
# # Print the first half of the string using slicing.
s="sunny"
print(s[0:len(s)//2])
# Q27
# # Take a string.
# # Print the second half of the string using slicing.
s="sunny"
print(s[len(s)//2:])
# Q28
# # Take a string.
# # Reverse it using slicing only.
s="sunny"
print(s[::-1])
# Q29
# # Take a string.
# # Print every alternate character.
s="sunny"
print(s[::2])

# Q30
# # Take your full name.
# # Print only the surname using slicing.
s="shaik sanni fuddin"
print(s[-6:])

# ============================================
# 🚀 GOOGLE / AMAZON CHALLENGE
# ============================================
# Q31
# # Take a string from the user.
# # Print:
# # 1. First 5 characters
# # 2. Last 5 characters
# # 3. Every alternate character
# # 4. Reverse the string
# # 5. Middle three characters
# # 6. String without first and last character
s="sannifuddin"
print(s[0:5])
print(s[-5:])
print(s[::2])
print(s[::-1])
mid=len(s)//2
print(s[mid-1:mid+2])
print(s[1:-1])
