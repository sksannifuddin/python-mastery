
# Q1 Take a person's age.
# If age ≥ 18:
# Ask whether they have a voter ID (yes/no).
# If yes → Print Eligible to Vote
# Else → Print Apply for Voter ID
# Else:
# Print Not Eligible to Vote
age=int(input("enter the age"))
if age >=18:
    voter_id = input("do you have voter id?(yes/no)").lower()
    if voter_id == "yes":
        print("you are eligible to vote")
    else:
        print("apply for the voter id")
else :
    print("you are not eligible to vote")

# Q2 Take username.
# Correct username:
# Sunny
# If correct:
# Ask for password.
# Correct password:
# python123
# If correct:
# Login Successful
# Else:
# Wrong Password
# Else:
# Invalid Username
username=input("enter the username")
corr_user="Sunny"
if username == corr_user:
    pas=input("enter the password")
    corr_pas="python123"
    if pas==corr_pas:
        print("login successfull")
    else:
        print("wrong password")
else:
    print("invalid username")
    
    
# Q3 Take marks.
# If marks ≥ 35:
# Ask attendance percentage.
# If attendance ≥ 75:
# Pass
# Else:
# Shortage of Attendance
# Else:
# Fail
exam_marks=int(input("enter your marks"))
if exam_marks>=35:
    attendance=int(input("enter your attendance"))
    if attendance >= 75:
        print("passed!")
    else:
        print("shortage of attendance")
else:
    print("fail")
    
    
# Q4 Take salary.
# If salary ≥ 50000:
# Ask experience.
# If experience ≥ 2 years:
# Promotion Eligible
# Else:
# Gain More Experience
# Else:
# Salary Criteria Not Met
salary=int(input("enter your salary"))
if salary >= 50000:
    experience=float(input(" enter your experience"))
    if experience >=2 :
        print("promotion eligible")
    else:
        print("Gain more Experience")
else:
    print("salary criteria not met")

# Q5
# Take age.
# If age ≥ 18:
# Ask whether the person has a driving license (yes/no).
# If yes:
# Can Drive
# Else:
# Apply for License
# Else:
# Under Age
age=int(input("enter the age"))
if age >=18:
    driving_license = input("do you have driving license?(yes/no)").lower()
    if driving_license == "yes":
        print("you can drive ")
    else:
        print("apply for license")
else :
    print("you are under age")

# Q6 Take CGPA.
# If CGPA ≥ 7.5:
# Ask communication skill rating (1–10).
# If rating ≥ 7:
# Eligible for Placement
# Else:
# Improve Communication Skills
# Else:
# CGPA Not Eligible
cgpa=float(input("enter the cgpa"))
if cgpa >=7.5:
    communication_rating = float(input("do you have communication skills?(1-10)"))
    if communication_rating >=7:
        print("you are eligible for placement ")
    else:
        print("improve the communication skills")
else :
    print("cgpa not eligible")

# Q7
# Take amount.
# If amount ≥ 1000:
# Ask payment method.
# If payment method is:
# UPI
# Print
# Payment Successful
# Else
# Invalid Payment Method
# Else
# Minimum Amount Required
amount=int(input("ener the amount"))
if amount >=1000:
    payment_method=input("enter the payment method").lower()
    if payment_method=="upi":
        print("payment successful")
    else:
        print("invalid payment method")
else:
    print("minimum amount required")

# Q8 Take username.
# If username exists:
# Ask OTP.
# Correct OTP:
# 123456
# If correct:
# Login Successful
# Else:
# Invalid OTP
# Else:
# User Not Found
username=input("enter the username").lower()
corr_username="sunny"
if username ==corr_username:
    otp=int(input("enter the otp"))
    corr_otp=123456
    if otp==corr_otp:
        print("Login Successful")
    else:
        print("invalid otp")
else:
    print("user not found")

# Q9 Take a number.
# If number > 0:
# If divisible by 2:
# Positive Even
# Else:
# Positive Odd
# Else:
# Negative Number
num=int(input("enter the number"))
if num>0:
    if num%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    print("negative number")
    
