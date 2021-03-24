<h1>How to automate a Telegram-Bot with Python</h1>

Hello guys 👋, today we are going to automate a Telegram-Bot with Python. Before starting the tutorial you must have installed ```Python``` in your computer. Python can be installed through the [offical website of Python](https://python.org)


In this tutorial, we would be using ```python-telegram-bot``` package or further called *wrapper*. You can install the package via typing this text given below in your prefered terminal or CLI
```
pip install python-telegram-bot
```

So, let's start tutorial with ease. First install an IDE(Integrated Development Environment), use **IDLE** for beginners to Python. know the basics of Python before learning the tutorial. 

**i)** First of all, create a file named ```config.py``` in your IDE. Then, write the following code below.
The ```str``` TOKEN is to replaced by the token gave by [@botfather]()

```
bot_token = "TOKEN"
```

**ii)** Then, create a file named ```main.py```
in your IDE. Then, write the following code below.

```python
import telegram
from telegram.ext import *
from config import bot_token  
#config.py stores the the token safely 

bot = telegram.Bot(token=bot_token) 
# this above code initializes the bot
```
**iii)** Third step, add commands to ```main.py``` file. 

```python
def start_command(update,context): #add arguments named 'update' & 'context' 
    context.bot.send_message(chat_id=update.message.chat.id,text="Hello World!") 
    #update.message.chat.id is used to get chat id of upcoming message
```
**iv)** Last step, add another function called ```main()``` which handles the *Telegram-Bot* and run it by adding the  last statement of ```if``` which can run ```main()```. Now, your bot is ready to 
```python
def main():
    updater = Updater(token=bot_token) # handles control of bot
    dispatcher = updater.dispatcher # handles behavior of bot
    dispatcher.add_handler(CommandHandler('start', start_command)) # handles response  the named "Hello World!"
    updater.start_polling() # starts running
    updater.idle()# start running till intervals and waits for first response from user is /start

if __name__ == '__main__':
    main()
```
**v)** Now the whole code is looks like this -
```python
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
```
You can clone this repository by typing this command in your prefered terminal or CLI. Before cloning repository, Install the git. Git can be install from [offical website of Git]( http://git-scm.com/)

```
git clone https://github.com/adarsh4u218/How-to-automate-a-Telegram-Bot-with-Python
```


