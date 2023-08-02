# API location
# API Request
MY_LAT = 25.288231
MY_LONG = 74.724869
import requests,datetime
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
response.raise_for_status()
data = response.json()
data_1 = response.json()["iss_position"]
data_2 = response.json()["iss_position"]["longitude"]
data_3 = response.json()["iss_position"]["latitude"]
print(data)
iss_position = (data_2,data_3)
# print(data)
# print(data_1)
# print(data_2)
# print(iss_position)

### Response Code ###
# 1XX : Hold on
# 2XX : Here you go
# 3XX : Go Away
# 4XX : You Screwed Up
# 5XX : Server Screwed Up

# API parameter
parameter = {
    "lat":MY_LAT,
    "lang":MY_LONG,
    "formatted":0,
}
response_2 = requests.get("https://api.sunrise-sunset.org/json",params=parameter)
response_2.raise_for_status()
print(response_2.json())
sunrise = response_2.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response_2.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
# data_4 = response_2.json()
# print(data_4)
time_now = datetime.datetime.now()
print(time_now.hour)

