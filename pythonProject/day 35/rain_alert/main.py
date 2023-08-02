import requests
from twilio.rest import Client


api_key = "dc6250ccf90b3cf91c708644b18364b3"
my_lat = 25.3407
my_long = 74.6313
account_sid = 'AC55f4b44f413ce614e738bb331bcad369'
auth_token = '9bfb9458851430bed044704341ba553b'

data = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={my_lat}&lon={my_long}&exclude=current,minutely,daily&appid={api_key}")
data.raise_for_status()
weather_data = data.json()
weather_slice = weather_data["hourly"][:24]

will_rain = False
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]['id'])
    if condition_code < 700 :
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="I will rain today. Please Bring an umbrella ☂️",
        from_='+17744694204',
        to='+919414055486',
    )

    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to be a sunny day 🔆",
        from_="+17744694204",
        to="+919829657691",
    )

    print(message.status)

