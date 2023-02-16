from flask import Flask, request
from telegram import Bot, Update
import os

TOKEN = os.environ["TOKEN"]

bot = Bot(TOKEN)

app = Flask(__name__)


@app.route('/webhook', methods=["POST"])
def hello():
    data = request.get_json(force = True)
    
    update:Update = Update.de_json(data, bot)
    
    #update 
    chat_id = update.message.chat_id
    text = update.message.text
    
    if text != None:
        bot.send_message(chat_id, text)
    
    return 'ok'


