import requests
import datetime as datetime
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
TOKEN = os.environ["TOKEN"]

GENDER = os.environ["GENDER"]
WEIGHT = os.environ["WEIGHT"]
HEIGHT = os.environ["HEIGHT"]
AGE = os.environ["AGE"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": TOKEN
}

QUERY = input("Tell me which exercises you did: ")

request_body = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": 21
}

response = requests.post(url=exercise_endpoint, headers=headers, json=request_body)
result = response.json()
print(result)

Sheety_endpoint = "https://api.sheety.co/34a2c87e9b37d46066b80a08620c3f77/neoWorkouts/workouts"

today = datetime.datetime.today()
date_time = today.date()

auth_header = {
    "Authorization": "Bearer plpokjbv234567quq9j389ey783409876r5rxtcfgvhbjkn"
}

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": date_time.strftime("%d/%m/%Y"),
            "time": date_time.strftime("%H:%M:%S"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=Sheety_endpoint, json=sheet_inputs, headers=auth_header)
    print(sheet_response.text)
