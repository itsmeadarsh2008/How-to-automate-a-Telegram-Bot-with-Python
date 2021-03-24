import telegram
from telegram.ext import *
from config import bot_token
#config.py stores the the token safely 

bot = telegram.Bot(token=bot_token) 
# this above code initializes the bot

def start_command(update,context): #add arguments named 'update' & 'context' 
    context.bot.send_message(chat_id=update.message.chat.id,text="Hello World!") 
    #update.message.chat.id is used to get chat id of upcoming message

def main():
    updater = Updater(token=bot_token) # handles control of bot
    dispatcher = updater.dispatcher # handles behavior of bot
    dispatcher.add_handler(CommandHandler('start', start_command)) # handles the response named "Hello World!"
    updater.start_polling() # starts running
    updater.idle()# start running till intervals and waits for first response from user is /start

if __name__ == '__main__':
    main()