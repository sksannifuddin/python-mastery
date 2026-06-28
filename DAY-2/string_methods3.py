# ============================================
# STRING METHODS - MODULE 4
# VALIDATION METHODS
# isalpha(), isdigit(), isalnum(), isspace(),
# islower(), isupper(), istitle(), isascii(),
# isdecimal(), isnumeric(), isidentifier(), isprintable()
# ============================================

# PART-1 : Coding Questions

# Q1
# Create:
# text = "Python"
# Check whether it contains only alphabets.
text = "Python"
print(text.isalpha())

# Q2
# Create:
# text = "Python123"
# Check whether it contains only alphabets.
text = "Python123"
print(text.isalpha())

# Q3
# Create:
# text = "12345"
# Check whether it contains only digits.
text = "12345"
print(text.isdigit())

# Q4
# Create:
# text = "123abc"
# Check whether it contains only digits.
text = "123abc"
print(text.isdigit())

# Q5
# Create:
# text = "Python123"
# Check whether it is alphanumeric.
text = "Python123"
print(text.isalnum())

# Q6
# Create:
# text = "Python 123"
# Check whether it is alphanumeric.
text = "Python 123"
print(text.isalnum())

# Q7
# Create:
# text = "     "
# Check whether it contains only spaces.
text = "     "
print(text.isspace())
# Q8
# Create:
# text = "python"
# Check whether it is lowercase.
text = "python"
print(text.islower())

# Q9
# Create:
# text = "PYTHON"
# Check whether it is uppercase.
text = "PYTHON"
print(text.isupper())

# Q10
# Create:
# text = "Python Programming"
# Check whether it is title case.
text = "Python Programming"
print(text.istitle())

# PART-2 : Output Prediction

# Q11
text = "Python"
print(text.isalpha())
# Predict Output:- True

# Q12
text = "Python123"
print(text.isalpha())
# Predict Output:-False

# Q13
text = "12345"
print(text.isdigit())
# Predict Output:-True

# Q14
text = "12.5"
print(text.isdigit())
# Predict Output:-False

# Q15
text = "Python123"
print(text.isalnum())
# Predict Output:-Treu

# Q16
text = "Python 123"
print(text.isalnum())
# Predict Output:-False

# Q17
text = "   "
print(text.isspace())
# Predict Output:-True

# Q18
text = "python"
print(text.islower())
# Predict Output:-True

# Q19
text = "PYTHON"
print(text.isupper())
# Predict Output:-True

# Q20
text = "Python Programming"
print(text.istitle())
# Predict Output:-True

# PART-3 : FAANG Tricky Questions

# Q21
text = ""
print(text.isalpha())
# Predict Output:- False

# Q22
text = "123"
print(text.isdecimal())
print(text.isdigit())
print(text.isnumeric())
# Predict Output:- True,True,True

# Q23
text = "variable_name"
print(text.isidentifier())
# Predict Output:- True

# Q24
text = "2name"
print(text.isidentifier())
# Predict Output:-False

# Q25
text = "Hello\nPython"
print(text.isprintable())
# Predict Output:- False

# PART-4 : Placement Coding Questions

# Q26
# Take username as input.
# Check whether it contains only alphabets.
s="sunny"
print(s.isalpha())

# Q27
# Take phone number as input.
# Check whether it contains only digits.
s="123456789"
print(s.isdigit())

# Q28
# Take password as input.
# Check whether it is alphanumeric.
s="sunny123"
print(s.isalnum())

# Q29
# Take a variable name as input.
# Check whether it is a valid Python identifier.
s="text"
print(s.isidentifier())

# Q30
# Take a sentence as input.
# Check whether it is in title case.
s="sunny is good boy"
print(s.istitle())

# GOOGLE / AMAZON CHALLENGE

