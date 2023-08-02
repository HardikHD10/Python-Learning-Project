#method 1 opening the file
# file = open("myfile.txt")
# contents = file.read()
# print(contents)
# file.close()

#method 2 opening and closing the file
# "a" for append mode
# "w" for write mode
# absolute file path :  /Users/hardik/Desktop/myfile.txt
# relative file path : ../../../Desktop/myfile.txt
with open("myfile.txt",mode="a") as file:
# contents = file.read()
# print(contents)
    file.write("\nThat's all about Jaipur.")

# creating a new file
with open("new_file.txt",mode="w") as file_2:
    file_2.write("Newly created File.")