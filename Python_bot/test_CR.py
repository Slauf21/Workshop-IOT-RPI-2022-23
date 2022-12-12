import spidev
from time import sleep

# First open up SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Initialize what sensor is where
Channel = 0
sleepTime = 1

def getReading(channel):
    # First pull the raw data from the chip
    rawData = spi.xfer([1, (8 + channel) << 4, 0])
    # Process the raw data into something we understand.
    processedData = ((rawData[1]&3) << 8) + rawData[2]
    return processedData

def convertVoltage(bitValue, decimalPlaces=2):
    voltage = (bitValue * 5) / float(1023)
    voltage = round(voltage, decimalPlaces)
    return voltage

while True:
    Data = getReading(Channel)
    Voltage = convertVoltage(Data)

    # Print ALL THE THINGS:
    print("BitValue = {} ; Voltage = {} V".format(Data, Voltage))
    sleep(sleepTime)