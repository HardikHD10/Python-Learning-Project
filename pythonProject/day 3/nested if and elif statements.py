# nested if/else statement
height = int(input("please enter your height in cm?\n"))

if height > 120:
    print("you can ride the roller coaster!")
    age = int(input("please enter your age?\n"))
    if age > 18:
        print(" please pay $12!")
    else:
        print("please pay $7!")
else:
     print("sorry! you can't ride the roller coaster!")

# elif statement
height = int(input("please enter your height in cm?\n"))

if height > 120:
    print("you can ride the roller coaster!")
    age = int(input("please enter your age?\n"))
    if age < 12:
        print(" please pay $5")
    elif age >= 12 and age <= 18:
        print("please pay $7")
    elif age > 18:
        print("please pay $12")
else:
     print("sorry! you can't ride the roller coaster!")

# challenge 3.2
height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in kg:\n"))
BMI = round(weight/(height**2))
if BMI < 18.5:
    print(f"your BMI is {BMI} and you are under weight!")
elif BMI < 25:
    print(f"your BMI is {BMI} and you are normal weight!")
elif  BMI < 30:
    print(f"your BMI is {BMI} and you are over weight!")
elif  BMI < 35:
    print(f"your BMI is {BMI} and you are obese!")
else:
    print(f"your BMI is {BMI} and you are clinically obese!")

# Challenge 3.3
year = int(input("which year do you want to check?\n"))

if year % 4 == 0 :
    if year % 100 == 0 and year % 400 == 0:
        print("it is a leap year!")
    elif year % 100 == 0 and year % 400 != 0:
        print("it is not a leap year!")
    else:
        print("it is a leap year!")
else:
    print("it is not a leap year!")





