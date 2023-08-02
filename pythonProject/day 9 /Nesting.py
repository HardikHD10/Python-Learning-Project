#nesting list
# travel_log = {
#     "France":["Paris","lille","Dijon"],
#     "Germany":["Berlin","Hamburg","Stuttgart"]
# }
#
# list_in_list = ["A","B"["C","D"]]
#
# travel_log_2 = {
#     "France":{
#         "cities_visited_1":"Paris",
#         "cities_visited_2":"lille",
#         "cities_visited_3":"Dijon",
# },
#     "Germany":["Berlin","Hamburg","Stuttgart"]
# }
#
# # nesting a dictionary in a list
# travel_log_3 = [
#     {
#     "country" :"France",
#     "cities_visited" : ["Paris","lille","Dijon"],
#     "Germany":["Berlin","Hamburg","Stuttgart"]
#      }
# ]

# challenge 2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_name,visits,cities):
    new_country = {}
    new_country["country"]=country_name
    new_country["visits"]=visits
    new_country["cities"]=cities
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



