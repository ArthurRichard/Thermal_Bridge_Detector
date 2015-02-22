#!/usr/bin/python
__author__ = 'arthrik'

import time
from PIL import Image

import picamera

import smbus
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)#Gauche
GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)#Droite
GPIO.setup(4, GPIO.IN, GPIO.PUD_UP) #Ok

GPIO.setup(18,GPIO.OUT) #Led Rouge
GPIO.setup(23,GPIO.OUT) #Led verte
GPIO.output(18,False)
GPIO.output(23,True)

print("Camera du futur pas cher 2000, version alpha 0.1")

def onQuit():
	print("Ciao morray")
	GPIO.cleanup()

#========================Partie Acquisition Donnees Thermiques========================

wallahlist = []
bus = smbus.SMBus(1)
DEVICE_ADDRESS = 0x68
imageir = Image.new('RGBA',(8,8))

print("Version du logiciel:",bus.read_byte_data(DEVICE_ADDRESS,0))

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


#========================Partie Acquisition Camera====================================

def takePicture():        #Capture de l'image
	GPIO.output(18,True)
	with picamera.PiCamera() as camera:
		print("Capture en cours...")
		camera.resolution = (800,800)
		camera.iso = 400
    	camera.capture('/home/pi/Detecteur/images/image.gif')
		GPIO.output(18,False)
		print("Photo Prise!")
		camera.close()

def ok():                  #Bouton Ok
	takePicture()
	return 1

def gauche():              #Bouton Gauche
	print("Gauche")
	convertirImage()
	return 1

def droite():              #Bouton Droit
	print("Droit")
	return 1

while True:
	if GPIO.input(17) == False:
		gauche()
	if GPIO.input(22) == False:
		droite()
	if GPIO.input(4) == False:
		ok()
	time.sleep(0.1)

#========================Partie Interface=================================================

