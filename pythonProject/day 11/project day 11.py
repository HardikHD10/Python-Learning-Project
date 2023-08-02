import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def blackjack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    def deal_card():
        card = random.choice(cards)
        return card

    flag = True
    while(flag):
        user_concent = input("Do you want ot play black jack game or not ?.'y' or 'n'.\n")

        if user_concent == "y" :
            print(logo)
            user_card_1 = deal_card()
            user_card_2 = deal_card()

            computer_card_1 = deal_card()
            computer_card_2 = deal_card()

            sum_computer = computer_card_1 + computer_card_2

            sum_user = user_card_1 + user_card_2

            print(f"Your both cards are [{user_card_1},{user_card_2}] ")

            print(f"Computer's both cards are [{computer_card_1},X] ")

            user_input = input(f"Sum of your both cards is {sum_user}.Are you sure you want to pick another card.'y' or 'n'.\n").lower()

            if user_input == "y" :
                user_card_3 = deal_card()
                print(f"Your third card is {user_card_3}")
                sum_user += user_card_3
            print(f"sum of your all cards is {sum_user}.")

            if sum_computer < 17 :
                computer_card_3 = deal_card()
                sum_computer += computer_card_3
                print("computer picked another card!.")
                print(f"[computer cards =  {computer_card_1},{computer_card_2},{computer_card_3}] ")
            else:
                print(f"[computer cards = {computer_card_1},{computer_card_2}]")

            print(f"sum of computer cards is {sum_computer}")

            if sum_computer > 21 :
                print("Sum of computer cards is greater than 21. You win !")
            elif sum_user > 21 :
                print("Sum of your cards is greater than 21. You lose !")
            elif (sum_computer <= 21 and sum_user <= 21) and sum_user < sum_computer :
                print("Sum of your cards is less than sum of computer cards. You lose !")
            elif (sum_computer <= 21 and sum_user <= 21) and sum_computer < sum_user :
                print("Sum of your cards is greater than sum of computer cards. You win !")
            else:
                print("sum of your cards is equals to sum of computer cards. It's a Draw !")

        elif user_concent == "n":
            flag = False
            blackjack()
            clear()

blackjack()
