import machine
from machine import PWM, Pin
from time import sleep
import math
import sys
for x in range(1):
    print(x)
    left = PWM(Pin(14))
    left.freq(50)
    left.duty_u16(5000)
    sleep(1)
    left.duty_u16(5500)
    print("move left to 5500")

    shoulder = PWM(Pin(15))              
    shoulder.freq(50)
    shoulder.duty_u16(5000)
    sleep(1)
    shoulder.duty_u16(5500)
  
else:
  print("Finally finished!")
sleep(1)
left.duty_u16(5000)
  