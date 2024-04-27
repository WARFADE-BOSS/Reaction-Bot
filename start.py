from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start():
    chat_id = request.json['message']['chat']['id']
    bot_message = "Hello! I'm your Telegram bot. How can I assist you today?"
    send_message(chat_id, bot_message)
    return 'OK'

def send_message(chat_id, message):
    bot_token = os.getenv('BOT_TOKEN')
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
  
