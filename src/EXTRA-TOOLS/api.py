import json
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

USERS_FILE = "users.json"

# Load users from file
def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save users to file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

  # Load users on startup

class ConfigRequest(BaseModel):
    api_keys: Dict[str, str]

class SearchRequest(BaseModel):
    unique_id: str
    query: str

class UpdateRequest(BaseModel):
    api_keys:Dict[str,str]
    unique_id:str

@app.post("/configure")
async def configure(config: ConfigRequest):
    users=load_users()
    unique_id = str(uuid.uuid4())  # Generate unique identifier
    users[unique_id] = config.api_keys  # Store API keys
    save_users(users)  # Persist data
    return {"message": "Configuration successful", "unique_id": unique_id}


@app.post("/update")
async def update(config : UpdateRequest):
    users=load_users()
    for key,value in config.api_keys.items():
        users[config.unique_id][key]=value
    save_users(users)
    return {"message" : "Update successful"}




@app.post("/search")
async def search(request: SearchRequest):
    users=load_users()
    api_keys = users.get(request.unique_id)  # Retrieve stored API keys

    if not api_keys:
        raise HTTPException(status_code=404, detail="User not found")

    # Pass API keys directly instead of setting environment variables
    from main import PolkaToolSearch  # Adjust import if needed


    
    search_tool = PolkaToolSearch(
        api_keys=api_keys  # Use user-specific API key

    )

    result = search_tool.search(request.query)
    return {"query": request.query, "result": result}



# how to handle race conditions