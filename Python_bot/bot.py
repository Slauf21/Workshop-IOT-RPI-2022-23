import requests
import telebot
import os
TOKEN = "5574596927:AAE4WXBSZbe0N6eIdlxHIfKe32hQfjJEThE"
API_KEY = '5574596927:AAE4WXBSZbe0N6eIdlxHIfKe32hQfjJEThE'
chat_id = "5452220589"
#message = "slauf"
#url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
#print(requests.get(url).json()) # this sends the message

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hallo'])
def hallo(message):
    bot.reply_to(message, "Hi from TELEBOT!!!!!!")

bot.polling()