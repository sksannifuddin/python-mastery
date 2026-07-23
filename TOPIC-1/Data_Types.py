# Q1. Create variables of type:
# int
# float
# str
# bool
integer_value=15
float_value=34.56
string_value="my name is sunny"
boolean_value=True
# Print both value and datatype.
print(f"{type(integer_value)} - integer: {integer_value}")
print(f"{type(float_value)} - float: {float_value}")
print(f"{type(string_value)} - string: {string_value}")
print(f"{type(boolean_value)} - bool: {boolean_value}")

# Q2 Create a student profile containing:
# name
# age
# cgpa
# is_placed
name="sunny"
age=20
cgpa=7.5
is_placed=True
# Print their datatypes.
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_placed))

# Q3 Store your height, weight, and age and print their types.
height=168.5
weight=50
age=20
print(type(height))
print(type(weight))
print(type(age))

# Q4 Create a list containing:
# integer
# string
# float
# boolean
mixed_data=[10,2.5,"sunny",True]
# Print the list and its datatype.
print(mixed_data)
print(type(mixed_data))
# Q5 Create a tuple of your favorite 5 technologies and print its datatype.
technologies=("deep learning","machine learning","Ai","cloud","devops")
print(technologies)
print(type(technologies))
# Q6 Create a set of 5 programming languages and print its datatype.
language={"python","C","java","html","javascript"}
print(language)
print(type(language))
# Q7 Create a dictionary storing:
# name
# age
# college
details={"name":"sunny","age":20, "college":"N.B.K.R Institute of science and technology"}
# Print the datatype.
print(type(details))
# Q8 Create a variable containing None and print its datatype.
empty=None
print(type(empty))
# Q9 Check whether a variable is an integer using isinstance().
num=25
print(isinstance(num,int))
# Q10 Create one variable and change its datatype 4 times.
# Print type after each change.
a=25
print(type(a))
a=float(a)
print(type(a))
a=str(a)
print(type(a))
a=bool(a)
print(type(a))


# Q11
x = 10
print(type(x))
# output:- <class 'int'>
# Q12
x = 10
x = 10.5
print(type(x))
# output:- <class 'float'>
# Q13
print(type(True))
# output:- <class 'bool'>
# Q14
print(type(None))
# output:- <class 'NoneType'>
# Q15
a = [1, 2, 3]
print(type(a))
# output:- <class 'list'>
# Q16
a = (1, 2, 3)
print(type(a))
# output:- <class 'tuple'>
# Q17
a = {1, 2, 3}
print(type(a))
# output:- <class 'set'>
# Q18
a = {}
print(type(a))
# output:- <class 'dict'>
# ⚠️ Tricky question.

# Q19
a = set()
print(type(a))
# output:- <class 'set'>
# 🔥 Interview favorite.
# Q20
print(type(type(10)))
# output:- <class 'type'>

