import json


with open("intents.json", "r") as json_data:
    intents = json.load(json_data)


def get_tag(msg):
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if msg.lower() == pattern.lower():
                return intent["tag"]
    return "unkown"
