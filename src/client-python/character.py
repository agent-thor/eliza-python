# class GenerateCharacter:
#     def __init__(self, agents):
#         self.agents = agents

#     def get_character_info(self):
#         character_json = {}

#         # Initialize fields with empty lists
#         fields = {
#             "plugins": [],
#             "modelProvider": [],
#             "clients": [],
#             "bio": [],
#             "lore": [],
#             "knowledge": [],
#             "messageExamples": [],
#             "postExamples": [],
#             "topics": [],
#             "style": [],
#             "adjectives": []
#         }

#         # Iterate through agents and populate fields
#         for agent in self.agents:
#             try:
#                 fields["plugins"].append(f'@elizaos/{getattr(agent, "agent_name", "")}')
#                 fields["modelProvider"].append(str(getattr(agent.model, "model", "")))
#                 fields["clients"].append(str(getattr(agent, "client", "")))
#                 fields["bio"].extend(getattr(agent.model, "bio", []))  # Extend for lists
#                 fields["lore"].extend(getattr(agent.model, "lore", []))
#                 fields["knowledge"].extend(getattr(agent.model, "knowledge", []))
#                 fields["messageExamples"].extend(getattr(agent.model, "messageExamples", []))
#                 fields["postExamples"].extend(getattr(agent.model, "postExamples", []))
#                 fields["topics"].extend(getattr(agent.model, "topics", []))
#                 fields["style"].append(getattr(agent.model, "style", {}))  # Assuming style is a dict or structured object
#                 fields["adjectives"].extend(getattr(agent.model, "adjectives", []))
#             except Exception as e:
#                 # Log or handle specific exceptions if needed
#                 continue

#         # Deduplicate fields where necessary
#         character_json["plugins"] = list(set(fields["plugins"]))
#         character_json["modelProvider"] = list(set(fields["modelProvider"]))
#         character_json["clients"] = list(set(fields["clients"]))
#         character_json["bio"] = list(set(fields["bio"]))
#         character_json["lore"] = list(set(fields["lore"]))
#         character_json["knowledge"] = list(set(fields["knowledge"]))
#         character_json["messageExamples"] = fields["messageExamples"]  # Deduplicate complex structures
#         character_json["postExamples"] = list(set(fields["postExamples"]))
#         character_json["topics"] = list(set(fields["topics"]))
#         character_json["style"] = {"style": fields["style"]}  # Adding as a dictionary
#         character_json["adjectives"] = list(set(fields["adjectives"]))

#         # Check if the required fields are populated
#         if not character_json["plugins"] or not character_json["modelProvider"]:
#             raise ValueError("Not sufficient plugins or models")

#         return character_json


import json

class GenerateCharacter:
    def __init__(self, agents):
        self.agents = agents

    def get_character_info(self):
        # Initialize the character JSON structure
        character_json = {
            "name": self.agents[0].name,  # Default name, can be modified dynamically
            "clients": [],
            "modelProvider": self.agents[0].model.model,  # Default model provider
            "settings": {
                "secrets": {},
                "voice": {"model": "en_US-male-medium"}
            },
            "plugins": [],
            "bio": [],
            "lore": [],
            "knowledge": [],
            "messageExamples": [],
            "postExamples": [],
            "topics": [],
            "style": {
                "all": [],
                "chat": [],
                "post": []
            },
            "adjectives": []
        }

        # Gather data from each agent
        for agent in self.agents:
            try:
                character_json["plugins"].append(f'@elizaos/{getattr(agent, "agent_name", "")}')
                character_json["clients"].extend(getattr(agent.model, "clients", []))
                character_json["bio"].extend(getattr(agent.model, "bio", []))
                character_json["lore"].extend(getattr(agent.model, "lore", []))
                character_json["knowledge"].extend(getattr(agent.model, "knowledge", []))
                character_json["messageExamples"].extend(getattr(agent.model, "messageExamples", []))
                character_json["postExamples"].extend(getattr(agent.model, "postExamples", []))
                character_json["topics"].extend(getattr(agent.model, "topics", []))
                
                # Handle styles as dictionary keys
                style_data = getattr(agent.model, "style", {})
                for key in ["all", "chat", "post"]:
                    if key in style_data:
                        character_json["style"][key].extend(style_data[key])
                
                character_json["adjectives"].extend(getattr(agent.model, "adjectives", []))
            except Exception:
                continue  # Optionally log the exception

        # Deduplicate lists to avoid redundancy
        character_json["plugins"] = list(set(character_json["plugins"]))
        character_json["clients"] = list(set(character_json["clients"]))
        character_json["bio"] = list(set(character_json["bio"]))
        character_json["lore"] = list(set(character_json["lore"]))
        character_json["knowledge"] = list(set(character_json["knowledge"]))
        # messageExamples often contain structured data; keep order or handle deduplication carefully
        character_json["messageExamples"] = character_json["messageExamples"]
        character_json["postExamples"] = list(set(character_json["postExamples"]))
        character_json["topics"] = list(set(character_json["topics"]))
        character_json["adjectives"] = list(set(character_json["adjectives"]))

        for key in ["all", "chat", "post"]:
            character_json["style"][key] = list(set(character_json["style"][key]))

        # Ensure required fields are present
        if not character_json["plugins"] or not character_json["modelProvider"]:
            raise ValueError("Not sufficient plugins or models")

        # Return valid JSON string with double quotes
        return character_json
