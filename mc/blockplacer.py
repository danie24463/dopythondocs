#Daniel Opoku
# Building a house by pressing a button
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def build():
    pos=mc.player.getTilePos()
    mc.setBlocks(pos.x+1, pos.y+0, pos.z+1, pos.x-7, pos.y-4, pos.z-5, 45)
    mc.setBlocks(pos.x+0, pos.y-1, pos.z+0, pos.x-6, pos.y-3, pos.z-4, 0)
    mc.setBlock(pos.x-7, pos.y-3,pos.z-2, 64)
    mc.setBlock(pos.x-7, pos.y-2,pos.z-2, 64)
    mc.setBlock(pos.x-6, pos.y-1,pos.z-1, 50)
    mc.setBlock(pos.x-6, pos.y-1,pos.z-3, 50)
    mc.setBlock(pos.x-7, pos.y-1,pos.z-1, 102)
 



#use a module to control time
import time

#Setup for buttons and LEDA
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


#se up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
   
    if GPIO.input(6) == GPIO.LOW:
        build()