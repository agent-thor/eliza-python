import requests
from bs4 import BeautifulSoup


# INFORMATION ABOUT EXCHANGE

def exchange(project_name):
    main_url=f"https://www.binance.com/en-IN/research/projects/{project_name}"
    try:

        # Send a GET request to the webpage
        response = requests.get(main_url)

        # Check if the request was successful
        
            
        if response.status_code == 200:
            # Parse the HTML content
            response = requests.get(main_url)

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract content from <span> tags
            span_content = soup.find_all('span',{"data-bn-type":"text"})
            span_texts = [span.get_text() for span in span_content]
            


            link_element = soup.find('a', {'data-bn-type': 'link'})
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
