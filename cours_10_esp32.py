import dht
import network
import urequests
import ujson
from machine import Pin
from time import sleep,sleep_ms,sleep_us
SSID="Tenda_EXT"
MOT_DE_PASSE="hhhhhhhh"

lien = "http://kharroubihakim.xyz/reception_donnees.php"

def connect() :
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        print('connexion en cours ...\n')
        wlan.connect (SSID , MOT_DE_PASSE )
        while not wlan.isconnected():
            pass
    print ("Connecte au reseau WiFi :", SSID )
    print ("Adresse IP:", wlan . ifconfig () [ 0 ])
    
am=dht.DHT22(Pin(27))
connect()
while True :
    am.measure()
    temp=am.temperature()
    hum =am.humidity()
    print(temp)
    print(hum)
    reponse = urequests.get(f"{lien}?valeur1={temp}&valeur2={hum}")
    if reponse.status_code == 200 :
        print ("Donnees envoyees avec succes ")
    else :
        print ("Erreur lors de l’envoi des donnees :", reponse.status_code)
    sleep(1)
