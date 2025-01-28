from utils import * 
import requests

config = load_config()

class Agent:
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def get_parsed_response(self, response):
        text_output_list = []
        
        for list1 in response:
            text_output_list.append(list1['text'])
        
        return ''.join(text_output_list)

    
    def send_query(self, query):
        """
        Send a query to the Eliza API and return the response.
    
        :param query: The query text to send.
        :return: The API response as a dictionary.
        """
        # Get the full URL from the config file
        url = config['eliza_address']
        
        # Prepare the payload
        payload = {
            "text": query,
            "user": "user"
        }
        headers = {"Content-Type": "application/json"}
                
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            output = self.get_parsed_response(response.json())
                        
            return output # Return the JSON response directly
        except requests.exceptions.RequestException as e:
            # Handle request-related errors (e.g., network issues, invalid responses)
            return {"error": "Failed to send query.", "details": str(e)}
        except ValueError as e:
            # Handle JSON decoding errors
            return {"error": "Invalid response from the server.", "details": str(e)}
        

    
        