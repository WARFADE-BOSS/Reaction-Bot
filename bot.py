import os
import telegram
import random
from telegram.ext import Updater, Dispatcher, MessageHandler, Filters

BOT_TOKEN = os.environ['BOT_TOKEN']

reactions = ['👍', '👎', '😂', '🎉', '🤔']

bot = telegram.Bot(token=BOT_TOKEN)

def react_to_message(update, context):
    if update.message:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        reaction = random.choice(reactions)
        bot.send_reaction(chat_id, message_id, reaction)

# Initialize the Dispatcher instead of Updater
dispatcher = Dispatcher(bot, None)

# Add handler to the Dispatcher
dispatcher.add_handler(MessageHandler(Filters.all, react_to_message))

# Start polling
dispatcher.start_polling()
dispatcher.idle()
