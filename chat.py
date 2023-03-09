import random
import json


from model import get_tag


with open("intents.json", "r") as json_data:
    intents = json.load(json_data)


bot_name = "Sam"

asked_questions_pk = list()
asked_questions_anuj = list()
ques_to_pk = [
    question
    for intent in intents["intents"]
    for question in intent["responses"]
    if intent["tag"] == "pk"
]
ques_to_anuj = [
    question
    for intent in intents["intents"]
    for question in intent["responses"]
    if intent["tag"] == "anuj"
]


def get_response(msg):
    tag = get_tag(msg)
    if tag != "unknown":
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                if intent["tag"] == "pk":
                    while len(ques_to_pk) > 0:
                        question = random.choice(ques_to_pk)
                        if question not in asked_questions_pk:
                            asked_questions_pk.append(question)
                            ques_to_pk.remove(question)
                            return question
                    if len(asked_questions_anuj) + len(asked_questions_pk) == 8:
                        return "That's all folks!"
                    return "No further questions for PK"
                elif intent["tag"] == "anuj":
                    while len(ques_to_anuj) > 0:
                        question = random.choice(ques_to_anuj)
                        if question not in asked_questions_anuj:
                            asked_questions_anuj.append(question)
                            ques_to_anuj.remove(question)
                            return question
                    if len(asked_questions_anuj) + len(asked_questions_pk) == 8:
                        return "That's all folks!"
                    return "No further questions for Anuj"
                else:
                    return random.choice(
                        intent["responses"]
                    )  # add logic to avoid repetition of questions

    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
