# Write your code below this line 👇

# print("Hello" + " Felix")

# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

# print("Day 1 - String Manipulation")
# print('String Concatenation is done with the "+" sign.')
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")

# ---------------------------------------------------------
# NESTED FUNCTION AND PRINT
# print("Hello " + input("what is your name?"))

# # NESTED FUNCTIONS

# print(len(input("what is your name?")))

#------------------------------------------------------------

# name = input("What is your name?");

# length = len(name);

# print(length);

# #----------------------------------

# # 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# c = a
# a = b
# b = c

# #Write your code above this line 👆
# ####################################

# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)

# #----------------------------------

# #1. Create a greeting for your program.
# name = input('What is your name?\n')
# #2. Ask the user for the city that they grew up in.
# city = input(name + " what city did you grew up in?\n")
# #3. Ask the user for the name of a pet.
# pet = input(name + " what is the name of your pet?\n")
# #4. Combine the name of their city and pet and show them their band name.
# print("the name of your band name could be " + city + " " + pet)
# #5. Make sure the input cursor shows on a new line, see the example at:
# #   https://replit.com/@appbrewery/band-name-generator-end

#----------------------------------------------

#Data Types

# num_char = len(input("Waht is your name ?\n"))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters")

# a = 123

# print(type(a))

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# print(int(two_digit_number[0]) + int(two_digit_number[1]));

# # int() casting
# # to change  a string into a number
# # or
# #  we can cast using str() to convert a number into a string

#-----------------------------------------------------------------------------------

# PEMDAS ORDER ( PARENTHESIS , EXPONENT , MULTIPLICATION , DIVISION , ADDING , SUBSTRACT)  FROM LEFT OT RIGHT

# ()
# **
# * /
# + -

# -------------------BMI CALCULATOR

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# height_float = float(height)

# BMI = int(weight) / (height_float * height_float)

# print(int(BMI))

#--------------------------------------------

# floor division

print(8 // 3)  # it returns a integer without having to convert it

# round

print(round(8 / 3, 2))  # the 2 its the specification for the decimal places

#------------------------------------------
#F-STRING

score = 0
heigth = 1.74
isWinning = true
print(
    f"your score is {score}, your height is {heigth},  you are winning is {isWinning}"
)

# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_days
days_of_ninty = 90 * 365
age_on_days = int(age) * 365
total_days = days_of_ninty - age_on_days

weeks_of_ninty = 90 * 52
age_on_weeks = int(age) * 52
total_weeks = weeks_of_ninty - age_on_weeks

months_of_ninty = 90 * 12
age_on_months = int(age) * 12
total_months = months_of_ninty - age_on_months

print(
    f"You have {total_days} days. {total_weeks} weeks, and {total_months} months left"
)

#-----------------------------------------------------------
#------------------------TIP CALCULATOR-----------------

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill?\n $"))
tip = input("How much tip would you like to give ? 10, 12, or 15?")
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")
