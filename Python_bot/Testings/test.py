import spidev
import time

spi = spidev.SpiDev(0,0)
spi.open(0,0)
spi.max_speed_hz= 122000


while True:
    print(spi.readbytes(1))
    time.sleep(2)