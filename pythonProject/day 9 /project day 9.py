logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
from replit import clear

dict = {}
flag = True
while (flag):
    name = input("What is you name?\n")
    bid = int(input("What is your bid in $?\n$"))
    dict[name] = bid

    user = input("Are there any more bidders?yes or no ?\n").lower()
    if(user=="no"):
        flag = False
    elif(user=="yes"):
        clear()

max = 0
for key in dict:
    if dict[key] > max:
        max = dict[key]
        max_key = key

print(f"Maximum bid {max} was made by {max_key}")
