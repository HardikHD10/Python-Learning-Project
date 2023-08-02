# for loop
fruits = ["apple","peach", "pear"]
for fruit in fruits:
    print(fruit)
    print( fruit + " pie")
print(fruits)

# challenge 5.1
students_heights = input("input a list of student heights.").split()
for n in range(0, len(students_heights)):
    students_heights[n]= int(students_heights[n])
print(students_heights)
total_height = 0
for height in students_heights:
    total_height += height
print(total_height)

number_students = 0
for student in students_heights:
    number_students += 1
print(number_students)

average_height = round(total_height/number_students)
print(average_height)

# challenge 5.2
student_score = input("input a list of student scores.").split()
for s in range(0, len(student_score)):
    student_score[s] = int(student_score[s])
print(student_score)

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score

print(f" highest score is score {highest_score}")

# for loop in range function()
for number in range(1,10,3):
    print(number)

total = 0
for r in range(1,101):
    total += r
print(total)

# challenge 5.3
sum = 0
for w in range(2,102,2):
    sum += w
print(sum)

# challenge 5,4
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0 :
        print("fizzbuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
        print(x)




