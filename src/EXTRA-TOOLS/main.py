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
load_dotenv()

client = chromadb.PersistentClient("/home/aryan/MY_PROJECTS/POLK/eliza-python/src/EXTRA-TOOLS")
collection_name = "polka_tools"
collection = client.get_or_create_collection(name=collection_name)

genai.configure(api_key=os.getenv("API_KEY"))

with open('/home/aryan/MY_PROJECTS/POLK/eliza-python/src/EXTRA-TOOLS/composio.json', 'r') as file:
    data = json.load(file)


def search(query:str):
    # for enum,desc in data.items():
            
    #         result = genai.embed_content(
    #         model="models/text-embedding-004",
    #         content=desc
    #     )
    #         embedding = result['embedding']
    #     # Generate combined embedding
    #         collection.add(
    #             documents=[desc],
    #             embeddings=[embedding],
    #             metadatas=[{
    #                 "enum": enum
    #             }],
    #             ids=[enum]
    #         )

        # Step 2: Combine user query with their needs
    user_query = query
    # Generate embedding for the query
    query_result = genai.embed_content(
        model="models/text-embedding-004",
        content=user_query
    )
    query_embedding =query_result['embedding']
    # Step 3: Perform semantic search in ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

# Step 4: Extract and return the top-k jewelry IDs
    if "ids" not in results or not results["ids"]:
        print("not found")

    top_tool = [id for id in results["ids"]][0]
    func_name=top_tool[0]




    print()
    print("CALLING FUNCTION :", func_name)
    print()
    try:

        
        signature = inspect.signature(globals()[func_name])
        params = signature.parameters
        args = {}
        for name, param in params.items():
            if param.default is inspect.Parameter.empty:
                args[name] = input(f"Enter value for '{name}': ")  # Required argument
            else:
                value = input(f"Enter value for '{name}' (Press Enter to use default {param.default}): ")
                args[name] = value if value else param.default  # Use default if no input

        print(globals()[func_name](**args))
    except:
        print("Function not found")






search("i want latest price of bitcoin ")


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

