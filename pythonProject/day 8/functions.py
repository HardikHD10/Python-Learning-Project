# exercise 1
import math


def greet():
    print("Hi ")
    print("Hello ")
    print("How are you ")

greet()

#exercise 2
def greet_with_name(name):
    print("Hi " + name)
    print("Hello " + name)
    print("How are you "+ name)

greet_with_name("Hardik")

#exercise 3: fuction with more than one input
def greet_with(name,location):
    print(f"Hi {name} from {location}!")

greet_with("Hardik","Bhilwara")

greet_with(location="bhilwara",name="Hardik")

#exercise 4
def print_calc(hieght,width,cover):
    n = math.ceil((hieght * width) / cover)
    print(f"Number of cans required {n}")

test_h = int(input("Hieght of Wall : "))
test_w = int(input("Width of Wall : "))
coverage = 5
print_calc(hieght=test_h,width=test_w,cover=coverage)

#exercise 5
def prime_checker(number):
    flag = False
    if number > 1 :
        for i in range(2,number):
            if n % i == 0 :
                flag = True
                break

    if flag == True:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is prime number.")


n=int(input("Enter the number : "))
prime_checker(number=n)

