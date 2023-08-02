import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

GENDER = "Male"
WEIGHT_KG = "70"
HEIGHT_CM = "176"
AGE = "19"

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/3319b0cf41747e4e8a2499d1172e54f4/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

access_authoriztion ={
    "Authorization":"Bearer 34598103245005246054203",
}
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=access_authoriztion)

    print(sheet_response.text)