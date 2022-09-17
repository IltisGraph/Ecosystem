import copy

import Brain as b
import random

class Bakterie:
    def __init__(self, name, type, x, y, color = None):
        self.name = name
        self.type = type
        self.x, self.y = x, y
        self.color = color if color is not None else (0, 0, 0)
        self.Brain = b.Brain()
        self.lastHealth = 100
        self.lastStamina = 100
        self.isDead = False
        self.health = 100
        self.stamina = 100

    def draw(self, pg, Fenster):
        pg.draw.rect(Fenster, (self.color), (self.x, self.y, 10, 10))

    def checkDead(self):
        if self.x > 500 or self.x < 0 or self.y > 500 or self.y < 0:
            self.health = 0
            self.isDead = True

    def actualize(self):
        self.checkDead()
        out = []
        good = 1

        self.x += 0.1
        self.lastHealth = self.health
        self.lastStamina = self.stamina
        if self.health >= self.lastHealth:
            out.append(1)

        else:
            out.append(0)

        if self.health < self.lastHealth:
            out.append(1)
        else:
            out.append(0)
        if self.stamina >= self.lastStamina:
            out.append(1)
        else:
            out.append(0)
        if self.stamina < self.lastStamina:
            out.append(1)
        else:
            out.append(0)
        entscheidung = self.Brain.entscheide(out)
        print(entscheidung)
        ent = copy.copy(entscheidung)
        randomEntscheidung = random.randint(1, 100) / 100

        if randomEntscheidung <= entscheidung[0]:
            entfuer = 0
        elif randomEntscheidung > entscheidung[0] and randomEntscheidung < sum(entscheidung[:2]):
            entfuer = 1
        elif randomEntscheidung >= sum(entscheidung[:2]) and randomEntscheidung < sum(entscheidung[:3]):
            entfuer = 2
        else:
            entfuer = 3
        entscheidung = entscheidung.index(max(entscheidung))

        if entfuer == 0:
            self.y -= 1

        elif entfuer == 1:
            self.x += 1
        elif entfuer == 2:
            self.y += 1
        elif entfuer == 3:
            self.x -= 1

        #trainieren

        trY = [0 for i in range(4)]
        trY[entfuer] = ent[entfuer] + 0.1 if ent[entfuer] < 1 else ent[entfuer]

        self.Brain.learn([ent], [trY], 3)




