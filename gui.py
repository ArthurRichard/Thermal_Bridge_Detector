#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'arthrik'

from Tkinter import *

TEMP_AMBIANTE = 25  #A remplacer par le registre I2C
FOND_LCD = '#D3FFCE'

mode = 1 #1: Image Reelle uniquement 2:Image infrarouge uniquement 3: Melange IR + RL

fen = Tk()
#fen.attributes('-fullscreen', 1)
fen.geometry('1280x800')

#imagefnl = PhotoImage(file="images/mix.gif")
imagerl = PhotoImage(file="images/image.gif")
imageir = PhotoImage(file="images/imageir.gif")
echelle = PhotoImage(file="images/echelle.gif")

canvas = Canvas(fen,width = 512,height = 256,relief=RAISED,bg=FOND_LCD)
canvas.grid(row=0,column=1,sticky=N+E)

canvas.create_text(200,100, font=("DS-Digital", 144),text=TEMP_AMBIANTE)
canvas.create_text(350,100, font=("DS-Digital", 144),text="C")
canvas.create_text(160,200, font=("DS-Digital", 32),text="Mode:")
canvas.create_text(220,200, font=("DS-Digital", 32),text=mode)

quitter = Button(fen, text="Quit", command=fen.destroy)
quitter.grid(row=1,column=1)

dispimage = Label(fen,image=imagerl)
dispimage.grid(row=0,column=0,sticky=W+S+N)

echelletemp = Label(fen,image=echelle)
echelletemp.grid(row=0,column=1,sticky=W+S)

fen.mainloop()