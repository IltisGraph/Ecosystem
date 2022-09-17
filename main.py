import pygame as pg
from Bakterie import *
import random

edgar = Bakterie("Edgar", "Normal", 250, 250, (255, 0, 0))
bakterien = []
bakterien.append(edgar)
for i in range(10):
    bakterien.append(Bakterie("k", "Normal", 250, 250, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))


BACKGROUND_COLOR = (255, 255, 255)



pg.init()
Fenster = pg.display.set_mode((500, 500))
pg.display.set_caption("Bakterien Simulation!")


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    Fenster.fill(BACKGROUND_COLOR)

    for b, i in enumerate(bakterien):
        i.draw(pg, Fenster)
        i.actualize()
        if i.isDead:
            del bakterien[b]



    pg.display.update()
