import random

print("Welcome to the Number Guessing Game !")

print("I am guessing a number between 1 to 100.")
Number = random.randint(1,100)

difficulty_level = input("Choose a difficulty level: 'easy' or 'hard': ").lower()

def game(lives):
    flag = True
    while(flag):
        user_input = int(input("Guess a nummber between 1 to 100 :\n"))
        if user_input == Number:
            print("You guessed the number correctly! You win !")
            flag = False
        elif user_input != Number:
            lives -= 1
            print(f"Try left : {lives}")
            if Number < user_input :
                print("Too High !")
            elif Number > user_input :
                print("Too Low !")
        if lives == 0 :
            print("No try left ! You lose ! ")
            flag = False

if difficulty_level == "easy":
    game(10)
elif difficulty_level == "hard":
    game(5)

