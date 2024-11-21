from machine import Pin, time_pulse_us
from time import sleep_us,sleep

echo = Pin(12,Pin.IN)
trig = Pin(14,Pin.OUT,value=0)

def mesureDistance () : 

    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    dureeImpulsion = time_pulse_us(echo,1,10000) 
    if dureeImpulsion == 0 : 
        distance = 0 
    else : 
        distance = (dureeImpulsion * 0.0343) / (2)
    
    return distance 

while True : 
    distance_cm_moy=0
    for i in range(20): 
        distance_cm = mesureDistance() 
        distance_cm_moy += distance_cm

    distance_cm = distance_cm_moy/20

    if distance_cm <= 0 : 
        print("Erreur ! \n")
    else : 
        distance_cm = round(distance_cm,1)
        print(f"Distance={distance_cm}CM \n")
    sleep(1) 

