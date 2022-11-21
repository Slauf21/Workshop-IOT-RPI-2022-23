# Libs
import telebot
import os
from picamera import PiCamera, Color
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import asyncio
from gpiozero import MotionSensor

API_KEY = '5574596927:AAE4WXBSZbe0N6eIdlxHIfKe32hQfjJEThE'
chat_id = '5452220589'

bot = telebot.TeleBot(API_KEY)

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

# Bewegingssensor declareren
pir = MotionSensor(24)

# Commondo voor simpele reply
@bot.message_handler(commands=['hallo'])
def hallo(message):
    bot.reply_to(message, "Hi from TELEBOT!!!!!!")

# Commondo voor foto
@bot.message_handler(commands=['foto'])
def hallo(message):
    bot.reply_to(message, "Foto is onderweg...")
    # Capture
    camera.capture('/home/pem/Desktop/pem_python/image.jpg')
    # Foto sturen via telegram
    bot.send_photo(chat_id, photo=open('/home/pem/Desktop/pem_python/image.jpg', 'rb'))
    
# Commondo voor DHT
@bot.message_handler(commands=['temperatuur'])
def hallo(message):
    bot.reply_to(message, "Temperatuur wordt gemeten...")
    # Meting
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, gpio_sensor)
    # Meting sturen via telegram
    bot.reply_to(message, 'Temp={0:0.1f}°C  Humidity={1:0.1f}%'.format(temperature, humidity))

# Commondo voor aanzetten relais
@bot.message_handler(commands=['relais_aan'])
def hallo(message):
    bot.reply_to(message, "Relais wordt aangezet")
    GPIO.output(gpio_relais, GPIO.HIGH)

# Commondo voor uitzetten relais
@bot.message_handler(commands=['relais_uit'])
def hallo(message):
    bot.reply_to(message, "Relais wordt uitgezet")
    GPIO.output(gpio_relais, GPIO.LOW)

# Commondo voor uitzetten relais
@bot.message_handler(commands=['motion_aan'])
def hallo(message):
    motion_det()
    bot.reply_to(message, "Bewegingssensor wordt aagezet")

# Commondo voor uitzetten relais
@bot.message_handler(commands=['motion_uit'])
def hallo(message):
    bot.reply_to(message, "Bewegingssensor wordt uitgezet")

# Aansturen beweginssensor
def motion_det():
    try:
        while True:
            if pir.motion_detected:
                bot.send_message(chat_id, text = "Beweging gedetecteerd -> dief!!!!!!!" + " " + (time.strftime("%H:%M:%S")))
                time.sleep(3)
            else:
                time.sleep(3)

    except KeyboardInterrupt:
        print('interrupted!')


bot.polling()