import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "592UIZS1ZBI2JZTT"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "7c924acca59d4109940f8271e394ac21"

ACCOUNT_SID = "AC3b05dda4fb8dfaa0d5dd15cb89b019be"
AUTH_TOKEN = "1e8a1fde07332acf38a9942e7ebc12eb"
TWILIO_NUM = "+14327772828"
RECEIVER_NUM = "+93780972633"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
stock_res = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_res.json()['Time Series (Daily)']
data_list = [value for (key,value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 5:
    up_down = "🆙"
else:
    up_down = "⏬"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
if abs(diff_percent) >= 1:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()['articles']
    three_articles = news_data[:3]
    formatted_news = [f"{COMPANY_NAME}: {up_down}{abs(diff_percent)}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for news in formatted_news:
        client.messages.create(
            body=news,
            from_=TWILIO_NUM,
            to=RECEIVER_NUM
        )

