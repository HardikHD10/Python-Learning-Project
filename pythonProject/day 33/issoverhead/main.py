import time

import requests
from datetime import datetime
import smtplib

MY_LAT =  25.288231
MY_LONG =  74.724869

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour
print(current_hour)

while True:
    time.sleep(60)
    if ((iss_latitude < MY_LAT + 5 and iss_latitude > MY_LAT - 5) and (iss_longitude < MY_LONG + 5 and iss_longitude > MY_LONG - 5)) and (current_hour > sunset or current_hour < sunrise) :
        message = random.choice(content)
        my_email = "schoolink06@gmail.com"
        my_password = "dbmkzougjjpnfvmy"

        connection = smtplib.SMTP("smtp.gmail.com", 587)

        connection.starttls()

        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email, to_addrs="hardikinani1007@gmail.com", msg=f"Subject:ISS Satellite\n\nLook Up!")

        connection.close()
    else :
        print("Please wait")



