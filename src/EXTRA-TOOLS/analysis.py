import requests
from bs4 import BeautifulSoup




def analysis(query=None):
    main_url=f"https://www.binance.com/en-IN/research/analysis"   #nstitutional-grade research reports, covering a broad range of topics in the digital asset industry such as blockchain, economics, and finance
    try:

        # Send a GET request to the webpage
        response = requests.get(main_url)

        # Check if the request was successful
        
            
        if response.status_code == 200:

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract content from <span> tags
            span_content = soup.find_all('div',{"data-bn-type":"text"})
            span_texts = [span.get_text() for span in span_content]
            


            
            print("\n".join(span_texts))
                    

        else:
            return f"Failed to retrieve webpage. Status code: {response.status_code}"
    except:
        return f"Failed to retrieve webpage"
    

if __name__=="__main__":
    
    print(analysis())
# put all article subjects into chromadb, scrape links and then do semantic search using user query