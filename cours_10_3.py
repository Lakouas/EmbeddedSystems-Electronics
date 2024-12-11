import serial
from tkinter import *
from datetime import datetime

def mise_a_jour_affichage():
    uart = serial.Serial('COM7')
    uart.baudrate = 9600
    uart.bytesize = 8
    uart.parity = 'N'
    uart.stopbits = 2
    uart.write(b'm')  # transmit 'A' (8bit) to micro/Arduino
    data = uart.read(8)
    data_text=data.decode('utf-8')
    temp = data_text[:4]
    hum = data_text[4:]
    if data :
        temp2.configure(text=f"{temp}")
        hum2.configure(text=f"{hum}")
        app.after(1000, mise_a_jour_affichage)
    else :
        print("rien")
        pass
def miseAjourTemps():
    date  = datetime.now().strftime("%d/%m/%Y")
    heure = datetime.now().strftime("%H:%M:%S")
    zoneDateHeure.configure(text=f"{date}|{heure}")
    zoneDateHeure.after(1, miseAjourTemps)

app= Tk()
app.title("Thermomètre Hygromètre")
app.geometry("250x120")
app.minsize(250,120)
app.maxsize(250,120)
icon="H:\\Enseignements\\Python\\Cours\\V2\\cours_10\\app.ico"
app.iconbitmap(icon)
app.configure(bg="white")

Zone1=Frame(app,bg="black")
Zone1.place(x=0,y=5,width=250,height=20)
zoneDateHeure = Label(Zone1,text="",bg="black",fg="white",font=("Verdana",9))
zoneDateHeure.pack(side=RIGHT)
miseAjourTemps()
Zone2=Frame(app,bg="white")
Zone2.place(x=0,y=25,width=250,height=50)
temp1=Label(Zone2,text="température",bg="white",fg="black",font=("Verdana",8))
temp1.place(x=5,y=15)
temp2=Label(Zone2,text="25.12",bg="white",fg="black",font=("Bahnschrift SemiBold",26))
temp2.place(x=110,y=0)
temp3=Label(Zone2,text="°C",bg="white",fg="black",font=("Bahnschrift SemiBold",10))
temp3.place(x=200,y=15)
Zone3=Frame(app,bg="white")
Zone3.place(x=0,y=70,width=250,height=50)
hum1=Label(Zone3,text="Humidité",bg="white",fg="black",font=("Verdana",8))
hum1.place(x=5,y=15)
hum2=Label(Zone3,text="25.12",bg="white",fg="black",font=("Bahnschrift SemiBold",26))
hum2.place(x=110,y=0)
hum3=Label(Zone3,text=" %",bg="white",fg="black",font=("Bahnschrift SemiBold",10))
hum3.place(x=200,y=15)
mise_a_jour_affichage()
app.mainloop()





