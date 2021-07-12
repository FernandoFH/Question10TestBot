from telegram.ext import Updater, CommandHandler 
from dotenv import load_dotenv
import os

def start(update, context):
    update.message.reply_text('Test Bot!')

if __name__ == "__main__":
    load_dotenv()
    updater = Updater(token=os.getenv('TELEGRAM_TOKEN'))
    dispatcher = updater.dispatcher
    print("Bot started") 

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    updater.start_polling()
    updater.idle()