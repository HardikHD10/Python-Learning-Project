states_of_america = ["delaware","Pennsylvania","new jersey"]
#print(states_of_america[0])
states_of_america.append("georgia")
#print(states_of_america)
states_of_america.extend(["connecticut", "massachusetts"])
#print(states_of_america)

# challenge 4.2
import random
#names_string = input("Give me everybody's name, seprated by comma!")
#names = names_string.split(", ")

#x = len(names)
#bill = random.randint(0, x-1)
#person_pays = names[bill]
#print(f"{person_pays} will pay the bill!")

# nested lists
# dirty_dozens = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears", "tomatoes", "celery", "spinach", "kale","potatoes"]
fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
vegetables = ["tomatoes", "celery", "spinach", "kale","potatoes"]
dirty_dozens = [fruits, vegetables]
# print(dirty_dozens[1][1])

# challenge 4.3
row1 = [" 🥸 "," 🥸 "," 🥸 "]
row2 = [" 🥸 "," 🥸 "," 🥸 "]
row3 = [" 🥸 "," 🥸 "," 🥸 "]
maps = [row1 , row2 , row3 ]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

selected_row = maps[vertical - 1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")









