import sys
from pathlib import Path
sys.path.append(Path.cwd().parent)

# for terminal
current_file_path = Path(__file__).resolve()
project_root = current_file_path.parent.parent  # Adjust as necessary
print(project_root)

sys.path.append(str(project_root))

from utils import * 

class ApiVerify:
    def __init__(self):
        try:
            # Load the API key table during initialization
            self.api_key_table = load_json_file(load_config()['api_table'])
        except FileNotFoundError:
            print(f"Error: API key table not found.")
            self.api_key_table = {}
        except Exception as e:
            print(f"Error loading API key table: {e}")
            self.api_key_table = {}

    def verify(self, api_key):
        # Check if the API key exists in the list
        if api_key in self.api_key_table.values():
            return True
        else:
            return False
        