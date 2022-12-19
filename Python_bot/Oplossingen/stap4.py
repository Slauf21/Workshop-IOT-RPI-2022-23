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

# Resolutie camera instellen
camera = PiCamera()
camera.resolution = (640,480)

# DHT declareren
dht_sensor = Adafruit_DHT.DHT11
# GPIO voor dht sensor
gpio_sensor = 18

# Relais declareren
GPIO.setmode(GPIO.BCM)
gpio_relais = 21
GPIO.setup(gpio_relais, GPIO.OUT)

# Commando voor simpele reply
@bot.message_handler(commands=['hallo'])
def hallo(message):
    bot.reply_to(message, "Hi from TELEBOT!!!!!!")

# Commando voor foto
@bot.message_handler(commands=['foto'])
def foto(message):
    bot.reply_to(message, "Foto is onderweg...")
    # Capture
    camera.capture('/home/Desktop/image.jpg')
    # Foto sturen via telegram
    bot.send_photo(chat_id, photo=open('/home/Desktop/image.jpg', 'rb'))

# Commando voor DHT
@bot.message_handler(commands=['temperatuur'])
def temperatuur(message):
    bot.reply_to(message, "Temperatuur wordt gemeten...")
    # Meting
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, gpio_sensor)
    # Meting sturen via telegram
    bot.reply_to(message, 'Temp={0:0.1f}°C  Humidity={1:0.1f}%'.format(temperature, humidity))

# Commando voor aanzetten relais
@bot.message_handler(commands=['relais_aan'])
def relais_aan(message):
    bot.reply_to(message, "Relais wordt aangezet")
    GPIO.output(gpio_relais, GPIO.HIGH)

# Commando voor uitzetten relais
@bot.message_handler(commands=['relais_uit'])
def relais_uit(message):
    bot.reply_to(message, "Relais wordt uitgezet")
    GPIO.output(gpio_relais, GPIO.LOW)

bot.polling()