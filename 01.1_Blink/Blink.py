from time import sleep_ms
from machine import Pin

sleep_time = 500
long_time = 1000
short_time = 200

def s():
    red.value(1)        
    sleep_ms(short_time)
    red.value(0)        
    sleep_ms(sleep_time)
    
def l():
    red.value(1)        
    sleep_ms(long_time)
    red.value(0)        
    sleep_ms(sleep_time) 

def b():
    blue.value(1)
    sleep_ms(short_time)
    blue.value(0)
    sleep_ms(sleep_time)

blue=Pin(0,Pin.OUT)
red=Pin(2,Pin.OUT)

try:
    while True:
        red.value(0)
        sleep_ms(3000)
        
        l()
        l()
        s()
        b()
        l()
        s()
        s()
        s()
        b()
        s()
        l()
        s()
except:
    pass





