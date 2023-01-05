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

"""i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)"""

# Commando voor simpele reply
@bot.message_handler(commands=['hallo'])
def hallo(message):
    bot.reply_to(message, "Hi from TELEBOT!!!!!!")

# Commando voor foto
@bot.message_handler(commands=['foto'])
def foto(message):
    bot.reply_to(message, "Foto is onderweg...")
    # Capture
    camera.capture('/home/pem/Desktop/pem_python/image.jpg')
    # Foto sturen via telegram
    bot.send_photo(chat_id, photo=open('/home/pem/Desktop/pem_python/image.jpg', 'rb'))
    
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

# Commando voor aanzetten bewegingssensor
@bot.message_handler(commands=['motion_aan'])
def motion_aan(message):
    bot.reply_to(message, "Bewegingssensor wordt aangezet")
    motion_det()

"""# Commando voor luchtkwaliteit
@bot.message_handler(commands=['luchtkwaliteit'])
def luchtkwaliteit(message):
    bot.reply_to(message, "Luchtkwaliteit aan het meten.. Resultaat beschikbaar na 15 seconden.")
    t_end = time.time() + 15
    while time.time() < t_end:
        eCO2, TVOC = sgp30.iaq_measure()
    bot.send_message(chat_id, text = "eCO2 = %d ppm \t TVOC = %d ppb" % (eCO2, TVOC))"""

# Aansturen bewegingssensor
def motion_det():
    while True:
        if pir.motion_detected:
            bot.send_message(chat_id, text = "Beweging gedetecteerd! -> " + " " + (time.strftime("%H:%M:%S")))
            time.sleep(3)
        else:
            time.sleep(3)


bot.polling()