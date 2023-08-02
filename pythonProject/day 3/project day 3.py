# project day 3
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the treasure island!")
print("Your mission here is to find treasure.")
road = input("You're at a cross road where do you want to go? type 'left' or 'right'.\n").lower()
if road == "left":
    lake = input( "You came to a lake.There is an island in middle of the lake.Type 'wait' to wait for boat. type 'swim' to swim across. \n ").lower()
    if lake == "swim":
        door = input("you arrived at the island unharmed! please choose a door to reach treasure! 'red', 'yellow' or 'blue'.\n ").lower()
        if door == 'red':
            print("you fell into fire! game over!")
        elif door == 'yellow':
            print("congratulations! you won")
        elif door == 'blue':
            print("you fell into sea! game over.")
        else:
            print("door doesn't exist!!")
    else:
        print("your ship sank! game over!")
else:
    print("you fell in a hole! game over!")