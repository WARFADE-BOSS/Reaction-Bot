import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def send_message(chat_id, text):
    bot_token = os.getenv('BOT_TOKEN')
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/start', methods=['POST'])
def start():
    data = request.json
    chat_id = data['message']['chat']['id']
    user_name = data['message']['from']['first_name']
    welcome_message = f"Hello {user_name}! Welcome to the Emoji Reaction Bot. Use me to send random emoji reactions to your messages. Just send any message and watch the reaction!"
    send_message(chat_id, welcome_message)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
