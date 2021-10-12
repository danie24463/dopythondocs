#Daniel Opoku
# Get block
import time


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lists=["gaming", "chair","elctrodes"]
while True:
    if GPIO.input(6) == GPIO.LOW:
        pos=mc.player.getTilePos()
        print("button 6 was pressed")
        blockData=mc.getBlock(pos.x, pos.y-1, pos.z)
        print(blockData)
        if blockData==57:
            mc.player.setTilePos(pos.x, pos.y +20, pos.z)