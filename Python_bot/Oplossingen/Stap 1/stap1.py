# Libs
import telebot
import os
from picamera import PiCamera, Color
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import asyncio
from gpiozero import MotionSensor
import board
import busio
import adafruit_sgp30

# Voer hier token in:
API_KEY = '5574596927:AAE4WXBSZbe0N6eIdlxHIfKe32hQfjJEThE'
# Voer hier chat id in:
chat_id = '5452220589'

bot = telebot.TeleBot(API_KEY)

print("Bot opgestart met token {}.".format(API_KEY))

# Commondo voor simpele reply
@bot.message_handler(commands=['hallo'])
def hallo(message):
    bot.reply_to(message, "Hi from TELEBOT!!!!!!")

bot.polling()