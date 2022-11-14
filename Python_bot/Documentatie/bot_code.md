# Telegram bot

<ins> Create a new bot </ins>

1. Open telegram and search for 'BotFather'
2. Click on the 'start' button or type '/start'
3. Type '/newbot'
4. Choose a name for your bot
5. Choose a username for your bot
6. You will get a message that contains a token to access the HTTP API

<ins> Python code </ins>

#### Import libraries
Some necessary libraries. Telebot is a Telegram bot library.

[![libs.png](https://i.postimg.cc/q70Y7h0k/libs.png)](https://postimg.cc/QF4S4MHP)

#### Key
Declaration of the personal token and initializes a connection to the bot.

[![key.png](https://i.postimg.cc/T3VWDXtc/key.png)](https://postimg.cc/75LLFj8C)

[![key-telebot.png](https://i.postimg.cc/0NNDRBCd/key-telebot.png)](https://postimg.cc/k2kBWwzB)

#### Pi camera
Then we create an object from the PiCamera class. When we create this object, the camera will start initializing itself. The resolution is also initialized.

*To use the PiCamera module, you will need to enable legacy support for the camera. (sudo raspi-config)*

[![picam.png](https://i.postimg.cc/Fs9KBJp0/picam.png)](https://postimg.cc/SjvqXRwK)

#### DHT 11
Create a DHT object from the Adafruit_DHT class. Gpio refers to the data pin of the sensor.

[![dht11.png](https://i.postimg.cc/P50TTLW3/dht11.png)](https://postimg.cc/3kjPZxbm)

#### Commands
The first command sends a fix reply when the user sends 'hallo'. When the second command is called, the Pi camera takes a picture and saves it to the specified path. After this, the picture will be sent as reply. The third command takes care of the measurement of temperature and humidity. The measuring will also be sent as reply.

[![commands.png](https://i.postimg.cc/15jZrgjm/commands.png)](https://postimg.cc/hfTwSGn6)

<ins> Results </ins>

Taking a picture with Pi camera:

[![foto.png](https://i.postimg.cc/5tfpHgS6/foto.png)](https://postimg.cc/xXFLhK72)

Measuring the temperature/humidity with DHT11:

![](https://user-images.githubusercontent.com/79916493/200297893-5a608b52-cad8-4d8a-97c5-aa622b74d706.PNG)
