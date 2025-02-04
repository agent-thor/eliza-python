# server.py
from flask import Flask, request, jsonify
from agent_session import Session
from verify import ApiVerify
import sys
from pathlib import Path
import requests
sys.path.append(Path.cwd().parent)

#for terminal
current_file_path = Path(__file__).resolve()
project_root = current_file_path.parent.parent  # Adjust as necessary
print(project_root)

sys.path.append(str(project_root))

from utils import * 

app = Flask(__name__)

@app.route("/create_session", methods=["POST"])
def create_session():
    try:
        # Parse the incoming JSON data
        data = request.json

        # Extract characterJson and api_key from the payload
        character_json = data.get("character_file")
        api_key = data.get("api_key")

        # Validate required fields
        if not (character_json and api_key):
            return jsonify({"error": "characterJson and api_key are required."}), 400

        # Verify the API key
        verify_obj = ApiVerify()
        if not verify_obj.verify(api_key):
            return jsonify({"error": "Invalid API key."}), 403

        # Prepare the payload for the external API (only characterJson)
        payload = {
            "characterJson": character_json
        }
        
        print(character_json)
        # Make a POST request to the predefined URL
        eliza_start_url = load_config()['eliza_create']
        response = requests.post(eliza_start_url, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            return jsonify(response.json()), 201
        else:
            return jsonify({"error": "Failed to create session on external server.", "details": response.text}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/close_session", methods=["POST"])
def close_session():
    try:
        data = request.json
        api_key = data.get("api_key")

        if not api_key:
            return jsonify({"error": "api_key is required."}), 400

        session = Session(None, None, api_key)
        result = session.close_session()
        return jsonify(result), 200

    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure the sessions directory exists
    if not os.path.exists("sessions"):
        os.makedirs("sessions")

    app.run(debug=True)
