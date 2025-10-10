### Day 1 ###

# PRINT #
# print("Hello World!")


# STRING CONCATENATION #
# print("Hello" + " Killol")
# print("Hello" + " " + "Killol")


# INPUT FUNCTION
# input("What is your name!")
# print("Hello " + input("What is your name? ") + "!")


# VARIABALES #
# name = input("What is your name!")
# print(name)

# name = "Jack"
# print(name)
# name="Brian"
# print(name)

# name = input("What is your name? ")
# length = len(name)
# print(length)

# glass1 = "milk"
# glass2 = "juice"
# temp=glass1
# glass1=glass2
# glass2=temp

### Day 2 ###

# DATA TYPES #

# Subscripting
# print("Happy"[0])
# print("Happy "[-2])

# String
# print("123" + "456")

# Integer
# print(123 + 456)

# Large Integer
# print(123_456_789)

# Float
# print(3.14)

# Boolean
# print(True)
# print(False)

# TYPE ERROR, CHECKING AND CONVERSION #
# print(type("Hello"))
# print(int("123") + int("456"))

# int()
# float()
# str()
# bool()

# print("Number of Letters " + str(len(input("Enter your name: "))))


# MATHEMATICAL OPERATIONS #
# print(1 + 2)
# print(2 - 1)
# # print(1/2) always float
# print(1 // 2) always int | Floor Division
# print(2*1) 
# print (2**2) Power

# BODMAS (Mutiplication and Division | Addition and Substraction have same importance)
# ()
# **
# * OR /
# + OR -

# print(3*3+3/3+3)
# print(3-3*3+3/3)

# NUMBER MANIPULATION #

# bmi = 84 / 1.65 ** 2
# print(bmi)

# Floors it
# print(int(bmi)) 

# Rounds it
# print(round(bmi)) integer
# print(round(bmi),2) float

# Continuous Add etc
# score = 123
# score = score + 1
# print(score)

# f String
# score = 0
# height = 1.8
# is_winning = True

# # All datatype are converted to string
# print(f"Your Score is = {score}, your height is {height}, you are winning {is_winning}")

### Day 3 ###

# Conditional Operations #
# = - Assignment
# == - Checking Equality

# Modulo Operator #
# 10%5 = 0 (remainder after dividing)
# 10%3 = 1

# Checking Odd or even
# num = int(input("Enter Number to check: "))
# mod = num%2
# if mod==0:
#     print("The given number is Even!")
# else:
#     print("The given number is Odd! because it has remainder ",mod)

# Elif
# Ticketing
# height = int(input("What is your height? "))
# bill=0
# if height>=120:
     
#     age = int(input("What is your age? "))
#     if age<12:
#         bill = 5
#         print(f"You can go, The fees are: ${bill}!")
#     elif age<=18:
#         bill = 7
#         print(f"You can go, The fees are: ${bill}!")
#     else:
#         bill = 12
#         print(f"You can go, The fees are: ${bill}!")
    
#     photo = bool(input("Do you want a photo (True|False)? "))
#     if photo == True:
#         bill+=3
#         print("Your Bill is: $")
# else:
#     print("Sorry, you can't got!")

# Pizza Order Selection
# print("Welcome to Dominos!!")
# size = (input("Size? (S, M or L): ")).lower()
# pepperoni = bool(input("Pepperoni? (True or False): "))
# extra_cheese = bool(input("Extra Cheese? (True or False): "))
# bill=0
# if size == 's':
#     bill += 15
# elif size == 'm':
#     bill += 20
# elif size == 'l':
#     bill += 25
# if pepperoni == True:
#     if size == 's':
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == True:
#     bill+=1
# else:
#     print("Invalid Size!")
# print("Please Pay : $",bill)

# Logical Operators #
# A and B -- Both have to be True
# C or D -- One True Both True
# not E -- if True it becomes False, if False it becomes True

# Ticketing
height = int(input("What is your height? "))
bill=0
if height>=120:
     
    age = int(input("What is your age? "))
    if age<12:
        bill = 5
        print(f"You can go, The fees are: ${bill}!")
    elif age<=18:
        bill = 7
        print(f"You can go, The fees are: ${bill}!")
    elif 45 <= age and age <= 50:
        print("You are Good, Enjoy!")
    else:
        bill = 12
        print(f"You can go, The fees are: ${bill}!")
    
    photo = bool(input("Do you want a photo (True|False)? "))
    if photo == True:
        bill+=3
        print("Your Bill is: $")
else:
    print("Sorry, you can't got!")


 
    

