### Day 1 ###

#- PRINT #
# print("Hello World!")


#- STRING CONCATENATION #
# print("Hello" + " Killol")
# print("Hello" + " " + "Killol")


#- INPUT FUNCTION #
# input("What is your name!")
# print("Hello " + input("What is your name? ") + "!")


#- VARIABALES #
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

#- DATA TYPES #

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


#- MATHEMATICAL OPERATIONS #
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

#- NUMBER MANIPULATION #

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

#- Conditional Operations #
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

#- # Ticketing
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
#     elif 45 <= age and age <= 50:
#         print("You are Good, Enjoy!")
#     else:
#         bill = 12
#         print(f"You can go, The fees are: ${bill}!")
    
#     photo = bool(input("Do you want a photo (True|False)? "))
#     if photo == True:
#         bill+=3
#         print("Your Bill is: $")
# else:
#     print("Sorry, you can't got!")

### Day 4 ###

#- RANDOMISATION #

## random.randint(a,b)
# import random #- MODULE
# random_integer = random.randint(1,10)
# print(random_integer)

#- CREATING MODULE #
# # checkout practive_new
# import random #- MODULE PYTHON DEFAULT
# import practice_new #- MODULE CREATED
# random_integer = random.randint(1,10)
# print(random_integer)
# print("New Module names practice_new has pi variable --> ",practice_new.pi)


## random.random
# import random
# random_number_0_to_1 = random.random() # *10 one digit on the left of the decimal shown. 
# print(random_number_0_to_1)

## random.uniform(a,b) - may get upper bound or not.
# random_number_0_to_1 = random.uniform(1,10)
# print(random_number_0_to_1)

# Heads or Tails
# coin = random.randint(0,1)
# if coin == 1:
#     print("Tails!")
# else:
#     print("Heads!")
# print("Coin Value",coin)

#- LIST #
# fruits = ['cherry','apple']
# print(fruits[0])

# # Change
# fruits[0]='banana'
# print(fruits[0])

# # Append
# fruits.append('pineapple')
# print(fruits[2])

# # Extend
# fruits.extend(['greenapple','mango'])
# print(fruits)

# Who will pay the Bill?
# friends = ['killol', 'meet', 'arjun', 'manish', 'avinash', 'jay', 'prit']
# print("Bill will be paid by --> ", random.choice(friends)) # Method 1
# print("Bill will be paid by --> ", friends[random.randint(0,6)]) # Method 2

# Index Out of Range Error - when we print more than the number of indexes, ((( length of list - 1 = number of index )))


#- Nested Lists #
# dirty_dozen = ['apple','banana', 'pineapple', 'carrot', 'spinach']

# fruits = ['apple','banana', 'pineapple']
# veggies = ['carrot', 'spinach']

# dirty_dozen = [fruits,veggies]
# print(dirty_dozen)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1]) # Index 1 of the list's list's first index entry is printed

### Day 5 ###


#- LOOPS #

## For Loop
# fruits = ['apple','banana','mango']

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie\n")
# print(fruits) # Indentation is Important

## Highest Score
student_scores = [1,2,3,4,5,6,7,8,9,10]

## Summation "sum"
# total_sum = sum(student_scores) # Automatic
# print(total_sum)

# sum=0 # Manual
# for score in student_scores:
#     sum+=score
# print(sum)

## Maximum "max"
# maximum = max(student_scores) # Automatic
# print(maximum)

# max=0 # Manual
# for score in student_scores:
#     if score>max:
#         max=score
# print(max)


#- RANGE #

# for number in range(1,10,2): # Last Number is Excluded. Ex:- only print till 9 # After higher limit, Step is added
#     print(number)

## 1 to 100 sum using code
# sum=0
# for number in range(1,101):
#     sum+=number
# print(sum)

## Coding Exercise
# num=0
# for num in range(1,101):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)

