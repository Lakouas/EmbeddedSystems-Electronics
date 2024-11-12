from tkinter import *

def direBonjour() :
    prenom = str(PrenomEtudiant.get().upper().strip())
    nom    = str(NomEtudiant.get().upper().strip())
    nom_complet=nom+' '+prenom
    return ZoneTextOut.configure(text=f"{nom_complet}")

app= Tk()
app.title("APP : Cours 9 / GUI")
app.geometry("640x480")

ZoneEntreeDonnees= Frame(app)
ZoneEntreeDonnees.grid(row=0,column=0)
ZoneText=Label(ZoneEntreeDonnees,text="Nom de l'étudiants:",font=("Calibri Bold",11))
ZoneText.grid(row=0,column=0,pady=5,padx=5)
NomEtudiant=Entry(ZoneEntreeDonnees,width=50)
NomEtudiant.grid(row=0,column=1,pady=5,padx=5)
ZoneText=Label(ZoneEntreeDonnees,text="Prénom de l'étudiants:",font=("Calibri Bold",11))
ZoneText.grid(row=1,column=0,pady=5,padx=5)
PrenomEtudiant=Entry(ZoneEntreeDonnees,width=50)
PrenomEtudiant.grid(row=1,column=1,pady=5,padx=5)
bouton=Button(ZoneEntreeDonnees,text="Entrer",command=direBonjour)
bouton.grid(row=2,column=1)
ZoneSortie = Frame(app)
ZoneSortie.grid(row=1,column=0)
ZoneText=Label(ZoneSortie,text="Bonjour M/Mme",font=("Calibri Bold",11))
ZoneText.grid(row=0,column=0,pady=5,padx=5)
ZoneTextOut=Label(ZoneSortie,text="----",font=("Calibri Bold",11))
ZoneTextOut.grid(row=0,column=1,pady=5,padx=5)
app.mainloop()
