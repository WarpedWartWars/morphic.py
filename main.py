import morphic

world = morphic.World()#1920, 1080)
try:
    world.loop()
finally:
    morphic.pygame.quit()