# Q31
# Take a password from user.
# Validate:
# 1. It must be alphanumeric.
# 2. It must not contain spaces.
# 3. It must contain at least 8 characters.
# Print whether password is valid or invalid.
s=input("enter your password:")
if " " not in s:
    if s.isalnum():
        if len(s)>=8:
            print("your passwword is valid")
        else:
            print("you password must contain atleast 8 characters")
    else:
        print("Password must contain only letters and numbers.")
else:
    print("your password must not contain spaces")


# ============================================
# STRING METHODS - MODULE 5
# FORMATTING METHODS
# center(), ljust(), rjust(), zfill(),
# expandtabs(), format(), format_map()
# ============================================

# PART-1 : Coding Questions

# Q1
# Create:
# text = "Python"
# Center it in width 20.
text = "Python"
print(text.center(20))

# Q2
# Create:
# text = "Python"
# Center it in width 20 using "*".
text = "Python"
print(text.center(20,"*"))

# Q3
# Create:
# text = "Python"
# Left align it in width 15.

# Q4
# Create:
# text = "Python"
# Right align it in width 15.
text = "Python"
print(text.ljust(15))

# Q5
# Create:
# text = "42"
# Fill it with zeros to make width 5.
text = "42"
print(text.zfill(5))

# Q6
# Create:
# text = "7"
# Fill it with zeros to make width 3.
text = "7"
print(text.zfill(3))

# Q7
# Create:
# text = "Python\tJava"
# Use expandtabs() with tab size 4.
text = "Python\tJava"
print(text.expandtabs(4))

# Q8
# Use format() to print:
# My name is Sunny and I am 20 years old.
print("My name is {} and I am {} years old".format("sunny","20"))
# Q9
# Use format() to print:
# Product: Laptop, Price: 50000
print("product: {}, Price: {}".format("Laptop", {50000}))
# Q10
# Use format_map() with dictionary:
# {"name":"Sunny", "age":20}
d={"name":"sunny","age":20}
print("my name is {name} i am {age} years old".format_map(d))
# PART-2 : Output Prediction

# Q11
text = "Python"
print(text.center(10))
# Predict Output:-  Python

# Q12
text = "Python"
print(text.center(10, "*"))
# Predict Output:-**Python**

# Q13
text = "Python"
print(text.ljust(10, "-"))
# Predict Output:- --Python

# Q14
text = "Python"
print(text.rjust(10, "-"))
# Predict Output:Python--

# Q15
text = "42"
print(text.zfill(5))
# Predict Output:-00042

# Q16
text = "-42"
print(text.zfill(5))
# Predict Output:-0042

# Q17
text = "A\tB"
print(text.expandtabs(4))
# Predict OutputA    B

# Q18
print("My name is {} and I am {}".format("Sunny", 20))
# Predict Output:-  My name is Sunny and I am 20 

# Q19
print("{1} loves {0}".format("Python", "Sunny"))
# Predict Output: Sunny Loves Python

# Q20
data = {"name": "Sunny", "course": "Python"}
print("{name} learns {course}".format_map(data))
# Predict Output:- Sunny learns Python

# PART-3 : FAANG Tricky Questions

# Q21
text = "Python"
print(text.center(4))
# Predict Output:-Python

# Q22
text = "Python"
print(text.zfill(3))
# Predict Output:Python

# Q23
print("{:.2f}".format(10.5678))
# Predict Output:10.57

# Q24
print("{:>10}".format("AI"))
# Predict Output:-        AI

# Q25
print("{:<10}".format("AI"))
# Predict Output:-AI

# PART-4 : Placement Coding Questions

# Q26
# Take a number as string.
# Add leading zeros until width becomes 6.
num="1234"
print(num.zfill(2))
# Q27
# Take name and age.
# Print using format().
print("My name is {} and I am {} years old".format("sunny","20"))

# Q28
# Take product name and price.
# Print a bill using format().
name="Laptop"
price="50000"
print("My {} price is {}".format(name,price))

