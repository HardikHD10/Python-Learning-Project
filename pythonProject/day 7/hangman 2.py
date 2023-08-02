# challenge 7.2

word_list = ["advark","baboon","camel"]

import random
word = random.choice(word_list)

print(f"the choosen word is {word}")

display = []
for _ in word:
    display += "_"
print(display)

guess = input("guess a letter : ").lower()

for position in range(len(word)):
    letter = word[position]
    if letter == guess :
        display[position] = letter
print(display)



