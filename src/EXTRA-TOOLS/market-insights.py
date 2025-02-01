import requests
from bs4 import BeautifulSoup
import json
import os


# MONTHLY AND YEARLY MARKET INSIGHTS

def monthly_yearly(year,month=None):
    if month is None:
        main_url=f"https://www.binance.com/en-IN/research/analysis/full-year-{int(year)-1}-and-themes-for-{year}"
    else:
        main_url=f"https://www.binance.com/en-IN/research/analysis/monthly-market-insights-{year}-{month}"
    try:

        # Send a GET request to the webpage
        response = requests.get(main_url)

        # Check if the request was successful
        
            
        if response.status_code == 200:

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract content from <span> tags
            span_content = soup.find_all('span',{"data-bn-type":"text"})
            span_texts = [span.get_text() for span in span_content]
            

# Find the first <a> tag with the specified attribute
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
    
    monthly_yearly("2025","01")







    

# def manage_undo_file(new_data, file_path='undo.json'):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#             print(data)
#     else:
#         data = []

#     data.append(new_data)

#     if len(data) > 10:
#         data.pop(0)

#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)

# # Example usage
# new_json = {"example_key": "example_value"}
# manage_undo_file(new_json)


# def undo_last_action(file_path='undo.json'):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             data = json.load(file)
        
#         if data:
#             last_element = data.pop()
#             with open(file_path, 'w') as file:
#                 json.dump(data, file, indent=4)
#             return last_element
#         else:
#             return "No actions to undo."
#     else:
#         return "Undo file does not exist."

# # Example usage
# last_action = undo_last_action()
# print("Last action undone:", last_action)