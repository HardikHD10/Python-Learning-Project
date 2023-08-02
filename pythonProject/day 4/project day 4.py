A  = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors."))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if A == 0:
    print(rock)
    import random

    game = random.randint(0, 2)
    if game == 0:
        print(rock)
    elif game == 1:
        print(paper)
    else:
        print(scissors)

    if  game == 0:
        print("it's a draw!")
    elif game == 1 :
        print("you loose!")
    elif  game == 2:
        print("you win!")

elif A == 1:
    print(paper)
    import random

    game = random.randint(0, 2)
    if game == 0:
        print(rock)
    elif game == 1:
        print(paper)
    else:
        print(scissors)

    if   game == 0:
        print("you win!")
    elif  game == 1:
        print("it's a draw!")
    elif  game == 2:
        print("you loose!")

elif A == 2:
    print(scissors)
    import random

    game = random.randint(0, 2)
    if game == 0:
        print(rock)
    elif game == 1:
        print(paper)
    else:
        print(scissors)

    if A == 2 and game == 0:
        print("you loose!")
    elif A == 2 and game == 1:
        print("you win!")
    elif A == 2 and game == 2:
        print("it's a draw!")

else:
    print("invalid input!")





