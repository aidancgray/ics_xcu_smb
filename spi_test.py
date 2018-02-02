#!/usr/bin/python

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629

# Split an integer input into a two byte array to send via SPI
def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    resp=spi.xfer([msb, lsb])
    return resp

# Repeatedly switch a MCP4151 digital pot off then on
while True:
    resp=write_pot(0x45)
    print(resp)
    time.sleep(0.5)
  
    