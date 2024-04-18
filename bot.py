import os
import telegram
from telegram.ext import Updater, Queue
import random

BOT_TOKEN = os.environ['BOT_TOKEN']

reactions = ['👍', '👎', '😂', '🎉', '🤔']

bot = telegram.Bot(BOT_TOKEN)

def react_to_message(update, context):
    if update.message:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        reaction = random.choice(reactions)
        bot.send_reaction(chat_id, message_id, reaction)

update_queue = Queue()
updater = Updater(bot=bot, update_queue=update_queue)
dp = updater.dispatcher
dp.add_handler(telegram.MessageHandler(telegram.Filters.all, react_to_message))

updater.start_polling()
updater.idle()
