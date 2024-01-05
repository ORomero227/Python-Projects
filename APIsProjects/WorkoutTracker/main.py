import os
import requests
from datetime import datetime

APP_ID = os.environ.get("Nutritionix_APP_ID")
APP_KEY = os.environ.get("Nutritionix_APP_KEY")
SHEETY_AUTH = os.environ.get("Sheety_AUTH")
GENDER = "men"
WEIGHT_KG = 106.594
HEIGHT = 193.040
AGE = 21

# ----------------- End Points -------------------------------
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/8c6988acbee6f63efc489cb3e14038b4/workoutTracking/workouts"

# -------------- Nutritionix API requests --------------------

exercise_text = input("Tell me which exercises you did: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, headers=header, json=params)
exercise_result = response.json()

# ---------- Sheety API requests ---------------------------
current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().time().strftime("%I:%M %p")

header = {
    "Authorization": SHEETY_AUTH,
}

# Adding new row
for exercise in exercise_result["exercises"]:
    content = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(sheety_endpoint, headers=header, json=content)

    print(sheety_response.text)
