# Libs
import telebot
import os
from picamera import PiCamera
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import asyncio
from gpiozero import MotionSensor
import board
import busio
import adafruit_sgp30

# Voer hier token in:
API_KEY = ''
# Voer hier chat id in:
chat_id = ''

bot = telebot.TeleBot(API_KEY)

print("Bot opgestart met token {}.".format(API_KEY))

# Commando voor simpele reply
@bot.message_handler(commands=['hallo'])
def hallo(message):
    bot.reply_to(message, "Hi from TELEBOT!!!!!!")

bot.polling()