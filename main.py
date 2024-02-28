import os

import requests
from datetime import datetime


APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "Content-type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
# user input
exercise = input("Tell me which exercises you did: ")

body = {
    "query": exercise
}

response = requests.post(url=nutrition_endpoint, json=body, headers=headers)
data = response.json()["exercises"]
print(data)

sheetly_endpoint = "https://api.sheety.co/7dd2f589e67edda0fb26b95f701af3b3/workoutTracking/workouts"

sheetly_header = {
    "Authorization": "Basic SnVuaW9yTTpMdXJrJExpc3MxNA=="
}

for exercise in data:
    details = {
        "workout":
            {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
    }

    new_data = requests.post(url=sheetly_endpoint, json=details, headers=sheetly_header)
    print(new_data.text)


