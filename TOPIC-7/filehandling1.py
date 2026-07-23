# # 📘 FILE HANDLING — MODULE 1
# # (Opening, Reading, Writing, Appending, File Pointer, Properties)
# # PART 1 — 30 Questions with Answers

# > Run the questions in order because later programs use files created in earlier questions.

# ---

# ## Q1
# ### Create a file named `sample.txt`.

# Write:

# ```text
# Hello Python
# ```

# ### Answer

# ```python
# with open("sample.txt", "w") as file:
#     file.write("Hello Python")
# ```

# ---

# ## Q2
# ### Read the complete contents of `sample.txt`.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     content = file.read()

# print(content)
# ```

# ---

# ## Q3
# ### Append the following text to `sample.txt`:

# ```text
# Welcome to File Handling
# ```

# ### Answer

# ```python
# with open("sample.txt", "a") as file:
#     file.write("\nWelcome to File Handling")
# ```

# ---

# ## Q4
# ### Create a new file using `x` mode.

# ### Answer

# ```python
# try:
#     with open("newfile.txt", "x") as file:
#         file.write("New file created")
# except FileExistsError:
#     print("The file already exists")
# ```

# `x` mode creates a new file but gives `FileExistsError` if the file already exists.

# ---

# ## Q5
# ### Read a file using `with open()`.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     print(file.read())
# ```

# `with open()` closes the file automatically after the block finishes.

# ---

# ## Q6
# ### Check whether a file is closed before and after `close()`.

# ### Answer

# ```python
# file = open("sample.txt", "r")

# print("Before closing:", file.closed)

# file.close()

# print("After closing:", file.closed)
# ```

# ### Output

# ```text
# Before closing: False
# After closing: True
# ```

# ---

# ## Q7
# ### Print the file name.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     print(file.name)
# ```

# ### Output

# ```text
# sample.txt
# ```

# ---

# ## Q8
# ### Print the file mode.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     print(file.mode)
# ```

# ### Output

# ```text
# r
# ```

# ---

# ## Q9
# ### Open a file using `r+` mode.

# Write `"Python"` and print the contents.

# ### Answer

# ```python
# with open("sample.txt", "r+") as file:
#     file.write("Python")

#     file.seek(0)

#     print(file.read())
# ```

# > `r+` supports both reading and writing. It does not erase the whole file, but writing begins at the current cursor position.

# ---

# ## Q10
# ### Create `student.txt`.

# Write:

# ```text
# Sunny
# 21
# AIDS
# ```

# Print every line separately.

# ### Answer

# ```python
# with open("student.txt", "w") as file:
#     file.write("Sunny\n")
#     file.write("21\n")
#     file.write("AIDS")

# with open("student.txt", "r") as file:
#     for line in file:
#         print(line.strip())
# ```

# ---

# ## Q11
# ### Read only the first 5 characters of `sample.txt`.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     print(file.read(5))
# ```

# ---

# ## Q12
# ### Read only the first 10 characters.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     print(file.read(10))
# ```

# ---

# ## Q13
# ### Read one line using `readline()`.

# ### Answer

# ```python
# with open("student.txt", "r") as file:
#     first_line = file.readline()

# print(first_line.strip())
# ```

# ### Output

# ```text
# Sunny
# ```

# ---

# ## Q14
# ### Read two lines using `readline()`.

# ### Answer

# ```python
# with open("student.txt", "r") as file:
#     first_line = file.readline()
#     second_line = file.readline()

# print(first_line.strip())
# print(second_line.strip())
# ```

# ### Output

# ```text
# Sunny
# 21
# ```

# ---

# ## Q15
# ### Read all lines using `readlines()`.

# ### Answer

# ```python
# with open("student.txt", "r") as file:
#     lines = file.readlines()

# print(lines)
# ```

# Possible output:

# ```python
# ['Sunny\n', '21\n', 'AIDS']
# ```

# ---

# ## Q16
# ### Print every line using a loop.

# ### Answer

# ```python
# with open("student.txt", "r") as file:
#     for line in file:
#         print(line.strip())
# ```

# ---

# ## Q17
# ### Write a list of strings using `writelines()`.

# ### Answer

# ```python
# lines = [
#     "Python\n",
#     "Java\n",
#     "Machine Learning\n",
#     "Artificial Intelligence\n"
# ]

# with open("courses.txt", "w") as file:
#     file.writelines(lines)

# with open("courses.txt", "r") as file:
#     print(file.read())
# ```

# > `writelines()` does not automatically add `\n`. We must add it ourselves.

# ---

# ## Q18
# ### Copy the contents of `sample.txt` into `copy.txt`.

# ### Answer

# ```python
# with open("sample.txt", "r") as source:
#     content = source.read()

# with open("copy.txt", "w") as destination:
#     destination.write(content)

# print("File copied successfully")
# ```

# ---

# ## Q19
# ### Count the total number of lines in `sample.txt`.

# ### Answer

# ```python
# line_count = 0

# with open("sample.txt", "r") as file:
#     for line in file:
#         line_count += 1

# print("Total lines:", line_count)
# ```

# ---

