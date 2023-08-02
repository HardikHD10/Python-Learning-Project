# challenge 7.3

word_list = ["advark","baboon","camel"]

import random
word = random.choice(word_list)

print(f"the choosen word is {word}")

display = []
for _ in range(len(word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("guess a letter : ").lower()

    for position in range(len(word)):
        letter = word[position]
        #(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}\n")
        if letter == guess :
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win!")








