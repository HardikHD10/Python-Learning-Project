import random
random_integer = random.randint(100,200)
print(random_integer)

random_float = random.random()       # [0,1)
print(random_float)

#0.0000000 - 0.99999999
random_float * 5

love_score = random.randint(1,100)
print(f"your love score is {love_score}")

# challenge 4.1
import random
toss = random.randint(0,1)
if toss == 0 :
    print("its a heads !")
else:
    print("its a tails !")

