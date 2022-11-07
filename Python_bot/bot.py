import telebot
import os
from picamera import PiCamera, Color

TOKEN = "5574596927:AAE4WXBSZbe0N6eIdlxHIfKe32hQfjJEThE"
API_KEY = '5574596927:AAE4WXBSZbe0N6eIdlxHIfKe32hQfjJEThE'
chat_id = "5452220589"

bot = telebot.TeleBot(API_KEY)

# Resolutie camera instellen
camera = PiCamera()
camera.resolution = (640,480)

@bot.message_handler(commands=['hallo'])
def hallo(message):
    bot.reply_to(message, "Hi from TELEBOT!!!!!!")

@bot.message_handler(commands=['foto'])
def hallo(message):
    bot.reply_to(message, "Foto is onderweg...")
    camera.capture('/home/pem/Desktop/pem_python/image.jpg')
    bot.send_photo(chat_id, photo=open('/home/pem/Desktop/pem_python/image.jpg', 'rb'))
    

bot.polling()