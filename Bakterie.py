from Brain import Brain


class Bakterie:
    def __init__(self, name, color, x, y):
        self.name, self.color = name, color
        self.x, self.y = x, y
        self.HP = 100
        self.lastHP = 100
        self.isHurting = False
        self.brain = Brain(3, 64, 2, 4)


    def draw(self, pg, fenster):
        pg.draw.rect(fenster, self.color, (self.x, self.y, 10, 10))

    def actualize(self):
        self.lastHP = self.HP

        # TODO: calculate if damage have been taken


        forBrain = [0 for i in range(2)]
        forBrain[0] = 1 if self.isHurting else 0
        forBrain[1] = 1 if not self.isHurting else 0

        out = self.brain.entscheide(forBrain)

        self.useBrainData(out)


    def useBrainData(self, data):

        entschieden = data.index(max(data))

        if entschieden == 0:
            self.y -= 0.1
        elif entschieden == 1:
            self.x += .1
        elif entschieden == 2:
            self.y += .1
        elif entschieden == 3:
            self.x -= .1
