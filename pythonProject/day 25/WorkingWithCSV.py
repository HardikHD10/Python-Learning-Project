# with open("weather_data.csv","r") as weatherdata :
#     data = weatherdata.readlines()

# import csv
# with open("weather_data.csv") as weatherdata:
#     data = csv.reader(weatherdata)
#     tempratures = []
#     for row in data :
#         if row[1] != "temp" :
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))


# avg_temp = ("%.2f" % round(sum(temp_list)/float(len(temp_list)),2))
# print(avg_temp)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
# print(data.condition[0])

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(int(monday.temp))
# print((int((monday.temp * 9)) / 5) + 32)

#create a data frame from scratch
# data_dict ={
#     "Students" : ["Amy","Jason","Angela"],
#     "scores" : [76,56,65]
# }
# DATA = pandas.DataFrame(data_dict)
# print(DATA)
# DATA.to_csv("new_data.csv")

# Gray, Cinnamon, Black
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_squirrels = len(data[data["PrimaryFurColor"]== "Gray"])
Cinnamon_squirrels = len(data[data["PrimaryFurColor"]== "Cinnamon"])
Black__squirrels = len(data[data["PrimaryFurColor"]== "Black"])

Data_dict = {
    "FUR COLOR" : ["Gray","Cinnamon","Black"],
    "COUNT":[Gray_squirrels,Cinnamon_squirrels,Black__squirrels]
}

DATA = pandas.DataFrame(Data_dict)
print(DATA)
DATA.to_csv("SQUIRREL_COUNT.csv")


