from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat(pos)
mc.postToChat("your X position: " + str(pos.x))
mc.postToChat("your y position: " + str(pos.y))
mc.postToChat("your z position: " + str(pos.z))