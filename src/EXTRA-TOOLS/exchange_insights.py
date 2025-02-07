import requests
from bs4 import BeautifulSoup
import httpx
import time
# INFORMATION ABOUT EXCHANGE

def exchange(project_name):
    main_url=f"https://www.binance.com/en-IN/research/projects/{project_name}"
    try:
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}   
        # Send a GET request to the webpage
        response = httpx.get(main_url, headers=headers,follow_redirects=True)

        # Check if the request was successful
        print(response.status_code)
            
        if response.status_code == 202:
            # Parse the HTML content
            time.sleep(10)
            print(response.content)
            response = requests.get(main_url)

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract content from <span> tags
            span_content = soup.find_all('span',{"data-bn-type":"text"})
            span_texts = [span.get_text() for span in span_content]
            


            link_element = soup.find('a', {'data-bn-type': 'link'})
            print("_________________________________________________________________")
            print("PDF Link:")
            print(link_element.get('href'))
            print()
            print("\n".join(span_texts))
                    

        else:
            return f"Failed to retrieve webpage. Status code: {response.status_code}"
    except:
        return f"Failed to retrieve webpage"
    

if __name__=="__main__":
    
    exchange("bio-protocol")
