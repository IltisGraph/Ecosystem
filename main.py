import pygame as pg
from Bakterie import Bakterie

Bakterien = []
for i in range(100):
    Bakterien.append(Bakterie("edgar", (255, 0, 0), 250, 250))



Fenster = pg.display.set_mode((500, 500))
pg.display.set_caption("Bakterien Simulation")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False



    Fenster.fill((255, 255, 255))

    for i in Bakterien:
        i.draw(pg, Fenster)
        i.actualize()

    pg.display.update()


pg.quit()