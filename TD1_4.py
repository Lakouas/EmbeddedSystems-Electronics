"""
Nom du programme : Antenne planaire Calculateur
Auteur : KHARROUBI Hakim (hlakouas2@gmail.com)
Date : 20/10/2023
Version/Révision : 0.1/0.0
"""
from math import sqrt, log, pi

Epsilon_r  = float(input("Quelle est la permittivité relative du substrat ? \n"))
h_substrat = float(input("Quelle est la hauteur du substrat en centimètres (cm) ? \n"))
fr_antenne = float(input("Quelle est la fréquence de résonance de l'antenne souhaitée (GHz)? \n"))

fr_antenne = fr_antenne * 1e9 # Fréquence en GHz

F = ((8.791)*(1e9))/(fr_antenne*(sqrt(Epsilon_r)))
B = (log((pi*F)/(2*h_substrat))) + (1.7726)
A = ((2*h_substrat)/(pi*Epsilon_r*F))*B
C=  sqrt(1+A)
rayon_antenne = F/C

print(F"---------------------------------------------------------->\n"
      F"Calculateur (Antenne planaire circulaire v0.1/0.0) : \n"
      F"Fréquence = {fr_antenne/1e9}GHZ | Epsilon_r = {Epsilon_r} : | Hauteur substrat : {h_substrat} cm\n"
      F"Rayon de l'antenne : {rayon_antenne} cm avec F={F} \n"
      F"Based on the cavity model formulation \n"
      F""
      F"---------------------------------------------------------->")
