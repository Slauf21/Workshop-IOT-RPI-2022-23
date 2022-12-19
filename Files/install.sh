#!/bin/su root
apt-get update -y 
apt install python3-pip -y 
apt install python3-cffi -y 
apt install -y gpac
pip3 install telebot
pip3 install pyTelegramBotAPI
pip3 install Adafruit_DHT
sudo apt-get -y install python3-rpi.gpio
pip3 install gpiozero
pip3 install board
pip3 install adafruit-circuitpython-sgp30
apt-get install build-essential python-dev -y
#apt-get autoremove -y
#apt-get autoclean -y
systemctl enable ssh
systemctl start ssh
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint do_spi 0
reboot
