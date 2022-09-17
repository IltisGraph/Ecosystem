from Brain import Brain


class Bakterie:
    def __init__(self, name, color, x, y):
        self.name, self.color = name, color
        self.x, self.y = x, y


    def draw(self, pg, fenster):
        pg.draw.rect(fenster, self.color, (self.x, self.y, 10, 10))

    def actualize(self):
        pass