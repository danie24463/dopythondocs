#Daniel Opoku
#Places a randomly colored wool block

'''
Set up program for MC and 2 buttons
Create a 'counter' variable that starts at 0
create a list of blockdata numbers for different color wool
define a function called placeNext
    -it takes one argument called direction
    -it changes the counter by adding the direction argument
    -place a wool block of the color from list where
    the index matches the counter variable
    -if the counter is out of bounds of the index, reset it
In a forever loop
    -if the first button was pessed, placeNext(1)
    -if the second button was pessed, placeNext(-1)
'''
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter=0
woolColors=[1,2,3,4,5,9]
def placeNext(direction):
    global counter
    counter+=direction
    pos=mc.player.getTilePos()
    mc.setBlock(pos.x,pos.y,pos.z,35,woolColors[counter])
    if woolColors=>5:
        placenext = 0
    if woolColors<0:
        PlaceNext = 5
while True:
   
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    if GPIO.input(13) == GPIO.LOW:
        placeNext(-1)