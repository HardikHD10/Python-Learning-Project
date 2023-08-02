#dictionary
# programming_dictionary = {
#     "bug" : "an error in an program that prevents the program from running as expected",
#     "Function":"A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. Functions are used to perform certain actions, and they are important for reusing code: Define the code once, and use it many times.",
#     "Loop":"the action of doing something over and over again",
# }
# print(programming_dictionary["bug"])
#
# # edit an item in dictionary
# programming_dictionary["bug"] = "a moth in your computer"
# print(programming_dictionary["bug"])
#
# #create an empty dictionary
# empty_dictionary = {}
#
# #wipe an existing dictionary
# #programming_dictionary = {}
# #print(programming_dictionary)
#
# # loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#challenge 1
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores :
    if student_scores [key] >= 91 :
        student_grades [key] = "Outstanding"
    elif student_scores [key] >= 81 and student_scores [key] <= 90 :
        student_grades [key] = "Exceeds Expectations"
    elif student_scores [key] >= 71 and student_scores [key] <= 80 :
        student_grades [key] = "Acceptable"
    else :
        student_grades [key] = "fails"

# 🚨 Don't change the code below 👇
print(student_grades)


