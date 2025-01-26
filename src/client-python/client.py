from agent import Agent
from initialize_agent import InitializeAgent
from model import Model

ai_model = Model(model = "openai", OPENAI_API_KEY= '')

web_search_agent = Agent(name = "websearch", 
                         agent_name = 'plugin-web-search', 
                         TAVILY_API_KEY='',
                         model = ai_model
                            )

initialize_agent = InitializeAgent(agents = [web_search_agent], API_KEY= "99999")
initialize_agent.start()
initialize_agent.close()
output = web_search_agent.send_query("what is the temperature in delhi")
print(output)







