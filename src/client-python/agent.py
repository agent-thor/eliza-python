from utils import * 
import requests

config = load_config()

class Agent:
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)
    
        

    
        