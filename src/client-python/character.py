class GenerateCharacter:
    def __init__(self, agents):
        self.agents = agents

    def get_character_info(self):
        character_json = {}

        # Initialize fields with empty lists
        fields = {
            "plugins": [],
            "modelProvider": [],
            "clients": [],
            "bio": [],
            "lore": [],
            "knowledge": [],
            "messageExamples": [],
            "postExamples": [],
            "topics": [],
            "style": [],
            "adjectives": []
        }

        # Iterate through agents and populate fields
        for agent in self.agents:
            try:
                fields["plugins"].append(f'@elizaos/{getattr(agent, "agent_name", "")}')
                fields["modelProvider"].append(str(getattr(agent.model, "model", "")))
                fields["clients"].append(str(getattr(agent, "client", "")))
                fields["bio"].extend(getattr(agent.model, "bio", []))  # Extend for lists
                fields["lore"].extend(getattr(agent.model, "lore", []))
                fields["knowledge"].extend(getattr(agent.model, "knowledge", []))
                fields["messageExamples"].extend(getattr(agent.model, "messageExamples", []))
                fields["postExamples"].extend(getattr(agent.model, "postExamples", []))
                fields["topics"].extend(getattr(agent.model, "topics", []))
                fields["style"].append(getattr(agent.model, "style", {}))  # Assuming style is a dict or structured object
                fields["adjectives"].extend(getattr(agent.model, "adjectives", []))
            except Exception as e:
                # Log or handle specific exceptions if needed
                continue

        # Deduplicate fields where necessary
        character_json["plugins"] = list(set(fields["plugins"]))
        character_json["modelProvider"] = list(set(fields["modelProvider"]))
        character_json["clients"] = list(set(fields["clients"]))
        character_json["bio"] = list(set(fields["bio"]))
        character_json["lore"] = list(set(fields["lore"]))
        character_json["knowledge"] = list(set(fields["knowledge"]))
        character_json["messageExamples"] = fields["messageExamples"]  # Deduplicate complex structures
        character_json["postExamples"] = list(set(fields["postExamples"]))
        character_json["topics"] = list(set(fields["topics"]))
        character_json["style"] = {"style": fields["style"]}  # Adding as a dictionary
        character_json["adjectives"] = list(set(fields["adjectives"]))

        # Check if the required fields are populated
        if not character_json["plugins"] or not character_json["modelProvider"]:
            raise ValueError("Not sufficient plugins or models")

        return character_json
