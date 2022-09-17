import pygame as pg



Fenster = pg.display.set_mode((500, 500))
pg.display.set_caption("Bakterien Simulation")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False



    Fenster.fill((255, 255, 255))

    pg.display.update()


pg.quit()