# ## Q20
# ### Count the total number of words.

# ### Answer

# ```python
# word_count = 0

# with open("sample.txt", "r") as file:
#     for line in file:
#         words = line.split()
#         word_count += len(words)

# print("Total words:", word_count)
# ```

# Without using `len()`:

# ```python
# word_count = 0

# with open("sample.txt", "r") as file:
#     for line in file:
#         for word in line.split():
#             word_count += 1

# print("Total words:", word_count)
# ```

# ---

# ## Q21
# ### Count the total number of characters.

# ### Answer

# ```python
# character_count = 0

# with open("sample.txt", "r") as file:
#     content = file.read()

#     for character in content:
#         character_count += 1

# print("Total characters:", character_count)
# ```

# This includes spaces and newline characters.

# ---

# ## Q22
# ### Count vowels in a file.

# ### Answer

# ```python
# vowel_count = 0

# with open("sample.txt", "r") as file:
#     content = file.read()

#     for character in content.lower():
#         if character in "aeiou":
#             vowel_count += 1

# print("Total vowels:", vowel_count)
# ```

# ---

# ## Q23
# ### Count uppercase letters.

# ### Answer

# ```python
# uppercase_count = 0

# with open("sample.txt", "r") as file:
#     content = file.read()

#     for character in content:
#         if character.isupper():
#             uppercase_count += 1

# print("Uppercase letters:", uppercase_count)
# ```

# ---

# ## Q24
# ### Count lowercase letters.

# ### Answer

# ```python
# lowercase_count = 0

# with open("sample.txt", "r") as file:
#     content = file.read()

#     for character in content:
#         if character.islower():
#             lowercase_count += 1

# print("Lowercase letters:", lowercase_count)
# ```

# ---

# ## Q25
# ### Count digits in a file.

# ### Answer

# ```python
# digit_count = 0

# with open("student.txt", "r") as file:
#     content = file.read()

#     for character in content:
#         if character.isdigit():
#             digit_count += 1

# print("Total digits:", digit_count)
# ```

# For `21`, the digit count is `2`.

# ---

# ## Q26
# ### Count spaces in a file.

# ### Answer

# ```python
# space_count = 0

# with open("sample.txt", "r") as file:
#     content = file.read()

#     for character in content:
#         if character == " ":
#             space_count += 1

# print("Total spaces:", space_count)
# ```

# ---

# ## Q27
# ### Find the current cursor position using `tell()`.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     print("Initial position:", file.tell())

#     file.read(5)

#     print("Position after reading 5 characters:", file.tell())
# ```

# `tell()` returns the current file-pointer position.

# ---

# ## Q28
# ### Move the cursor using `seek()`.

# ### Answer

# ```python
# with open("sample.txt", "r") as file:
#     print(file.read(5))

#     print("Current position:", file.tell())

#     file.seek(0)

#     print("Position after seek:", file.tell())

#     print(file.read())
# ```

# `seek(0)` moves the cursor to the beginning of the file.

# ---

# ## Q29
# ### Print these file properties:

# - Name
# - Mode
# - Closed

# ### Answer

# ```python
# file = open("sample.txt", "r")

# print("File name:", file.name)
# print("File mode:", file.mode)
# print("Is closed:", file.closed)

# file.close()

# print("Is closed after close():", file.closed)
# ```

# ---

# ## Q30 — Google/Amazon Mini Challenge

# ### Given `student.txt`, perform all the following:

# - Read the file
# - Count lines
# - Count words
# - Count characters
# - Count vowels
# - Count uppercase letters
# - Count lowercase letters
# - Count digits
# - Count spaces
# - Copy the contents to `backup.txt`
# - Print the file name
# - Print the mode
# - Print the current cursor position

# ### Answer

# ```python
# line_count = 0
# word_count = 0
# character_count = 0
# vowel_count = 0
# uppercase_count = 0
# lowercase_count = 0
# digit_count = 0
# space_count = 0

# with open("student.txt", "r") as file:
#     print("File name:", file.name)
#     print("File mode:", file.mode)
#     print("Initial cursor position:", file.tell())

#     content = file.read()

#     print("Cursor position after reading:", file.tell())

# for character in content:
#     character_count += 1

#     if character.lower() in "aeiou":
#         vowel_count += 1

#     if character.isupper():
#         uppercase_count += 1

#     if character.islower():
#         lowercase_count += 1

#     if character.isdigit():
#         digit_count += 1

#     if character == " ":
#         space_count += 1

# for line in content.splitlines():
#     line_count += 1

#     for word in line.split():
#         word_count += 1

# with open("backup.txt", "w") as backup:
#     backup.write(content)

# print("\nFile Content:")
# print(content)

# print("\nAnalysis")
# print("Total lines:", line_count)
# print("Total words:", word_count)
# print("Total characters:", character_count)
# print("Total vowels:", vowel_count)
# print("Uppercase letters:", uppercase_count)
# print("Lowercase letters:", lowercase_count)
# print("Total digits:", digit_count)
# print("Total spaces:", space_count)

# print("\nContents copied to backup.txt")
# ```

# ---



