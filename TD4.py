from math import sqrt, log, pi
from tkinter import * 

def calculRayon():
    fr=float(fr_antenne.get())
    fr= fr * 1e9
    Epsr=float(Epsilon_r.get())
    h_sub=float(h_substrat.get())
    F = ((8.791)*(1e9))/(fr*(sqrt(Epsr)))
    B = (log((pi*F)/(2*h_sub))) + (1.7726)
    A = ((2*h_sub)/(pi*Epsr*F))*B
    C=  sqrt(1+A)
    rayon_antenne = F/C
    rayon_antenne=round(rayon_antenne,4)
    resultats.config(text=f"{rayon_antenne}Cm",font=("Calibri light",12))

fenetre_main = Tk()
fenetre_main.title("MicroStrip Antenna Calculator")
fenetre_main.geometry("330x190")
fenetre_main.minsize(330,190)
fenetre_main.maxsize(330,190)
#icon=PhotoImage(file="H:\\Enseignements\\Python\\TP\\TP6\\antenne.png")
#fenetre_main.iconphoto(True,icon)

zone_entree_donnee=Frame(fenetre_main,borderwidth=2,relief=GROOVE)
zone_entree_donnee.pack(pady=10)

entree_donnee_text=Label(zone_entree_donnee,text="Épaisseur du substrat:",font=("Calibri light",11))
entree_donnee_text.grid(column=0,row=0)
h_substrat = Entry(zone_entree_donnee,width=7)
h_substrat.grid(column=15,row=0)
entree_donnee_text=Label(zone_entree_donnee,text="cm",font=("Calibri light",11))
entree_donnee_text.grid(column=23,row=0)

entree_donnee_text=Label(zone_entree_donnee,text="Fréquence de l'antenne souhaitée:",font=("Calibri light",11))
entree_donnee_text.grid(column=0,row=1)
fr_antenne = Entry(zone_entree_donnee,width=7)
fr_antenne.grid(column=15,row=1)
entree_donnee_text=Label(zone_entree_donnee,text="GHz",font=("Calibri light",11))
entree_donnee_text.grid(column=23,row=1)

entree_donnee_text=Label(zone_entree_donnee,text="Permittivité relative du substrat:",font=("Calibri light",11))
entree_donnee_text.grid(column=0,row=2)
Epsilon_r = Entry(zone_entree_donnee,width=7)
Epsilon_r.grid(column=15,row=2)
entree_donnee_text=Label(zone_entree_donnee,text="Eps_r",font=("Calibri light",11))
entree_donnee_text.grid(column=23,row=2)

zone_resulats=Frame(fenetre_main,borderwidth=2,relief=GROOVE)
zone_resulats.pack(pady=10)

resultats=Label(zone_resulats,text="Rayon de l'antenne:",font=("Calibri Bold:",12))
resultats.grid(column=0,row=0)
resultats=Label(zone_resulats,text="cm",font=("Calibri Bold:",11))
resultats.grid(column=15,row=0)

bouton_calcul=Button(fenetre_main,text="Calcul",width=10,font=("Calibri Bold",10),command=calculRayon)
bouton_calcul.pack(pady=2)

fenetre_main.mainloop()
