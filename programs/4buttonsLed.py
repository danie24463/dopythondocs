#Daniel Opoku
#4 buttons 1 LED

#use a modules for requesting data online

import requests


#use a module to control time
import time

#Setup for buttons and LEDA
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


#se up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Start an infinite loop
while True:
    #wait for i second
    time.sleep(1)
    #check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("button 6 was pressed")
        requests.get("http://192.168.10.53:5000/sfx?file=bruh")
    elif GPIO.input(13) == GPIO.LOW:
        print("button 13 was pressed")
    elif GPIO.input(19) == GPIO.LOW:
        print("button 19 was pressed")
    elif GPIO.input(26) == GPIO.LOW:
        print("button 26 was pressed")