# Q10 Take temperature.
# If temperature > 30:
# Ask humidity.
# If humidity > 70:
# Hot and Humid
# Else:
# Hot and Dry
# Else:
# Pleasant Weather
temperature=float(input("enter the temperature"))
if temperature >30:
    humidity=float(input("enter the humidity"))
    if humidity >70:
        print("hot and humid")
    else:
        print("hot and dry")
else:
    print("pleasent weather")


# Q11
age = 20
if age >= 18:
    if age >= 60:
        print("Senior")
    else:
        print("Adult")
else:
    print("Minor")
# output:- adult

# Q12
x = 10
if x > 0:
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
# output:- even

# Q13
username = "Sunny"
if username == "Sunny":
    password = "python"

    if password == "python123":
        print("Login")
    else:
        print("Wrong Password")
else:
    print("User Not Found")
 # output:-  Wrong password   
    
# Q14
marks = 80
if marks >= 35:
    attendance = 70

    if attendance >= 75:
        print("Pass")
    else:
        print("Attendance Shortage")
# output:- attendence shortage

# Q15
salary = 60000
if salary >= 50000:
    experience = 1

    if experience >= 2:
        print("Promotion")
    else:
        print("No Promotion")
# output:- no promotion

# Q16
x = -5

if x > 0:
    if x % 2 == 0:
        print("Positive Even")
else:
    print("Negative")
# output:- negativve

# Q17
if True:
    if False:
        print("A")
    else:
        print("B")
# output:-B

# Q18
if False:
    if True:
        print("A")
else:
    print("B")
# output:- b    
    
# Q19
if "":
    if True:
        print("Python")
else:
    print("Java")
# output:- java

# Q20
if "False":
    if 0:
        print("Google")
    else:
        print("Amazon")
# output:- amazon


# Q21
if True:
    print("A")
    if False:
        print("B")
    print("C")
print("D")
# output:- a,c,d 

# Q22
x = 0
if not x:
    print("A")
else:
    print("B")
# output:- a    
    
# Q23
if []:
    print("A")
else:
    print("B")
# output:- b

# Q24
if [0]:
    print("Python")
else:
    print("Java")
# output:- python

# Q25
if None:
    print("Google")
else:
    print("Microsoft")
# output:- microsoft


# Q26
# Check whether a person is eligible for a passport.
# Conditions:
# Age ≥ 18
# Aadhaar available (yes/no)
age=int(input("enter your age"))
if age>=18:
    aadhar=input("does your aadhar availabe(yes/no)").lower()
    if aadhar=="yes":
        print("you are eligible for a passport")
    else:
        print("not eligible")
else:
    print("you are under age")
# Q27

# Check whether a student can write the final exam.
# Conditions:
# Attendance ≥ 75
# Fees paid (yes/no)
attendance=float(input("enter your attendance"))
if attendance >=75:
    fees=input("did you pay your fee?(yes/no)").lower()
    if fees=="yes":
        print("you can the final exam")
    else:
        print("fee not paid")
else:
    print("attendance shortage")

# Q28
# ATM Withdrawal
# Conditions:
# PIN is correct.
# Balance is sufficient.
correct_pin = 34567
balance = 50000

pin = int(input("Enter PIN: "))

if pin == correct_pin:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        print("Amount Debited")
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")
    
# Q29
# Online Shopping
# Conditions:
# Product available.
# Payment successful.
product=input("enter the product")
available_product="wathces"
if product ==available_product:
    payment=input("enter the payment method:").lower()
    if payment=="upi":
        print("payment successful")
    else:
        print("payment not successful")
else:
    print("product not available")

# Q30
# Company Interview
# Conditions:
# CGPA ≥ 7.5
# Aptitude test passed (yes/no)
# Print whether the student is selected for the interview.
cgpa=float(input("enter your cgpa"))
if cgpa>=7.5:
    test=input("did you pass your aptitude test(yes/no)").lower()
    if test=="yes":
        print("you are selected")
    else:
        print("you are not selected")
else:
    print("your cgpa is less")