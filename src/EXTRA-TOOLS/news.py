#crypto news
"https://techpoint.africa/crypto/"    #get articles subjects and link, then do semantic search using user query

import requests
from bs4 import BeautifulSoup
#ALL exchangge names



def get_news():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}   
    response = requests.get("https://techpoint.africa/crypto/",headers=headers)

        # Check if the request was successful
    print(response.status_code)
            
    if response.status_code == 200:

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all <a> inside <span class="ct-span">
        links = soup.select("span.ct-span a")

        # Print the href attributes
        for link in links:
            print()
            print(link['href'])




"https://api.twelvedata.com/cryptocurrency_exchanges?apikey=9973cacdafa04ea48dcd1208626138e9"



#symbol, available exchange for that symbol, currency base, currency quote

"https://api.twelvedata.com/cryptocurrencies?apikey=9973cacdafa04ea48dcd1208626138e9"



def real_time_price(symbol,twelve):
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={twelve}"
    r = requests.get(url)
    data = r.json()
    return data


# REAL TIME PRICE
"https://api.twelvedata.com/price?symbol=TRP&country=Canada&apikey=9973cacdafa04ea48dcd1208626138e9"


get_news()