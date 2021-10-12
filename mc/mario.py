#Daniel Opoku
#Mc demo lists

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

woolLine= [13,12,8,7,1]
woolGrid= [[15,15,15,15,12,12,12,12,15,15,15,15,12,12,12,12,15,15,15,15],
           [15,15,15,15,15,12,12,12,15,15,15,15,12,12,12,15,15,15,15,15],
           [15,15,15,15,3,3,3,15,15,15,15,3,3,3,15,15,15,15,15,15],
           [15,5,5,5,5,5,5,15],
           [15,5,5,5,5,5,5,15],
           [15,5,5,5,5,5,5,15],
           [15,5,5,5,5,5,5,15],
           [15,5,0,0,0,0,5,15],
           [15,5,0,0,0,0,5,15],
           [15,5,5,5,5,5,5,15],
           [15,15,15,15,15,15,15,15,]]
pos =mc.player.getTilePos()

for i, wool in enumerate (woolLine):
    print (str(i) + "is the color" + str (wool))
    mc.setBlock (pos.x+i, pos.y, pos.z, 35, wool)
   
    
for i, row in enumerate (woolGrid):
    print(row)
    for j, col in enumerate(row):
        print(col)
        mc.setBlock (pos.x+j, pos.y+i, pos.z, 35, col)