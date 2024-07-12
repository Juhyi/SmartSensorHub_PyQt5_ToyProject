# led_blink.py
# Red led 
import RPi.GPIO as GPIO
import time

# RGB LED Pinnumber setting
red_pin = 4
green_pin = 6
blue_pin = 5 

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD(1~40)
GPIO.setup(red_pin, GPIO.OUT)   # 4 pin output
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

try:
    while(True):
        GPIO.output(red_pin, False)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, False)
        time.sleep(1) # 1sec가 기본

        #GPIO.output(red_pin, False)
        #GPIO.output(green_pin, True)
        #GPIO.output(blue_pin, False)
        #time.sleep(0.5) # 1sec가 기본
        
        #GPIO.output(red_pin, False)
        #GPIO.output(green_pin, False)
        #GPIO.output(blue_pin, True)
        #time.sleep(0.5) # 1sec가 기본
        
        GPIO.output(red_pin, True)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, True)
        time.sleep(0.5) # 1sec가 기본
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
    