import json


with open("intents.json", "r") as json_data:
    intents = json.load(json_data)


# for intent in intents["intents"]:
#     print(intent)
#     print("tag " + intent["tag"])
#     if not intent["tag"].startswith("questions"):
#         for response in intent["responses"]:
#             # print("pattern: " + pattern)
#             print("response: " + response)


ques_to_pk = [
    question
    for intent in intents["intents"]
    for question in intent["responses"]
    if intent["tag"] == "pk"
]
print(ques_to_pk)
ques_to_anuj = [
    question
    for intent in intents["intents"]
    for question in intent["responses"]
    if intent["tag"] == "anuj"
]
print(ques_to_anuj)