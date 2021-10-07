#Daniel Opoku


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    import requests
    import time
    time.sleep(1)
    #check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("button 6 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    if GPIO.input(13) == GPIO.LOW:
        print("button 13 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down")
    if GPIO.input(19) == GPIO.LOW:
        print("button 19 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thunb=wiggle")