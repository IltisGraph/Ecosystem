import random

import neat
import pygame as pg
import os

pg.init()
Fenster = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
FPS = 144


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.food = 100
        self.health = 100
        self.color = (0, 0, self.food + 50)

    def draw(self):
        pg.draw.rect(Fenster, self.color, (self.x, self.y, 10, 10))

    def actualize(self):

        if self.x < 0 or self.x > 500 or self.y < 0 or self.y > 500:
            self.health = 0
            self.food = 0


        self.food -= 0.01 if self.food > 0 else 0
        if self.food <= 0:
            self.food = 0
            self.health -= 1
        if self.food == 100:
            self.health += 1

        if self.food > 0 and self.health < 100:
            self.food -= 1
            self.health += 1

    def go(self, data):

        if data[4] >= 0.5:
            return
        if self.food > 0:
            if data[0] >= 0.5:
                self.y -= 1
                self.food -= 0.05
            if data[1] >= 0.5:
                self.x += 1
                self.food -= 0.05
            if data[2] >= 0.5:
                self.y += 1
                self.food -= 0.05
            if data[3] >= 0.5:
                self.x -= 1
                self.food -= 0.05


    def giveData(self):
        out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        out[0] = self.y
        out[1] = 500 - self.x
        out[2] = 500 - self.y
        out[3] = self.x

        is_oben = False
        is_unten = False
        is_rechts = False
        is_links = False

        for f in Foods:
            if self.x > f.x and self.x < f.x + 20 and self.y > f.y:
                is_oben = True
            if self.x > f.x and self.x < f.x + 20 and self.y <= f.y:
                is_unten = True
            if self.y > f.y and self.y < f.y + 20 and self.x > f.x:
                is_links = True
            if self.y > f.y and self.y < f.y + 20 and self.x <= f.x:
                is_rechts = True

            if is_oben and is_unten and is_rechts and is_links:
                break

        out[4] = 1 if is_oben else 0
        out[5] = 1 if is_rechts else 0
        out[6] = 1 if is_unten else 0
        out[7] = 1 if is_links else 0

        out[8] = self.food
        out[9] = self.health

        return out

    def check_food(self):

        if self.food < 100:
            for i, f in enumerate(Foods):
                if self.x > f.x and self.x < f.x + 20 and self.y > f.y and self.y < f.y + 20:
                    Foods.pop(i)
                    self.food = self.food + 30 if self.food + 30 < 100 else 100
                    break


Foods = []

class Food:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pg.draw.rect(Fenster, (0, 255, 0), (self.x, self.y, 20, 20))

def main(genomes, config):

    global FPS, Foods
    Foods = []
    nets = []
    ticks = 0
    ge = []
    Spieler = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)
        Spieler.append(Player(250, 250))
        Foods.append(Food(random.randint(0, 480), random.randint(0, 480)))
        Foods.append(Food(random.randint(0, 480), random.randint(0, 480)))


    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    FPS = 1440
                if event.key == pg.K_DOWN:
                    FPS = 144
                if event.key == pg.K_SPACE:
                    FPS = 0

        Fenster.fill((255, 255, 255))

        ticks += 1
        if ticks >= 200:
            ticks = 0
            Foods.append(Food(random.randint(0, 480), random.randint(0, 480)))

        for f in Foods:
            f.draw()

        for i, s in enumerate(Spieler):
            s.draw()
            s.actualize()
            s.check_food()
            ge[i].fitness += 0.1

        for i, s in enumerate(Spieler):
            if s.health <= 0:
                Spieler.pop(i)
                ge[i].fitness -= 1
                ge.pop(i)
                nets.pop(i)

        for i, s in enumerate(Spieler):
            s.go(nets[i].activate(s.giveData()))

        if len(Spieler) == 0:
            running = False

        pg.display.update()

        #print(Spieler[0].food, Spieler[0].health)








def run(config_path):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50 ** 10)


if __name__ == "__main__":
    cur_path = os.path.dirname(__file__)
    config_path = os.path.join(cur_path, "config-forward.txt")
    run(config_path)