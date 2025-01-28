import json
import os
from utils import *
import requests
from character import GenerateCharacter

config = load_config()


class InitializeAgent:
    def __init__(self, agents, API_KEY):
        """
        Initialize the class with a list of agents.

        :param agents: A list of agent objects or dictionaries.
        :param API_KEY: The API key for authentication.
        """
        self.agents = agents
        self.API_KEY = API_KEY  # Explicitly assign API_KEY
        self.session_id = None  # Initialize session_id as None

    def display_agents(self):
        """Display details of all agents."""
        for agent in self.agents:
            if isinstance(agent, dict):
                print(f"Agent: {agent.get('name', 'Unknown')}, Attributes: {agent}")
            else:
                print(f"Agent: {agent.name}, Attributes: {agent.__dict__}")

    def generate_character_file(self):
        character_file = load_json_file(config['character_dir'])
        character = GenerateCharacter(self.agents)
        character_json = character.get_character_info()

        for key, value in character_json.items():
            if key in character_file:
                character_file[key] = value
        
        character_file["modelProvider"] = character_file["modelProvider"][0]

        return character_file

    def generate_env_file(self):
        env_file = load_json_file(config['env_dir'])

        for key in env_file.keys():
            for agent in self.agents:
                if hasattr(agent.model, key):
                    env_file[key] = getattr(agent.model, key)
                    
                elif hasattr(agent, key):
                    env_file[key] = getattr(agent, key)

        return env_file

    def start(self):
        """
        Start a new session by hitting the create_session API endpoint.
        Stores the session_id returned by the API.
        """
        character_file = self.generate_character_file()
        env_file = self.generate_env_file()

        session_address = config['session_address_create']
        payload = {
            "character_file": character_file,
            "env_file": env_file,
            "api_key": self.API_KEY
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(session_address, data=json.dumps(payload), headers=headers)

        if response.status_code == 201:
            print("Session created successfully!")
            response_data = response.json()
            self.session_id = response_data.get("session_id")  # Store the session_id
            print(response_data)
        elif response.status_code == 409:
            print("Error: Previous session is not closed.")
            print(response.json())
        else:
            print("An error occurred.")
            print(response.json())

    def close(self):
        """
        Close the session using the stored session_id.
        """
        if not self.session_id:
            character_file = self.generate_character_file()
            env_file = self.generate_env_file()

            session_address = config['session_address_create']
            payload = {
                "character_file": character_file,
                "env_file": env_file,
                "api_key": self.API_KEY
            }

            headers = {"Content-Type": "application/json"}
            
            session_id_response = requests.post(session_address, data=json.dumps(payload), headers=headers)
            session_id_response_data = session_id_response.json()
            
            if session_id_response.status_code == 500:
                return {"error": "No active session to close."}
            
            else:
                self.session_id = session_id_response_data.get("session_id")

        url = config['session_address_close']
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "api_key": self.API_KEY,
            "session_id": self.session_id  # Include the session_id in the payload
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            self.session_id = None  # Reset the session_id after closing
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}