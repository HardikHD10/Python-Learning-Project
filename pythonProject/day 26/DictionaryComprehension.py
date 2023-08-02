# new_dict = {new_key : new_value for item in list}
# new_dict = {new_key : new_value for (key,value) in dict.items()}
import random

name = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
students_score = {item : random.randint(1,100) for item in name}
# print(students_score)
pass_student = {student : score for (student,score) in students_score.items() if score > 50}
# print(pass_student)

# challenge 1
sentence = "What is the airspeed Velocity of an Unladen Swallow?"

result = {item: len(item) for item in sentence.split()}
# print(result)

# challenge 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c*9/5)+32 for (day,temp_c) in weather_c.items()}
# print(weather_f)

import pandas
student_dict = {
    "Student" : ["Angela","James","Lily"],
    "Score" : [56,76,98]
}

Data = pandas.DataFrame(student_dict)
Data.to_csv("Data.csv")

# for (key, value) in Data.items():
#     print(value)

for(index, row) in Data.iterrows():
    if row.Student == "Angela" :
        print(row.Score)