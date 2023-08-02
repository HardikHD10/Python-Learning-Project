# File not Found
# with open("a_file.txt") as file :
#      file.read()
# try:
#     file = open("a_file.txt")
#     a_dicitonary = {"key": "value"}
#     value = a_dicitonary["non_existent_key"]
#     print(value)
# except FileNotFoundError:
#     file = open("a_file.txt","a")
# except KeyError as errormsg:
#     print(f"key {errormsg} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is the error I made up")
# Key Error
# a_dicitonary = {"key":"value"}
# value = a_dicitonary["non_existent_key"]

#IndexError
# fruit_list = ["Apple","Banana","Pear"]
# print(fruit_list[3])

#typeError
# text = "abc"
# print(text + 5)

#try
#except
#else
#finally

# height = float(input("Height: "))
# weight = float(input("Weight: "))
# if height > 3 :
#     raise ValueError("Human height should not be over 3 meters.")
# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.

# try:
#     def make_pie(index):
#         fruit = fruits[index]
#         print(fruit + " pie")
#
#     make_pie(56)
# except IndexError:
#     print("Fruit Pie")


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
try :
    for post in facebook_posts:
        total_likes = total_likes + post['Likes']
except KeyError:
    #toal_likes += 0
    pass


print(total_likes)