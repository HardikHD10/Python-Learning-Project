# scope
enemies = 1
def increase_enemies():
    enemies = 2
    print(enemies)

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#potion_strength

###### global score ######
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()

game()

#there is no block scope
game_level = 3
enemies = ["Skeleton","Zombie","Alien"]
if game_level < 5 :
    new_enemy = enemies[0]

print(new_enemy)

#modify global scope
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)

increase_enemies()
print(enemies)

# don't use this, use return statement instead #

