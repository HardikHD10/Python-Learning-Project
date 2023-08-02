# Data types

# string

print("hello"[0])
print("hello"[4])

# integer

print(123 + 345)

# float
# 3.14159

# boolean
# True or False

num_char = len(input("what is your name?\n"))
# converting integer data type into string data type
new_num_char = str(num_char)
print("your name has" + new_num_char + "characters.")

a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

# challenge 2.1
two_digit_number = input("type a two digit number :\n")
number_1 = int(two_digit_number[0])
number_2 = int(two_digit_number[1])
print( number_1 + number_2)

print(type(int("5")/int(2.7)))
