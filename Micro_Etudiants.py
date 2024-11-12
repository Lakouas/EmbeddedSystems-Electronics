from datetime import datetime
listes_etudiants = {}

def traitement_nom(nom_f,prenom_f) :
    nom_f=nom_f.strip() # nom = KHARROUBI ->KHARROUBI
    nom_f=nom_f.upper() # nom = khArroubi -> KHARROUBI
    prenom_f = prenom_f.strip()
    prenom_f = prenom_f.upper()
    nom_complet_f = nom_f+" "+prenom_f # -> KHARROUBI HAKIM
    return nom_complet_f

def traitement_note() :
    while True :
        cc_f = float(input("la note du cc(/20):?"))
        if cc_f>20 :
            print(F"Erreur {cc_f}>20:")
        elif cc_f<0 :
            print(F"Erreur {cc_f}<0:")
        else :
            break
    while True :
        emd_f = float(input("la note du emd(/20):?"))
        if emd_f>20 :
            print(F"Erreur {emd_f}>20:")
        elif cc_f<0 :
            print(F"Erreur {emd_f}<0:")
        else :
            break
    cc_f = round(cc_f,2)
    emd_f = round(emd_f,2)
    moyenne_f = 0.4*cc_f + 0.6*emd_f
    moyenne_f = round(moyenne_f,2)
    return moyenne_f,cc_f,emd_f


print(F"-------------------------------------------------------------------------\n"
      F"Bonjour, Bienvenue dans Micro_Etudiants(0.1/0.0) Que souhaiteriez-vous faire ?\n"
      F"-------------------------------------------------------------------------"
      F"-->")
while True :
    cmd=int(input(F"1. Ajouter un étudiant ? |2. Supprimer un étudiant ?| 3.Afficher la liste des étudiants ?"
          F"| 4.Ajouter une note (calcul de la moyenne)?| 5.Enregistrez dans un fichier texte.?\n")) # cmd : commande
    if cmd==1 :
        print("Ajouter un étudiant:Veuillez entrer->")
        nom = input("le nom de l'étudiant:?")
        prenom = input("le Prénom de l'étudiant:?")
        nomComplet = traitement_nom(nom,prenom)
        if nomComplet in listes_etudiants :
            print(F"L'étudiant {nomComplet} existe déjà.\n")
        else :
            listes_etudiants.update({nomComplet:''})
    elif cmd==2:
        print("Supprimer un étudiant :Veuillez entrer->")
        nom = input("le nom de l'étudiant:?")
        prenom = input("le Prénom de l'étudiant:?")
        nomComplet = traitement_nom(nom,prenom)
        if nomComplet in listes_etudiants :
            listes_etudiants.pop(nomComplet,None)
            print(F"L'étudiant {nomComplet} vient d'être supprimé de la base de données.\n")
        else :
            print(F"L'étudiant {nomComplet}n'existe pas dans la base de données..\n")
    elif cmd==3:
        print(listes_etudiants)
    elif cmd==4:
        print("Ajouter une note :Veuillez entrer->")
        nom = input("le nom de l'étudiant:?")
        prenom = input("le Prénom de l'étudiant:?")
        nomComplet = traitement_nom(nom,prenom)
        if nomComplet in listes_etudiants :
            moy,cc,emd=traitement_note()
            listes_etudiants[nomComplet]=cc,emd,moy
        else :
            print(F"L'étudiant {nomComplet}n'existe pas dans la base de données..\n")
    elif cmd==5 :
        fichier = open('notes_micro_etudiants.txt','a')
        temps = datetime.now()
        temps= temps.strftime("%Y-%m-%d %H:%M:%S")
        fichier.write(f"Micro_Etudiants(0.1/0.0)\n")
        fichier.write(f"{str(temps)}\n")
        liste = list(listes_etudiants.keys())
        fichier.write(f"id;Nom & Prénom;cc;emd;moy\n")
        for i in range(len(liste)):
            fichier.write(f";{liste[i]};")
            for j in range(len(listes_etudiants[liste[i]])) :
                fichier.write(f"{listes_etudiants.get(liste[i])[j]};")
            fichier.write(f"\n")
        fichier.close()
        print("Enregistrement effectué avec succès.")
    else :
        pass
