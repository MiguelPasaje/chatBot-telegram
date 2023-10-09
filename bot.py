import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print('->')
    print(message.text == '/start')
    if message.text == '/start':
        bot.reply_to(message, "Howdy, how are you doing?")
    else:
        bot.reply_to(message, "help")
		
		
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
bot.infinity_polling()