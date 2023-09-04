from textbase import bot, Message
from textbase.models import OpenAI
from textbase import models
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "API_KEY"

# Prompt for GPT-3.5 Turbo
'''SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like.
The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a
pleasant chat!
"""'''
SYSTEM_PROMPT = ["Hi, I'm your personal fashion assistant. How can I help you today"]
preference = {}
@bot()
def on_message(message_history: List[Message], state: dict = None):

    user_message=message_history[-1]['content']

    if any(keyword in user_message for keyword in ["fashion", "outfit"]):
        message_history.append({"role":"assistant","content":bot_response})

    else:
        bot_response = generate_outfit(user_message,message_history)


    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }

def generate_outfit(user_message,message_history):
    response = OpenAI.generate(
        model="gpt-3.5-turbo",
        system_prompt=f"{SYSTEM_PROMPT}\nUser: {user_message}\n",
        message_history=message_history,
        max_tokens=50,  # Adjust the response length as needed
        temperature=0.7,  # Adjust the temperature for response creativity
    )

    return response

