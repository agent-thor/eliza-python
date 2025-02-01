# api key = 
import requests
import json

def news_sentiments(tickers, topics, time_from):
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&topics=blockchain&time_from=20250101T0000&apikey=QBTFDLTF1YAH05GW'
    r = requests.get(url)
    data = r.json()

    print(json.dumps(data, indent=2))


#1. ABOVE -- News and it's sentiments, see more TOPICS and TICKERS in the documentation : https://www.alphavantage.co/documentation/#news-sentiment




def currency_exchange_rates(from_currency, to_currency):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey=QBTFDLTF1YAH05GW'
    r = requests.get(url)
    data = r.json()

    print(json.dumps(data, indent=2))

# 2. exchange rates from currency and to currency. See from , digital currence list.csv






def historical_time_series(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey=QBTFDLTF1YAH05GW'
    r = requests.get(url)
    data = r.json()

    print(json.dumps(data, indent=2))
# 3. HISTORICAL TIME SERIES (DAILY)
# remove (output size = full) to get this week data only



def intraday_time_series(symbol,interval_mins):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval_mins}min&apikey=QBTFDLTF1YAH05GW'
    #Query the most recent full 30 days of intraday data by setting outputsize=full
    r = requests.get(url)
    data = r.json()
    print(json.dumps(data, indent=2))


# 4. daily cryptocurrency time series  https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=EUR&apikey=demo





def insider_transactions(symbol):
    url = f'https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&symbol={symbol}&apikey=QBTFDLTF1YAH05GW'
    r = requests.get(url)
    data = r.json()

    print(json.dumps(data, indent=2))

# 5. This API returns the latest and historical insider transactions made be key stakeholders (e.g., founders, executives, board members, etc.) of a specific company.






#6. TICKER SEARCH USING KEYWORD
#https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=SAIC&apikey=demo






# 7. (what markets are open) ??
#https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=demo









# 8. need technical indicators ??






# 9. need analytics fixed and sliding ?





#10. Advanced Analytics (Fixed Window)
#This endpoint returns a rich set of advanced analytics metrics (e.g., total return, variance, auto-correlation, etc.) for a given time series over a fixed temporal window.
