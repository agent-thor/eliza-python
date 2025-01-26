
import os 
import json

current_dir = os.getcwd()  # Get the current file's directory
config_dir = os.path.dirname(os.path.dirname(current_dir)) + '/config.json'

def load_json_file(file_path):
    """
    Load a JSON file and return its contents as a Python dictionary.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file.

    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} was not found.")

    # Load the JSON file
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            raise ValueError(f"The file at {file_path} is not a valid JSON.")
            
            
def load_config():
    config_file = load_json_file(config_dir)
    
    return config_file
    