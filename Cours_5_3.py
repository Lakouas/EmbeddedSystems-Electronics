from shutil import which
from tkinter import *

app = Tk()
app.title("Antenne patch Calculator - 0.1")
app.geometry("640x480")
app.wm_maxsize(width=640,height=480)
app.wm_minsize(width=640,height=480)
frame_gauche =  Frame(app,width=300,height=420,bg='black')
frame_gauche.grid(row=0,column=0,padx=10,pady=20)
frame_droite = Frame(app,width=200,height=420,bg='red')
frame_droite.grid(row=0,column=1,padx=10,pady=20)
frame_ex_droite = Frame(app,width=70,height=420,bg='white')
frame_ex_droite.grid(row=0,column=2,padx=10,pady=20)
app.mainloop()
