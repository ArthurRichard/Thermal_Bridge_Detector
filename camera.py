import time

import picamera

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)  # Gauche
GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)  # Droite
GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)  # Ok

GPIO.setup(18, GPIO.OUT)  # Led Rouge
GPIO.setup(23, GPIO.OUT)  # Led verte
GPIO.output(18, False)
GPIO.output(23, True)

print("Camera du futur pas cher 2000, version alpha 0.1")


def onQuit():
    print("Ciao morray")
    GPIO.cleanup()


def takePicture():  # Capture de l'image
    GPIO.output(18, True)
    with picamera.PiCamera() as camera:
        print("Capture en cours...")
        camera.resolution = (800, 800)
        camera.iso = 400
    camera.capture('/home/pi/Detecteur/images/image.gif')
    GPIO.output(18, False)
    print("Photo Prise!")
    camera.close()


def ok():
    takePicture()
    return 1


def gauche():
    print("Gauche")
    return 1


def droite():
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
