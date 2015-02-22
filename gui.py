#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'arthrik'

from Tkinter import *

TEMP_AMBIANTE = 25  #A remplacer par le registre I2C

fen = Tk()
#fen.attributes('-fullscreen', 1)
fen.geometry('1280x800')

#imagefnl = PhotoImage(file="images/mix.gif")
imagerl = PhotoImage(file="images/image.gif")
imageir = PhotoImage(file="images/imageir.gif")

canvas = Canvas(fen,width = 512,height = 384,relief=SUNKEN)
canvas.pack(side = RIGHT)

canvas.create_text(50,50, font=("Arial", 76),text=TEMP_AMBIANTE)
canvas.create_text(150,50, font=("Arial", 76),text="°C")

quitter = Button(fen, text="Quit", command=fen.destroy)
quitter.pack(side = RIGHT)

dispimage = Label(fen,image=imagerl)
dispimage.pack(side = LEFT)

fen.mainloop()