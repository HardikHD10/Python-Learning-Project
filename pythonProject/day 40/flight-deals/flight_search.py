import requests
from flight_data import FlightData
api_key = "QginnzKHTaXtlS_NsCqnrO1COPLEBFr1"
url = "https://tequila-api.kiwi.com/locations/query"
class FlightSearch:
    def get_destination_code(self, city_name):
        headers={
            "apikey": api_key,
        }
        parameters={
            "term":city_name,
            "location_types":"city"

        }
        response = requests.get(url=url,params=parameters,headers=headers)
        data = response.json()
        self.code = data["locations"][0]["code"]
        return code

    def get_cheapest_flight(self,city_code):
        flight_data =FlightData()
        flight_end_point = flight_data.serach_url()
        search_parameters = {
            "fly_from": "city:LON",
            "fly_to": f"city:{city_code}",
            "date_from": flight_data.today(),
            "date_to": flight_data.six_month_date(),
            "curr": "INR",
            "sort": "price"
        }
        flight_headers = flight_data.flight_api()

        response =requests.get(url=flight_end_point,params=search_parameters,headers=flight_headers)
        data = response.json()["data"] [0]["price"]
        date = response.json()["data"] [0]["utc_departure"].split("T",1)[0]
        time = response.json()["data"] [0]["utc_departure"].split("T",1)[1].split(".",1)[0]

        string = f"Your Flight's cheapest price INR {data} is on date : {date}, departure timing: {time} in next six month."
        return string



