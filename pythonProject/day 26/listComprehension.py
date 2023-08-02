numbers = [1,2,3]
# new_item for item in list
new_list = [ n + 1 for n in numbers]
# print(new_list)
name = "Hardik"
new_list_2 = [letter for letter in name]
# print(new_list_2)

r = range(1,5)
new_list_3 = [n*2 for n in r]
# print(new_list_3)

#conditional list comprehension
# new_item for item in list if test
name = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
new_list_4 = [n for n in name if len(n) <= 4]
# print(new_list_4)

new_list_5 = [n.upper() for n in name if len(n) > 4]
# print(new_list_5)

# challenge 1
numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

#challenge 2
# result = [n for n in numbers if n % 2 == 0]
# print(result)

# challenge 3
with open("file1.txt") as file1 :
    content_1 = file1.readlines()

with open("file2.txt") as file2 :
    content_2 = file2.readlines()

common = [n for n in content_2 if n in content_1]
print(common)


