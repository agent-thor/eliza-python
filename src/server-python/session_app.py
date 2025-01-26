# server.py
from flask import Flask, request, jsonify
from agent_session import Session
import os

app = Flask(__name__)

@app.route("/create_session", methods=["POST"])
def create_session():
    try:
        data = request.json
        character_file = data.get("character_file")
        env_file = data.get("env_file")
        api_key = data.get("api_key")

        if not (character_file and env_file and api_key):
            return jsonify({"error": "character_file, env_file, and api_key are required."}), 400

        session = Session(character_file, env_file, api_key)
        result = session.create_session()
        return jsonify(result), 201

    except FileExistsError as e:
        return jsonify({"error": str(e)}), 409
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
