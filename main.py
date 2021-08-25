import request
from datetime import datetime
import os


NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")     # 9b05beb1e370edb77e359f5679d43afd NUTRITIONIX_API_KEY
AGE = 26
WEIGHT_KG = 69
HEIGHT_CM = 180
GENDER = "Male"

nutritionix_exercice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": os.environ.get("x-app-id"),
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

nutritionx_parameters = {
    "query": input("Tell me which exercise you did: "),
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "gender": GENDER
}

response_nutritionx = requests.post(nutritionix_exercice_endpoint, json=nutritionx_parameters, headers=nutritionix_headers)
result = response_nutritionx.json()
print(result)

sheety_endpoint = os.environ.get("sheety_endpoint")

correct_date = datetime.now().strftime("%d/%m/%Y")
correct_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": correct_date,
            "time": correct_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response_sheety = requests.post(sheety_endpoint,
                                    json=sheety_parameters,
                                    auth=(os.environ.get("username"), os.environ.get("password")))
    print(response_sheety.text)
