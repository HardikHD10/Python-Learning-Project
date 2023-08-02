print(int(8/3))
print(round(8/3))
print(round(2.6666666666, 2))
print(8//3)         # data type is integer

R = 4/2
R /= 2
print(R)
height = 1.8
isWinning = True
# f -string
print(f"your score is {R},your height is {height}, you are winning is {isWinning}")

# challenge 2.3
age = input("what is your current age?\n")
AGE = int(age)
days = (90 - AGE) * 365
months = (90 - AGE) * 12
weeks = (90 - AGE) * 52
print(f"You have {days} days, {weeks} weeks and {months} months left ")

