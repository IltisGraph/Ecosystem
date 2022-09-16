import pygame as pg

BACKGROUND_COLOR = (255, 255, 255)




Fenster = pg.display.set_mode((500, 500))
pg.display.set_caption("Bakterien Simulation!")


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    Fenster.fill(BACKGROUND_COLOR)


    pg.display.update()
