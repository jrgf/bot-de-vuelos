import requests
import time
from telegram import ChatAction,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater,CommandHandler,ConversationHandler

def start(update,context):
    update.message.replay_text('Bienvenido a Flight Master el mejor bot \n Para encontrar vuelos baratos hacia cualquier parte del mundo')
    


if __name__ == "__main__":
    updater = Updater(token = '5588711197:AAEVOHd8BAxkT64VPptEDG7OKCFZhBpvYxE',use_context= True)
    dp = updater.dispatcher
     
                    
    updater.start_polling()
    updater.idle()