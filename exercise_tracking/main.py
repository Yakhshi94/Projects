import requests
import os
from datetime import datetime

"""Exercise Tracking App Using NUTRITIONX, GOOGLE SHEET AND SHEETY API"""

GENDER = "Male"
WEIGHT_KG = 82
HEIGHT_CM = 1.8
AGE = 30

# setting environment variable for security
os.environ.setdefault("NUTRITIONIX_API_KEY", "a57588f054f7728ec193ea5b549d8859")
os.environ.setdefault("NUTRITIONIX_API_ID", "fc3cd8f6")
os.environ.setdefault("BEARER_HEADER", "Basic ZXNtYXR1bGxhaDp5YWtoc2hp")
# accessing environment variable
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_API_ID = os.environ.get("NUTRITIONIX_API_ID")

# APIs endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/13b071e8472f7111e532dec852e62b1c/exerciseSheet/workouts"

exercise_header = {
    'x-app-id': NUTRITIONIX_API_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}

exercise_text = input('Tell me which exercise you did ?')

exercise_params = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

# pass user's input to nutritionx NLP and get the result
exercise_result = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_header).json()
print(exercise_result)

# get and convert date as 20/07/2023
today = datetime.now().strftime("%d/%m/%Y")
# get current formated time
time = datetime.now().strftime("%X")
bearer_header = {
    "Authorization": os.environ.get('BEARER_HEADER')
}
# loop and pass each workout records to sheety_endpoint which will insert it to google sheet
for exercise in exercise_result['exercises']:
    workout_records = {
        'workout': {
            "date": today,
            "time": time,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    resp = requests.post(url=sheety_endpoint, json=workout_records, headers=bearer_header)
    print(resp.text)


