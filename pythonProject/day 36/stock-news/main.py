import json
import datetime as DT
from datetime import timedelta
import html
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = 'AC55f4b44f413ce614e738bb331bcad369'
auth_token = '9bfb9458851430bed044704341ba553b'


date_time = DT.datetime.now()
today_date = date_time.date()
yesterday = today_date - timedelta(days = 1)
stock_opening = f"{yesterday} 05:00:00"
stock_closing = f"{yesterday} 20:00:00"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_price_api_key = "2O3T5LPR794PZEM0"
url_stock_price = "https://www.alphavantage.co/query?"
parameters = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":"TSLA",
    "interval":"60min",
    "apikey":stock_price_api_key,
}
request_stock_data = requests.get(url=url_stock_price,params=parameters)
tsla_stock_data = request_stock_data.json()
stock_opening_data = float(request_stock_data.json()["Time Series (60min)"][stock_opening]["1. open"])
stock_closing_data = float(request_stock_data.json()["Time Series (60min)"][stock_closing]["4. close"])
if stock_closing_data > stock_opening_data :
    stock_difference = stock_closing_data - stock_opening_data
    percent_stock_difference = (stock_difference / stock_opening_data)*100
    x = f"TSLA: 🔺{round(percent_stock_difference)}%"
else:
    stock_difference= stock_opening_data - stock_closing_data
    percent_stock_difference = (stock_difference / stock_opening_data) * 100
    x = f"TSLA: 🔻{round(percent_stock_difference)}%"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_api_key = "608b7ba9a1024f66a46fefdad44b38bc"
url_news = "https://newsapi.org/v2/everything?"
parameters_news = {
    "q":"tesla",
    "from":yesterday,
    "sortBy":"publishedAt",
    "apiKey":news_api_key,
}
get_news = requests.get(url=url_news,params=parameters_news)

news_title = html.unescape(get_news.json()["articles"][0]["title"])
news_description = html.unescape(get_news.json()["articles"][0]["description"])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body=f"{x}\nHeadline: {news_title}\nDescription: {news_description}f️",
    from_='+17744694204',
    to='+919829657691',
)

print(message.status)

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

