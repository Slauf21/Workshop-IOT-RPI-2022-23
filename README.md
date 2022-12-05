# Workshop-IOT-RPI-2022-23

Steeds meer dingen – auto’s, deurbellen, rookmelders, koelkasten, noem maar op – zijn via een ‘embedded systeem’ verbonden met het internet. Internet of Things (IoT) noemen we dat. Hoe werken die systemen en wat zijn de elementaire bouwstenen om een volwaardig IoT-device te maken? In deze workshop bouwen we een eerste IoT-device. We bouwen een koppeling tussen sociale media (Telegram) en een “thing” met behulp van een Raspberry Pi-computertje verbonden met een temepratuur en luchtvochtigheid sensor, een bewegingssensor, een camera, een lichtsensor en een versnellings sensor. Dit alles doen we op een laagdrempelige manier. Alles is beschikbaar zodat je thuis - met je eigen Raspberry Pi – het werk kan voortzetten, als je dat wil.

# Inhoudstabel

- [Workshop-IOT-RPI-2022-23](#workshop-iot-rpi-2022-23)
- [Inhoudstabel](#inhoudstabel)
- [1. Installeren en Configureren Raspberry Pi](#1-installeren-en-configureren-raspberry-pi)
  - [1.1. Installeren Raspberry Pi OS](#11-installeren-raspberry-pi-os)
  - [1.2. Raspberry Pi verbinden met WiFi](#12-raspberry-pi-verbinden-met-wifi)
  - [1.3. Configureren Raspberry Pi](#13-configureren-raspberry-pi)
- [2. Aanmaken van Telegram Bot](#2-aanmaken-van-telegram-bot)
  - [2.1 Installeer Telegram](#21-installeer-telegram)
  - [2.2 Configureren van bot](#22-configureren-van-bot)
- [3. Schrijven van de code](#3-schrijven-van-de-code)

# 1. Installeren en Configureren Raspberry Pi

Om de Raspberry PI te kunnen gebruiken voor het IOT-project moet eerst het Raspberry Pi operating system geïnstalleerd worden (1.1). Daarna moet de wifi op de PI geconfigureerd worden en het IP genoteerd worden zodat vanaf een andere pc ingelogd kan worden op de PI via SSH (1.2). Als je de workshop volgt tijdens de demo kan je deel 1 volledig overslaan en naar deel 2 gaan. Wil je het project bij je thuis nabouwen, dan moet je eerst stap 1.1 doornemen om het project te kunnen opbouwen.

## 1.1. Installeren Raspberry Pi OS

Om het project te kunnen bouwen moet het Raspberry PI operating system geïnstalleerd worden (op een SD-kaart van minstens 16GB die volledig geformateerd mag worden) samen met enkele installatie pakketten. Bij de PI die tijdens de workshop gebruikt wordt is dit reeds uitgevoerd. Om dit thuis ook te kunnen doen moet dit eerst nog op de SD-kaart geïnstalleerd worden. 

Eerst moet de [Raspberry Pi Imager](https://www.raspberrypi.com/software/) geinstalleerd worden op je computer. De imager is een snelle en makkelijke manier om de Raspberry Pi OS te installeren op een SD kaart.

Steek de SD kaart in je computer en open de imager. Bij het openen van de imager word je begroet met het volgende scherm:

![image](https://user-images.githubusercontent.com/79916416/201630879-30a88e3d-f5d6-4e55-9f89-e1bc7c484a24.png)

Hier ga je op "CHOOSE OS" klikken en selecteer je Raspberry Pi OS (32-bit). Daarna kies je de SD kaart waarop je de OS wilt zetten. Dit gebeurt door op de "CHOOSE STORAGE" knop te klikken. Je SD kaart zal daar staan en die moet je dan selecteren.

Wanneer je de melding krijgt dat het schrijven van de image succesvol afgerond is mag je de kaart verwijderen uit je PC en in de Raspberry PI plaatsen. Sluit vervolgens het toetsenbord, muis, camera, HDMI-scherm, en sensor bord aan. De sensoren bord is al gemaakt tijdens de workshop. Als je deze zelf wil maken kan je [hier](https://github.com/Slauf21/Workshop-IOT-RPI-2022-23/blob/main/Circuit/PCB.md) meer informatie vinden.

Nu is de Raspberry Pi klaargezet en moet hij geconfigureerd worden.

## 1.2. Raspberry Pi verbinden met WiFi

Start de Raspberry PI op en klik recht boven op het wifi-icoontje (1), controleer vervolgens of de wifi ingeschakeld is (2) en selecteer daarna het gewenste netwerk (3). Er zal nu een melding komen om een wachtwoord in te geven (4). Kies na het ingeven van het wachtwoord ten slotte voor OK (5).

Startscherm

[![rpi-home.png](https://i.postimg.cc/rsWysJ6F/rpi-home.png)](https://postimg.cc/xNfVFLTW)

![image](https://user-images.githubusercontent.com/79916416/201632572-0cdbd516-498e-4d88-9431-06fde4849533.png)

De Raspberry is nu verbonden met het wifi netwerkt en er werd door de router een IP-adres toegewezen aan de Raspberry. Beweeg met de cursor over het wifi-icoontje (1), er zal nu een text vlak verschijnen met daarin het IP-adres (2). Noteer dit IP_adres ergens wat je zal het later nodig hebben om via de PC te verbinden met de Raspberry.

![image](https://user-images.githubusercontent.com/79916416/201632807-cfd7bbc9-b4fc-4ae6-9ba2-312468fa495d.png)

## 1.3. Configureren Raspberry Pi
Als volgende stap gaan we met een voorgeschreven .sh file de nodige bibliotheken afhalen en functionaliteiten aanzetten van de RPI.

Open de terminal op de Raspberry PI door op het terminal icoontje te klikken of door gebruik te maken van de sneltots ctrl+alt+t

[![trml-logo.png](https://i.postimg.cc/JhDjxfZT/trml-logo.png)](https://postimg.cc/KKbKvs9L)

Met onderstaande commando's gaan we als eerst de .sh downloaden en vervolgens uitvoeren.

- Downloaden script
  - wget https://raw.github.com/PXLDigital/EAI-Workshop-IoT-met-RPi/main/Code/install.sh
- Script uivoerbaar maken
  - chmod +x install.sh
- Starten van script
  - sudo ./install.sh

Vervolgens zal de RPI herstarten en kan er verder gegaan worden met de volgende stap.

# 2. Aanmaken van Telegram Bot

## 2.1 Installeer Telegram
We beginnen met het installeren van Telegram. Deze kan zowel op PC als op mobiel geïnstalleerd worden. Volg deze link om [Telegram Desktop](https://desktop.telegram.org/) te installeren op PC.

## 2.2 Configureren van bot
- Open telegram en zoek naar BotFather.

[![btfthr.png](https://i.postimg.cc/LXqyfSd9/btfthr.png)](https://postimg.cc/XGbcST7m)

Onderstaande venster bij invoer BotFather:
[![botfather.png](https://i.postimg.cc/vZQbvg2P/botfather.png)](https://postimg.cc/ZCDGbRS3)

- Klik vervolgens op start.

Hierna verschijnt een hoop uileg van verschillende commando's voor het aansturen van de bot.

- Om nu een bot te creëren voeren we '/newbot' in.

*Elk <ins> commando </ins> begint met een slash (/).*

# 3. Schrijven van de code

Nu alles ingesteld is kan begonnen worden met het schrijven van de code. Om dit te doen gebruiken we een laptop met daarop een code editor. We gebruiken de [notepad++ editor](https://notepad-plus-plus.org/). We moeten ook de geschreven code op de Raspberry Pi krijgen
