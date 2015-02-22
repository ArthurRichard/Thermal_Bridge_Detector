from Tkinter import *


fen=Tk()
fen.geometry('1280x800')
photo=PhotoImage(file="image.gif")
labl = Label(fen, image=photo)
labl.pack();
labl.place(bordermode=OUTSIDE)
lb1=Label(fen,text="TEST TEMPERATURE")
labl.place(bordermode=OUTSIDE,height=25,width=1000)
fen.mainloop() 
