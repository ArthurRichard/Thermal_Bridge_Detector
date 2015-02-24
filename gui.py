#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'arthrik'

from Tkinter import *

FOND_LCD = '#D3FFCE'


class Interface:
    'Ici, c est la classe qui gere l interface'

    def __init__(self):

        self.fen = Tk()
        # fen.attributes('-fullscreen', 1)
        self.fen.geometry('1280x800')

        # imagefnl = PhotoImage(file="images/mix.gif")
        self.imagerl = PhotoImage(file="images/image.gif")  #Image venant de la webcam
        self.imageir = PhotoImage(file="images/imageir.gif")  #Image infrarouge
        self.degrade = PhotoImage(file="images/echelle.gif")  #Degrade de couleurs

        self.canvas = Canvas(self.fen, width=512, height=256, relief=SUNKEN, bd=2, bg=FOND_LCD)  #Afficheur de temperature
        self.canvas.grid(row=0, column=1, sticky=N + E)

        self.canvastemp = Canvas(self.fen, width=256, height=512, bg='white')  #Echelle mouvante
        self.canvastemp.grid(row=0, column=1, sticky=S + E)

        self.canvas.create_text(200, 100, font=("DS-Digital", 144), text=25)  #Affichage de la temperature ambiante
        self.canvas.create_text(350, 100, font=("DS-Digital", 144), text="C")
        self.canvas.create_text(160, 200, font=("DS-Digital", 32), text="Mode:")  #Affichage du mode selectionne
        self.canvas.create_text(220, 200, font=("DS-Digital", 32), text=1)

        self.quitter = Button(self.fen, text="Quit", command=self.fen.destroy)
        self.quitter.grid(row=1, column=1)

        self.dispimage = Label(self.fen, image=self.imagerl, relief=RAISED, bd=2)
        self.dispimage.grid(row=0, column=0, sticky=W + S + N)

        self.degradetemp = Label(self.fen, image=self.degrade)
        self.degradetemp.grid(row=0, column=1, sticky=W + S)


    def moreTemp(self, i):
        Interface.temperature += i
        return Interface.temperature


    def getTemp(self):
        return Interface.temperature


    def run(self):
        self.fen.mainloop()

if __name__ == '__main__':
    app = Interface()
    app.run()




