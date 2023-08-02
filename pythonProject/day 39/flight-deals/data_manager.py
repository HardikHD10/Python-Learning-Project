import requests

sheety_endpoint = "https://api.sheety.co/3319b0cf41747e4e8a2499d1172e54f4/flightDeals/prices"
# access_authorization ={
#     "Authorization":"Bearer 1343954892301r90238498319048129048210948239831081904830481",
# }
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)






