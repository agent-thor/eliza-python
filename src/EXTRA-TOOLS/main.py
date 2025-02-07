from alphavantage import news_sentiment, currency_exchange_rates, historical_time_series, intraday_time_series, insider_transactions
from exchange_insights import exchange
from market_insights import monthly_yearly
from news import real_time_price, get_news
from analysis import analysis
import chromadb
import json
import google.generativeai as genai
from dotenv import load_dotenv
import os
import inspect
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()

class PolkaToolSearch:
    def __init__(self, api_keys, model_name="gemini-2.0-flash",natural_language_response=False):
        self.client = chromadb.PersistentClient("/home/aryan/MY_PROJECTS/POLK/eliza-python/src/EXTRA-TOOLS")
        self.collection = self.client.get_or_create_collection(name="polka_tools")
        try:
            genai.configure(api_key=api_keys.get("GEMINI"))
        except:
            print("NO key found for gemini")
            return "NO key found for gemini"
        self.api_keys=api_keys
        self.llm = genai.GenerativeModel(model_name=model_name)
        self.natural_language_response=natural_language_response
        with open(os.path.join("/home/aryan/MY_PROJECTS/POLK/eliza-python/src/EXTRA-TOOLS", "composio.json"), 'r') as file:
            self.data = json.load(file)

    def generate_embedding(self, content):
        """Generates an embedding for the given content."""
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=content
        )
        return result['embedding']

    def search(self, query: str):
        """Performs a semantic search in ChromaDB and calls the relevant function."""
        
        query_embedding = self.generate_embedding(query)
        results = self.collection.query(query_embeddings=[query_embedding], n_results=1)

        if "ids" not in results or not results["ids"]:
            print("No relevant tool found.")
            return
        
        func_name = results["ids"][0][0]  # Extract function name
        print(f"\nCALLING FUNCTION: {func_name}\n")

        try:
            signature = inspect.signature(globals()[func_name])
            inputs = inputs = {name: param.default if param.default is not inspect.Parameter.empty else None
          for name, param in signature.parameters.items()}

            print("inputs:" ,inputs)
            prompt = (
                f"for the given query, find out all the inputs which are available in the query, keep default inputs only of not available in query. Return a json response whose keys are the inputs and values are the user inputs from the query. the values for symbols are capitalized short forms . example :- BTC for bitcoin. keep keys as it is.  No preambles and postambles, keep all strings in double quotes.\n Inputs with their default values: {inputs}\n Query: {query}"
            )
            
            response = self.llm.generate_content([prompt], safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            })

            gemini_response = response.text[7:-4]  # Cleanup response
            # print(gemini_response)
            extracted_inputs = json.loads(gemini_response)
            
            print(self.api_keys)
            for req in inputs:
                if self.api_keys.get(req) is not None:
                    extracted_inputs[req]=self.api_keys.get(req)

            print(extracted_inputs)
            # Call function with extracted inputs
            out=globals()[func_name](**extracted_inputs)
            print(out)
            if not self.natural_language_response:
                return out
            else:
                return self.llm.generate_content([f"give output in natural language based on the given query and some data\nQuery:{query}\n Data:{out}\nIf data is not sufficient to answer the query, simply output insufficient data"], safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            }).text



        except Exception as e:
            # print("Error:", e)
            
            return f"Error: {e}"
            


# Usage
if __name__ == "__main__":
    api_keys={
        "GEMINI":os.getenv("GEMINI"),
        # "twelve":os.getenv("TWELVE_API"),
        # "alpha":os.getenv("ALPHA_VANTAGE")
    }
    search_tool = PolkaToolSearch(
        api_keys=api_keys
    )

    print(search_tool.search(" i want to retreve latest price of BTC"))




    # client = chromadb.PersistentClient("/home/aryan/MY_PROJECTS/POLK/eliza-python/src/EXTRA-TOOLS")
    # collection = client.get_or_create_collection(name="polka_tools")
    # with open(os.path.join("/home/aryan/MY_PROJECTS/POLK/eliza-python/src/EXTRA-TOOLS", "composio.json"), 'r') as file:
    #     data = json.load(file)
    # genai.configure(api_key=os.getenv("API_KEY"))
    # for key, value in data.items():
    #     embedding = genai.embed_content(model="models/text-embedding-004", content=value)
    #     collection.add(
    #         documents=[value],  
    #         embeddings=[embedding["embedding"]],
    #         ids=[key]
    #     )
        

        





#TO DO :-
# chromadb location ?
# new tools add , semantic collection
# delete faaltu functions from composio.json, create collection once again
# input possible? possible symbols?  (also not AUG, but need to convert to 08)
# how to give response to llm to get good natural language output ?
# clean function, remove comments
# json save what mongo?
# remove comments, structure code




#POSSIBLE QUERIES:-

# i want to get latest crypto news
# i want to retrieve latest BTC news and it's sentiments
# i want latest price of bitcoin
# i want some information about the exchange bio-protocol
# i want to get yearly crypto insights for 2024
# i want to get some research analysis under crypto
# i want to buy NFT
# i want to get insider information about transactions of bitcoin
# i want to get time series data of bitcoin
# i want to exchange BTC to ETH what are exchange rates



