import requests
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
'''This file will need to use the 
DataManager,FlightSearch, FlightData, NotificationManager classes 
to achieve the program requirements.'''

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"]=="":
    for row in sheet_data:
        row["iataCode"]=flight_search.get_destination_code(row["city"])
    print(f"Sheet Data = {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

print("Welcome to Hardik's Flight Club!")
print("We will get you best Flight Deals to Your destination cities.")
user_name = input("Please Enter your name : ")
user_email = input("Please Enter your email : ")
confirm_email = input("Please Enter your email again :")
if user_email != confirm_email:
    print("Both Email adresses Should be same!")
    user_email = input("Please Enter your email : ")
    confirm_email = input("Please Enter your email again :")

user_input = input("Choose the city you want to travel from London : 1.Paris\n2.Berlin\n3.Tokyo\n4.Sydney\n5.Istanbul\n6.Kuala Lumpur\n7.New York\n8.San Francisco\n9.Cape Town:\n").title()
for x in range(0,len(sheet_data)):
    if sheet_data[x]["city"] == user_input :
        code = sheet_data[x]["iataCode"]

print(code)
price_message = flight_search.get_cheapest_flight(code)
send_message = NotificationManager()
send_message.send_message_sms(price_message)
send_message.send_email(user_email,price_message)
print("Please Check your messages inbox and Email for the details!")


