# challenge 7.1

word_list = ["advark","baboon","camel"]

import random
word = random.choice(word_list)

guess = input("guess a letter :").lower()

for letter in word:
    if letter == guess:
        print("right")
    else:
        print("wrong")






