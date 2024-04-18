import os
import telegram
from telegram.ext import Updater
import random

BOT_TOKEN = os.environ['BOT_TOKEN']

reactions = ['👍', '👎', '😂', '🎉', '🤔']

bot = telegram.Bot(token=BOT_TOKEN)

def react_to_message(update, context):
    if update.message:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        reaction = random.choice(reactions)
        bot.send_reaction(chat_id, message_id, reaction)

updater = telegram.Updater(token=BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(telegram.MessageHandler(telegram.Filters.all, react_to_message))

updater.start_polling()
updater.idle()
