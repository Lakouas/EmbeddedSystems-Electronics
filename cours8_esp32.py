from machine import Pin,UART
from time import sleep_us,sleep_ms,sleep
import dht

uart = UART(1, baudrate=9600,tx=Pin(4),rx=Pin(5))
led_cpu = Pin(25,Pin.OUT)
indice = False
uart.init(bits=8,parity=None,stop=2)
capteur = dht.DHT22(Pin(15))
temp=0
hum =0 

while True:
    led_cpu.value(indice)
    if uart.any() :
        data = uart.read()
        print(str(data))
        if data== b'm' :
            capteur.measure()
            temp = capteur.temperature()
            hum = capteur.humidity()
            print(temp)
            print(hum)
            uart.write(str(f"{temp}{hum}"))
            indice=not(indice)
        else :
            pass
