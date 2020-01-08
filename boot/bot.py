import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

print("hola")

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Soc un bot bàsic.")

def ayuda(bot,update):
	informacio = open("informacio.txt").read().strip()
	bot.send_message(chat_id=update.message.chat_id, text=informacio)

def author(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="El autor es Ricardo López, email:ricardo.lopez@est.fib.upc.edu")

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start1', start))

dispatcher.add_handler(CommandHandler('author', author))

dispatcher.add_handler(CommandHandler('help', ayuda))

# engega el bot
updater.start_polling()