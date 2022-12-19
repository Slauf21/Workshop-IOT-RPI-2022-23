#!/bin/su root
apt-get update -y 
apt install python3-pip -y 
apt install python3-cffi -y 
apt install -y gpac
pip3 install telebot
pip3 install Adafruit_DHT
apt-get -y install python3-rpi.gpio
pip3 install gpiozero
pip3 install board
pip3 install adafruit-circuitpython-sgp30
apt-get install build-essential python-dev -y
#apt-get autoremove -y
#apt-get autoclean -y
systemctl enable ssh
systemctl start ssh
raspi-config nonint do_camera 0
sudo raspi-config nonint do_spi 0
mkdir /home/pi/Desktop/IOT_Workshop
chown pi:pi /home/pi/Desktop/IOT_Workshop
cd /home/pi/Desktop/IOT_Workshop
touch Workshop.py
chown pi:pi /home/pi/Desktop/IOT_Workshop/Workshop.py
reboot
