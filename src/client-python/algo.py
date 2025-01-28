
"""
Local run via API

"""
    
    
    
#server-side code
from agent import create_agent 
from utils import initialize_agent

weather_object = agent(plugin_name, api_key)
whatsapp_object = agent(whatsapp_plugin, api_key, number)

"""creating weather_object or whatsapp object will create a dict with key value pair
    {
     "plugin_name": 
         "api_key" : 
             "whatsapp_num": 
     }
"""


initialize = initialize_agent([weather_object, whatsapp_object])
initialize.start()
    #this will be a flask like terminal which will keep opened until the session is terminated




#our framework at client side
class agent(plugin_name, api_key):
    //create a json file from given plugin_name and api_key
    check if the info is sufficient or not for creating that agent
    if not give error otherwise create a json file.:
        

class agent_chat:
    def chat(query):
        //this will extract the address at which query needs to be sent
        local address
        local_address --> server address
        
        

        
"""
This code will be a server side where goat SDK is located and initailize_agent will be given in the form of API
"""
class initialize_agent(agent_object_list):
    for agent in agent_object_list:
            fill_info(agent)
            
    
    def fill_info(agent):
        actual_plugin = get_actual_plugin_name(agent['plugin_name'])
        create .env file(agent['api_key'])
        create_character_file(agent['plugin_name'])
        
        this .env file and character file will be placed in certain directory with id associated with it.
        when the session is ended, this file will be destroyed.
        
        prince make code such that it can start with the .env file at given folder and character file pointed at given folder.

    def start():
        address = create_session()
            create session will run the command with character file and will be hosted and return an address
        print(address)



"""
People at client side
"""
from agent_chat import chat
    weather = chat("what is the weather in Delhi")
    
            
            
        
"""
Prince work: create an API, make the code run with specific .env file and character file
problem is if 1000 people comes then 1000 session will be created.
--use a process manager like PM2
--Running in isolated environemnt like docker
--Load balancing
--Testing using Jmeter, Apache and use tools like prometheus, new relic for resource consumption.


aaryan work. you will be provided a json file
{
 "plugin_name" : 
a nested dictionary with 
api_key,
whatsapp number
 }
"""

agent(name, whatsapp_access_token, whatsapp_phone_number)

agent:
    agent1 : 
        agent2: 
            
            

Python SDK --> Server Hosted Eliza

agent --> Server hosted on Eliza


10 parallely 

1 -->twitter, solana
2 --> web search , binanace


Server -> 1 time host (.env, character file)

1 -> Twitter, solana
2 --> web search , binanace

user 1 form -> data --> Eliza -> Eliza running (session created --> Isolated)
user 2 form --> data --> Eliza -> Eliza 2nd session (isolated)



character_card 2_character
env_card 2_env


eliza1 = Eliza(env, character) --> 

Server 

###################
1. send .env and character file in json to the server
2. At server, there will be a script which will create a folder with session_id and inside that folder there will be 
    .env and character file.
3. After file will bre created an object will be created with that .env and character file.
4. session.close will close that object and remove that dir with the session_id
5. People first need to create session_id and cannot do with another session_id simultaneoulsy.
6. prevent duplicate creation of session_id with API keys.




###################
Eliza OS-->
server start

automated -->
BTC---> 90000 -> trade_binance()



.env --> start() o1 -> character file -> twitter plugin .env

o2 start() - c2 -> .env2 -> twitter plugin




    
    
