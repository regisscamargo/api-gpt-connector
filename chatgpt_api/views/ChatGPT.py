
import openai 
import loguru
import json
import os

from chatgpt_api.constants import ACCESS_KEY_GPT
from chatgpt_api.helpers.tools import Tools
from chatgpt_api.error.exceptions import ExceptionNoteResponse
from flask import request, jsonify

class ChatGPTView:

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.client = openai.OpenAI(api_key=ACCESS_KEY_GPT) 
        self.tools = Tools()

    def send_message(self, message):
        self.tools.logger(f"ChatGPTView - Send Message user:{message['messages'][0]['content']}")

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": message['messages'][0]['content']},
                ]
            )

            self.tools.logger(f"Response: {response.choices[0].message.content}")
            return json.dumps({"response": response.choices[0].message.content}) 

        except ExceptionNoteResponse as e:
            self.tools.logger(f"Error: {e}")
            return json.dumps({"error": e.msg})



