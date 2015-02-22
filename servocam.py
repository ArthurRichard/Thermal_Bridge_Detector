#!/usr/bin/python
import time
import Image

import smbus


wallahlist = []
bus = smbus.SMBus(1)
DEVICE_ADDRESS = 0x68 #Adresse I2C du capteur
TEMP_AMBIANTE = bus.read_byte_data(DEVICE_ADDRESS,1)
imageir = Image.new('RGBA',(8,8))

print("Version du logiciel:",bus.read_byte_data(DEVICE_ADDRESS,0))
print("Temperature ambiante",TEMP_AMBIANTE)

def captureThermique():
	for i in range(2,10):
		wallah = bus.read_byte_data(DEVICE_ADDRESS,i)
		wallahlist.append(wallah)
		imageir.putdata(wallahlist)
		
	imgmod = imageir.resize((80,80))
	imgmod.save("imageir.gif")
	
for z in range(0,8):
	bus.write_byte_data(DEVICE_ADDRESS,0x00,z)
	captureThermique()
	time.sleep(0.1)


