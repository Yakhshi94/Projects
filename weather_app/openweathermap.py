import requests
from twilio.rest import Client
import os
account_sid = os.environ.setdefault("ACCOUNT_SID", "AC3b05dda4fb8dfaa0d5dd15cb89b019be")
auth_token = os.environ.setdefault("auth_token", "1e8a1fde07332acf38a9942e7ebc12eb")

LAT = 36.7551
LONG = 66.8975
EXCLUDE = 'current,minutely,daily'
API_KEY = "5abdc3031838b38330969bb0c8d0303f"
END_POINT = f"https://api.openweathermap.org/data/2.5/onecall"
PARAMS = {'lat': LAT, 'lon': LONG, 'appid': API_KEY, 'exclude': EXCLUDE}
response = requests.get(END_POINT, params=PARAMS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False
for hourly in weather_slice:
    for w in hourly['weather']:
        if w['id'] <= 800:
            will_rain = True
        else:
            pass

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Get your umbrella today its gonna rain 🌧",
        from_='+14327772828',
        to='+93780972633'
    )
    print(message.status)
