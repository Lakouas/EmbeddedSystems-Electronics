from sys import maxsize
from tkinter import *
from unittest import expectedFailure
infostxtBatteries = ("Batterie 12V 120AH\n"
                     "Tension : 12.75VDC\n"
                     "Etat de charge : Float")
app=Tk()
app.title("Solaire Plus 1220A | V0.1")
#app.geometry("640x480")
app.maxsize(640,480)
app.minsize(640,480)
frame_haut = Frame(app,width=620,height=240,bg='black')
frame_bas  = Frame(app,width=620,height=240,bg='red')
frame_haut.pack(side='top',padx=5,pady=20)
frame_haut.propagate(False)
frame_bas.pack(side='bottom',padx=100,pady=30)
frame_bas.propagate(False)
infosBatteries = Label(frame_haut,text=f"{infostxtBatteries}")
infosBatteries.pack(padx=5,pady=5)
infosPv = Label(frame_bas,text=f"{infostxtBatteries}")
infosPv.pack()
app.mainloop()
