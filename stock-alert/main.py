import requests
import os
from twilio.rest import Client


# CONSTANTS
STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "API_KEY"
STOCK_API_KEY = "STOCK_API_KEY"
TWILIO_SID = 'TWILIO_SID'
TWILI_OUTH_TOKEN = 'TWILIO_TOKEN'

# GET PRICES
stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY
    }
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]


yesterday = data_list[0]
yesterday_closing = float(yesterday["4. close"])
day_before = data_list[1]
day_before_closing = float(day_before["4. close"])

difference = yesterday_closing - day_before_closing

up_or_down = None
if difference > 0:
    up_or_down = "⬆️"
else:
    up_or_down = "⬇️"

diff_percent = round((difference / yesterday_closing) * 100)

if abs(diff_percent) > 3:

    # GET NEWS
    parameters = {
            "q": COMPANY_NAME,
            "from": "2023-10-17",
            "to": "2023-10-17",
            "language": "en",
            "apikey": NEWS_API_KEY,
        }
    response = requests.get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    news = response.json()['articles']

    three_articles = news[0:3]

    formatted_articles = [f"{STOCK_NAME}: {up_or_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    # SEND IT AS SMS WITH TWILIO
    client = Client(TWILIO_SID, TWILI_OUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(body=article,
                    from_="SENDER",
                    to="RECEIVER",
                    )

        print(message.status)

