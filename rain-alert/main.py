import requests
from twilio.rest import Client
import os


MY_LAT = 45.936829
MY_LONG = 6.090300
API_KEY = "API_KEY"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# Twilio
account_sid = 'ACCOUNT_SID'
auth_token = 'TOKEN'

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()


weather_id = weather_data['weather'][0]['id']

will_rain = False

if int(weather_id) > 100:
    will_rain = True
else:
    pass

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today",
        from_="NUMBER",
        to="ANOTHER_NUMBER",
    )

    print(message.status)

