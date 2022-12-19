# Workshop-IOT-RPI-2022-23

Steeds meer dingen – auto’s, deurbellen, rookmelders, koelkasten, noem maar op – zijn via een ‘embedded systeem’ verbonden met het internet. Internet of Things (IoT) noemen we dat. Hoe werken die systemen en wat zijn de elementaire bouwstenen om een volwaardig IoT-device te maken? In deze workshop bouwen we een eerste IoT-device. We bouwen een koppeling tussen sociale media (Telegram) en een “thing” met behulp van een Raspberry Pi-computertje verbonden met een temperatuur en luchtvochtigheid sensor, een bewegingssensor, een camera, een lichtsensor en een versnellingssensor. Dit alles doen we op een laagdrempelige manier. Alles is beschikbaar zodat je thuis - met je eigen Raspberry Pi – het werk kan voortzetten, als je dat wil.

Onderstaande linken om de benodigde applicaties te downloaden: <ins>*Indien je van thuis volgt.*</ins>

- Editor: [Notepad++](https://notepad-plus-plus.org/downloads/) (installeer de laatste versie)
- FTP-client: [FileZilla](https://filezilla-project.org/download.php?type=client)
- SSH-client: [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (MSI Windows Installer: 64-bit x86:)

**Indien je de workshop volgt mag je beginnen bij [Stap 2](#2-aanmaken-van-telegram-bot).**

# Inhoudstabel

- [Workshop-IOT-RPI-2022-23](#workshop-iot-rpi-2022-23)
- [Inhoudstabel](#inhoudstabel)
- [1. Installeren en Configureren Raspberry Pi](#1-installeren-en-configureren-raspberry-pi)
  - [1.1. Installeren Raspberry Pi OS](#11-installeren-raspberry-pi-os)
  - [1.2. Raspberry Pi verbinden met wifi](#12-raspberry-pi-verbinden-met-wifi)
  - [1.3. Configureren Raspberry Pi](#13-configureren-raspberry-pi)
- [2. Aanmaken van Telegram Bot](#2-aanmaken-van-telegram-bot)
  - [2.1 Installeer Telegram](#21-installeer-telegram)
  - [2.2 Configureren van bot](#22-configureren-van-bot)
- [3. Schrijven van de code](#3-schrijven-van-de-code)
  - [3.1 Putty](#31-putty)
  - [3.1 FileZilla](#31-filezilla)
  - [3.1 Notepad++](#31-notepad)

# 1. Installeren en Configureren Raspberry Pi

Om de Raspberry PI te kunnen gebruiken voor het IOT-project moet eerst het Raspberry Pi operating system geïnstalleerd worden. Daarna moet de wifi op de Raspberry Pi geconfigureerd worden en het IP-adres genoteerd worden zodat vanaf een andere pc ingelogd kan worden op de PI via SSH. Als je de workshop volgt tijdens de demo kan je deel 1 volledig overslaan en naar deel 2 gaan. Wil je het project bij je thuis nabouwen, dan moet je eerst stap 1.1 doornemen om het project te kunnen opbouwen.

## 1.1. Installeren Raspberry Pi OS

Om het project te kunnen opstellen moet het Raspberry PI operating system geïnstalleerd worden (op een SD-kaart van minstens 16GB die volledig geformatteerd mag worden) samen met enkele installatie pakketten. Bij de Raspberry Pi die tijdens de workshop gebruikt wordt is dit al uitgevoerd. Om dit thuis ook te kunnen doen moet dit eerst nog op de SD-kaart geïnstalleerd worden. 

Eerst moet de [Raspberry Pi Imager](https://www.raspberrypi.com/software/) geïnstalleerd worden op je computer. De imager is een snelle en makkelijke manier om de Raspberry Pi OS te installeren op een SD kaart.

Steek de SD kaart in je computer en open de imager. Bij het openen van de imager word je begroet met het volgende scherm:

![image](https://user-images.githubusercontent.com/79916416/201630879-30a88e3d-f5d6-4e55-9f89-e1bc7c484a24.png)

Vooraleer je het OS erop zet is het belangrijk op de ssh van de raspberry pi aan te zetten. In de imager druk je de sneltoets ctrl+shift+x in om de instellingen te openen. Hier vink je enable SSH aan.

![image](https://user-images.githubusercontent.com/79916416/208386264-77ec658c-7dfb-485b-9a96-0a958e4d4d9c.png)

Sluit de instellingen en ga op 'CHOOSE OS' klikken en selecteer je Raspberry Pi OS (32-bit). Daarna kies je de SD kaart waarop je de OS wilt zetten. Dit gebeurt door op de 'CHOOSE STORAGE' knop te klikken. Je SD kaart zal daar staan en die moet je dan selecteren.

Wanneer je de melding krijgt dat het schrijven van de image succesvol afgerond is mag je de kaart verwijderen uit je pc en in de Raspberry Pi plaatsen. Sluit vervolgens het toetsenbord, muis, camera, HDMI-scherm, en sensor bord aan. De sensoren bord is al gemaakt tijdens de workshop. Als je deze zelf wil maken kan je [hier](https://github.com/Slauf21/Workshop-IOT-RPI-2022-23/blob/main/Circuit/PCB.md) meer informatie vinden.

Nu is de Raspberry Pi klaargezet maar deze moet nog geconfigureerd worden.

## 1.2. Raspberry Pi verbinden met wifi

- Steek de Raspberry Pi in en wacht tot deze is ingeschakeld.

Startscherm:

[![rpi-home.png](https://i.postimg.cc/VkX8LyDr/rpi-home.png)](https://postimg.cc/5X9Gnrcb)

- Klik rechtsboven op het wifi-icoontje. Schakel de wifi in en kies voor je wifi netwerk.

[![rpi-ssid.jpg](https://i.postimg.cc/CxbsvJxp/rpi-ssid.jpg)](https://postimg.cc/HrsMnwM6)

- Na het selecteren van het netwerk komt er in het midden een venster tevoorschijn. Vul hier het wachtwoord van je netwerk in.

[![rpi-ssid-pass-1.png](https://i.postimg.cc/0QBbp6FH/rpi-ssid-pass-1.png)](https://postimg.cc/7GSH4Lxg)

Nu de Raspberry Pi verbonden is met het netwerk bewaren we het toegewezen IP-adres. Door over het wifi-icoontje te bewegen met de cursor zal er een venster verschijnen. Noteer deze IP-adres. Wees zeker dat je raspberry pi en je PC verbonden zijn met hetzelfde wifi netwerk.

[![rpi-ssid-pass.png](https://i.postimg.cc/GmJdcwm7/rpi-ssid-pass.png)](https://postimg.cc/k24kcH8K)

*Ons IP-adres: 169.154.146.220, niet overnemen.*

## 1.3. Configureren Raspberry Pi
Als volgende stap gaan we met een voorgeschreven .sh file de nodige bibliotheken afhalen en functionaliteiten aanzetten van de RPI.

Open de terminal op de Raspberry PI door op het terminal icoontje te klikken of door gebruik te maken van de sneltoets ctrl+alt+t

[![trml-logo.png](https://i.postimg.cc/JhDjxfZT/trml-logo.png)](https://postimg.cc/KKbKvs9L)

Met onderstaande commando's gaan we als eerst de .sh downloaden en vervolgens uitvoeren.

- Downloaden script:
  - wget https://github.com/Slauf21/Workshop-IOT-RPI-2022-23/blob/d751ddeb24a901cbfb92339efcc60615b5a4963a/Files/install.sh
- Script uitvoerbaar maken:
  - chmod +x install.sh
- Starten van script:
  - sudo ./install.sh

*Kopieer deze commando's individueel en plak met rechtermuisknop in de terminal.*

Vervolgens zal de RPI herstarten en kan er verder gegaan worden met de volgende stap.

# 2. Aanmaken van Telegram Bot

## 2.1 Installeer Telegram
We beginnen met het installeren van Telegram. Deze kan zowel op pc als op mobiel geïnstalleerd worden. Volg deze link om [Telegram Desktop](https://desktop.telegram.org/) te installeren op pc.

## 2.2 Configureren van bot
- Open telegram en zoek naar BotFather.

[![btfthr.png](https://i.postimg.cc/LXqyfSd9/btfthr.png)](https://postimg.cc/XGbcST7m)

Onderstaande venster bij invoer BotFather:

*Elk <ins>commando</ins> begint met een slash (/).*

[![botfather.png](https://i.postimg.cc/vZQbvg2P/botfather.png)](https://postimg.cc/ZCDGbRS3)

- Klik vervolgens op start.

Hierna verschijnt een hoop uitleg van verschillende commando's voor het aansturen van de bot.

- Om nu een bot te creëren voeren we '/newbot' in.

[![nwbot.png](https://i.postimg.cc/xjB8VV9K/nwbot.png)](https://postimg.cc/t7tpFfZT)


- Kies een naam voor je bot.

[![name.png](https://i.postimg.cc/2jnQtGD8/name.png)](https://postimg.cc/0r2KMpjL)

- Kies nu een gebruikersnaam voor je bot dat eindigt met bot (bv. test_bot). 

[![username.png](https://i.postimg.cc/htZZGshR/username.png)](https://postimg.cc/jDN4gzzM)

*Gebruik iets anders als 'Telegram_bot'.*

Indien naam in gebruik kan er nogmaals gevraagd worden om een gebruikersnaam in te voeren.

- Als dit succesvol is gelukt, wordt er een unieke token aangemaakt die later gebruikt wordt in de software.

[![token.png](https://i.postimg.cc/PfBK80ry/token.png)](https://postimg.cc/QVJc247K)

Nu de **token** is gegenereerd gaan we niet meet met de BotFather praten, maar met onze eigen bot.

- In de zoekbalk moet je zoeken naar de gebruikersnaam van je bot (bij ons geval is dat "slauf_bot"). Die voeg je dan toe en druk je op start.

![image](https://user-images.githubusercontent.com/79916416/208381541-434ed268-0e59-4c0b-96ee-08381ae21ad1.png)

We gaan ook de chat id nodig hebben. Met deze [link](https://ungineer.github.io/chatid.html) kan je de chat id terugvinden door je **token** in het venster te plakken.

- Plak de **token** in het vakje en klik op 'Get Chat ID'.

[![site.png](https://i.postimg.cc/tTB242bY/site.png)](https://postimg.cc/5YFwP56V)

# 3. Schrijven van de code

Nu de Raspberry Pi is geïnstalleerd kunnen we beginnen met het schrijven van een Python code. Om de code te schrijven hebben we als eerst een editor nodig. Om de code te transporteren op de Raspberry Pi hebben we vervolgens een FTP-client nodig. En als laatste een SSH-client om commando's uit te voeren op de Raspberry Pi. Deze had je in het begin moeten installeren.

## 3.1 Putty

- Open Putty en voer de IP-adres in die je had teruggevonden in de vorige stappen.
- *Kijk na of 'Connection type' op SSH staat en 22 als poortnummer is gekozen.*
- Klik onderaan op 'Open'.

Er wordt nu een verbinding gemaakt met het bovenvermelde adres.

![Putty](https://www.ssh.com/hubfs/Imported_Blog_Media/PuTTY_Windows_configuration_and_connection_screen_with_profile_save_option-2.png)

Vervolgens zal je moeten inloggen op de Raspberry Pi. Gebruik de standaard inloggegevens als volgt:

- login as: **pi** (enter)
- password: **raspberry** (enter)

<br>

- *Mogelijke waarschuwing: klik op 'Accept'*

[![ptty-wrning.png](https://i.postimg.cc/s2Msdnv1/ptty-wrning.png)](https://postimg.cc/R3xjwL1z)

Indien je succesvol bent ingelogd ziet je terminal als volgt uit:

[![putty.png](https://i.postimg.cc/qMgkYPn0/putty.png)](https://postimg.cc/HVDD8PBP)

*Inloggegevens ter illustratie, niet overnemen.*

Hierna kunnen we aan de slag met het downloaden van de start code. Deze wordt bewaard op de Raspberry Pi met de volgende commando:

- wget https://raw.githubusercontent.com/Slauf21/Workshop-IOT-RPI-2022-23/main/Python_bot/Workshop.py -O ~/Desktop/Workshop.py

*Bestand bewaard op bureaublad.*

## 3.1 FileZilla

- Open FileZilla en voer de gegevens in die je had teruggevonden in de vorige stappen.
  - Host: IP-adres
  - Gebruikersnaam: **pi**
  - Wachtwoord: **raspberry**
  - Poort: 22
- Klik op 'Snelverbinden' om een verbinding te maken.

[![filezilla.png](https://i.postimg.cc/28hgB7Bp/filezilla.png)](https://postimg.cc/qzB1PnLQ)

Indien je succesvol bent ingelogd ziet je scherm als volgt uit:

[![filzil.jpg](https://i.postimg.cc/HsmRC7VT/filzil.jpg)](https://postimg.cc/8sytRcRY)

*Links zie je de werkomgeving van je pc en rechts die van de Raspberry Pi. Nu kan er bestanden uitgewisseld worden tussen deze 2 apparaten.*

- Ga nu in de map 'Desktop' die je rechts terugvindt.
- Binnen Desktop vind je nu 'Workshop.py' die eerder was afgehaald met een link.

[![ws.png](https://i.postimg.cc/VNy48xk2/ws.png)](https://postimg.cc/zyjTwPWk)

- Sleep deze bestand nu naar je bureaublad van je <ins>pc</ins>.

[![pyfile.png](https://i.postimg.cc/tJVHs0FW/pyfile.png)](https://postimg.cc/JHmFF26z)

## 3.1 Notepad++

- Open Notepad++ en klik linksboven op 'Bestand'.

[![notepad.png](https://i.postimg.cc/D0KPVLfs/notepad.png)](https://postimg.cc/CBmqkZqL)

- Klik op 'Openen' en kies voor 'Workshop.py' die op je persoonlijke bureaublad staat.

[![ntpd.png](https://i.postimg.cc/3W56cdVb/ntpd.png)](https://postimg.cc/p5Cq9X2D)

Indien je de bestand succesvol hebt kunnen openen ziet je scherm als volgt uit:

[![ntpd-code.png](https://i.postimg.cc/DyhpPjf4/ntpd-code.png)](https://postimg.cc/HjStptyT)

- Plak vervolgens de token en chat id binnen de aanhalingstekens.

- Om deze wijziging op te slaan druk op Ctrl + S of via 'Bestand' linksboven 'Opslaan' klikken.

- Open FileZilla en sleep deze bestand vanuit je persoonlijke bureaublad aan de rechterkant binnen het map 'Desktop'.

[![filzil.png](https://i.postimg.cc/66VqPqKb/filzil.png)](https://postimg.cc/yWd7gVk0)

*Vink 'Deze actie altijd gebruiken' en klik op 'OK' als je een waarschuwing krijgt over 'Doelbestand bestaat al'.*

Nu de bijgewerkte versie van de code op de Raspberry Pi staat kunnen we deze runnen.

- Open Putty en tik 'cd Desktop/' in om in het bureaublad te zitten waar de code zich bevindt.

- Tik nu 'python3 Workshop.py' in om de code te runnen.

Indien je de bestand succesvol hebt kunnen runnen ziet je scherm als volgt uit:

[![ptty-termnl.png](https://i.postimg.cc/GpsgLZht/ptty-termnl.png)](https://postimg.cc/t1pNDv6G)

Nu heb je de basis bereikt, om nu de interessante delen toe te voegen in je code klik je op deze [link](https://github.com/Slauf21/Workshop-IOT-RPI-2022-23/wiki).

Verder zal je hardware aansturen gelijk PiCamera om foto's te nemen, DHT11 om temperatuurmetingen uit te voeren enzovoort.
