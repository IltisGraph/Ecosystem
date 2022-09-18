from Brain import Brain


class Bakterie:
    def __init__(self, name, color, x, y):
        self.name, self.color = name, color
        self.x, self.y = x, y
        self.width = 10
        self.HP = 100
        self.lastHP = 100
        self.isHurting = False
        self.brain = Brain(3, 64, 2, 4)

    def draw(self, pg, fenster):
        pg.draw.rect(fenster, self.color, (self.x, self.y, self.width, self.width))

    def actualize(self):
        self.lastHP = self.HP

        forBrain = self.getBraindata()

        out = self.brain.entscheide(forBrain)

        self.useBrainData(out)

    def useBrainData(self, data):

        entschieden = data.index(max(data))

        if entschieden == 0 and self.y > 0:
            self.y -= 0.1
        elif entschieden == 1 and self.x < 500 - self.width:
            self.x += .1
        elif entschieden == 2 and self.y < 500 - self.width:
            self.y += .1
        elif entschieden == 3 and self.x > 0:
            self.x -= .1

    def getBraindata(self):
        if self.lastHP < self.HP:
            self.isHurting = False
        elif self.lastHP > self.HP:
            self.isHurting = True

        forBrain = [0 for i in range(2)]
        forBrain[0] = 1 if self.isHurting else 0
        forBrain[1] = 1 if not self.isHurting else 0

        return forBrain

