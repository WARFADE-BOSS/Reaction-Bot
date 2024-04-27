import os
import random
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def send_reaction():
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = request.json.get('chat_id')
    message_id = request.json.get('message_id')

    my_emoji = ["❤", "🥰", "🤩", "😍", "❤‍🔥", "🤗", "😘"]
    do_emoji = random.choice(my_emoji)

    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [
            {
                "type": "emoji",
                "emoji": do_emoji,
                "is_big": True
            }
        ]
    }

    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/setMessageReaction", json=payload
    )

    return jsonify({"status": response.status_code})

if __name__ == '__main__':
    app.run(debug=True)
