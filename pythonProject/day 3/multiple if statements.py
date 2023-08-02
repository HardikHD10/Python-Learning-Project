# multiple if statements
height = int(input("please enter your height in cm?\n"))
bill = 0

if height > 120:
    print("you can ride the roller coaster!")
    age = int(input("please enter your age?\n"))
    if age < 12:
        bill = 5
        print(" child tickets are $5")
    elif age >= 12 and age <= 18:
        bill = 7
        print("youth tickets are $7")
    elif age > 18:
        bill = 12
        print("adult tickets are $12")
    photo = input("do you want a photo taken? Y or N.")
    if photo == "Y":
        bill += 3
    print(f"your final bill is {bill}")

else:
     print("sorry! you can't ride the roller coaster!")

# challenge 3.4
print("Welcome to python pizza deliveries!")
size = input("What size of pizza do you want? S, M or L?")
add_pepperoni = input("do you want pepperoni? Y or N.")
extra_cheese = input("do you want extra cheese? Y or N.")
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")

# LOGICAL OPERATORS
height = int(input("please enter your height in cm?\n"))
bill = 0

if height > 120:
    print("you can ride the roller coaster!")
    age = int(input("please enter your age?\n"))
    if age < 12:
        bill = 5
        print(" child tickets are $5")
    elif age >= 12 and age <= 18:
        bill = 7
        print("youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("everything is going to be okay! have a free ride on us!")
    elif age > 18:
        bill = 12
        print("adult tickets are $12")
    photo = input("do you want a photo taken? Y or N.")
    if photo == "Y":
        bill += 3
    print(f"your final bill is {bill}")

else:
     print("sorry! you can't ride the roller coaster!")

# challenge 3.5
print("Welocome to the love caculator!")
name_1 = input("please enter your name: \n")
name_2 = input("please enter their name: \n")
combined_string = name_1 + name_2
N_1 = combined_string.lower()
t = N_1.count("t")
r = N_1.count("r")
u = N_1.count("u")
e = N_1.count("e")
l = N_1.count("l")
o = N_1.count("o")
v = N_1.count("v")

A = str(t+ r + u + e)
B = str(l + o + v + e)
C = int(A + B)

if C < 10 and C > 90 :
    print(f"Your score is {C}, you go together like coke and mentos.")
elif C > 40 and C < 50 :
    print(f"Your score is {C}, you are alright together.")
else:
    print(f"Your score is {C}")