# Q29
# Take a word.
# Center it using "*" with width 30.
s="Python"
print(s.center(30,"*"))
# Q30
# Take a student dictionary:
# name, branch, college
# Print using format_map().
student={"name":"sunny",
"branch":"aids",
"college":"nbkr"}
print("my name is {name} , my branch is {branch} and my college name is {college}".format_map(student))


# GOOGLE / AMAZON CHALLENGE

# Q31
# Create a small invoice.
# Inputs:
# product name
# quantity
# price
# Print:
# Product name left aligned
# Quantity centered
# Price right aligned
# Total bill at the end
# ============================================
# STRING METHODS - MODULE 6
# ADVANCED STRING METHODS
# partition(), rpartition(), casefold(),
# encode(), maketrans(), translate()
# ============================================

# PART-1 : Coding Questions

# Q1
# Create:
# text = "Python is easy"
# Use partition("is").

# Q2
# Create:
# text = "Python is easy and Python is powerful"
# Use partition("Python").

# Q3
# Create:
# text = "Python is easy and Python is powerful"
# Use rpartition("Python").

# Q4
# Create:
# text = "Python Programming"
# Use partition("Java").

# Q5
# Create:
# text = "Straße"
# Convert it using casefold().

# Q6
# Create:
# text = "PYTHON"
# Convert it using casefold().

# Q7
# Create:
# text = "Python"
# Encode it using default encoding.

# Q8
# Create:
# text = "Python"
# Create translation table to replace P with J.
# Use maketrans() and translate().

# Q9
# Create:
# text = "hello world"
# Replace h with H and w with W using translate().

# Q10
# Create:
# text = "banana"
# Replace a with @ using translate().

# PART-2 : Output Prediction

# Q11
text = "Python is easy"
print(text.partition("is"))
# Predict Output

# Q12
text = "Python is easy"
print(text.partition("Java"))
# Predict Output

# Q13
text = "Python is easy and Python is powerful"
print(text.rpartition("Python"))
# Predict Output

# Q14
text = "PYTHON"
print(text.casefold())
# Predict Output

# Q15
text = "Straße"
print(text.casefold())
# Predict Output

# Q16
text = "Python"
print(text.encode())
# Predict Output

# Q17
table = str.maketrans("P", "J")
text = "Python"
print(text.translate(table))
# Predict Output

# Q18
table = str.maketrans("aeiou", "12345")
text = "education"
print(text.translate(table))
# Predict Output

# Q19
text = "Python"
print(text.partition("t"))
# Predict Output

# Q20
text = "Python Python"
print(text.rpartition("Python"))
# Predict Output

# PART-3 : FAANG Tricky Questions

# Q21
text = "Python"
print(text.partition("z"))
# Predict Output

# Q22
text = "Python"
print(text.rpartition("z"))
# Predict Output

# Q23
text = "HELLO"
print(text.lower())
print(text.casefold())
# Predict Output

# Q24
table = str.maketrans("abc", "123")
text = "abc cab"
print(text.translate(table))
# Predict Output

# Q25
table = str.maketrans("", "", "aeiou")
text = "education"
print(text.translate(table))
# Predict Output

# PART-4 : Placement Coding Questions

# Q26
# Take an email:
# username@gmail.com
# Use partition("@") to separate username and domain.

# Q27
# Take a full name.
# Use partition(" ") to separate first name and remaining name.

# Q28
# Take a sentence.
# Use rpartition(" ") to separate the last word.

# Q29
# Take a sentence.
# Convert it using casefold().
# Check whether it equals another sentence ignoring case.

# Q30
# Take a sentence.
# Remove all vowels using maketrans() and translate().

# GOOGLE / AMAZON CHALLENGE

# Q31
# Take a sentence from user.
# Perform:
# 1. Convert to casefold
# 2. Remove vowels using translate
# 3. Partition the sentence at first space
# 4. rpartition the sentence at last space
# 5. Encode the final sentence
# Print all results.