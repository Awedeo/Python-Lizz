
from machine import Pin, PWM
import time

A = PWM(Pin(2))   # First solo buzzer
B = PWM(Pin(4))   # Second solo buzzer
C = PWM(Pin(15))  # Chant buzzer
buzzd = Pin(5, Pin.OUT)
buzze = Pin(18, Pin.OUT)


while True:

    A.freq(4940)
    time.sleep(0.15)
    A.freq(6590)
    time.sleep(0.15)
    A.freq(4940)
    time.sleep(0.15)
    A.freq(5870)
    time.sleep(0.15)
    A.freq(4940)
    time.sleep(0.15)
    A.freq(6590)
    time.sleep(0.15)
    A.freq(4940)
    time.sleep(0.15)
    A.freq(5870)
    time.sleep(0.15)



#"E5": 659, "D5": 587, "B4": 494, "A4": 440,
    #"G4": 392, "F#4": 370, "E4": 330, "D4": 294

    #"B4", "E5", "B4", "D5", "B4", "E5", "B4", "D5"
