import os
import openai

class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPEN AI API")


    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="text-davinci-003",
            prompt = user_input,
            max_tokens = 3000,
            temprature = 0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Hi How are you")
    print(response)