import random


class Neuron:
    def __init__(self, number):
        self.number = number
        self.currentstate = 0


class Brain:
    def __init__(self, layers, width, width_of_input_layer, width_of_output_Layer):
        self.widthOfOut = width_of_output_Layer
        self.layers = layers
        self.width = width
        self.widthOfInput = width_of_input_layer
        self.Layer = []
        self.start()

    def start(self):

        # randomly initialise network
        out = []
        for i in range(self.widthOfInput):
            out.append(Neuron(random.randint(0, 10) / 10))

        self.Layer.append(out)

        for i in range(self.layers):
            out = []
            for b in range(self.width):
                out.append(Neuron(random.randint(0, 1000) / 1000))

            self.Layer.append(out)

        out = []
        for i in range(self.widthOfOut):
            out.append(Neuron(random.randint(0, 10) / 10))

        self.Layer.append(out)



    def entscheide(self, input):
        self.resetLayers()

        assert self.widthOfInput == len(input)

        # there might be an error if this is not true
        assert self.layers > 1

        for i in range(self.widthOfInput):
            self.Layer[0][i].currentstate = input[i]

        for i in range(1, self.layers + 1):
            for b in range(self.width):
                if i == 1:
                    for c in range(self.widthOfInput):
                        self.Layer[i][b].currentstate += self.Layer[0][c].currentstate * (self.Layer[i][b].number + self.Layer[0][c].number)
                else:
                    for c in range(self.width):
                        self.Layer[i][b].currentstate += self.Layer[i-1][c].currentstate * (self.Layer[i][b].number + self.Layer[i-1][c].number)


        for i in range(self.widthOfOut):
            for b in range(self.width):
                self.Layer[-1][i].currentstate += self.Layer[-2][b].currentstate * (self.Layer[-1][i].number + self.Layer[-2][b].number)


        return [self.Layer[-1][b].currentstate for b in range(self.widthOfOut)]



    def resetLayers(self):
        for b in range(self.layers):
            for i in range(self.width):
                self.Layer[b + 1][i].currentstate = 0

        for i in range(self.widthOfInput):
            self.Layer[0][i].currentstate = 0

        for i in range(self.widthOfOut):
            self.Layer[-1][i].currentstate = 0

    def getGenetics(self):

        out = []
        for i in range(self.layers + 2):
            if i != len(self.Layer) - 1 and i != 0:
                for b in range(self.width):
                    out.append(self.Layer[i][b].number)
            if i == len(self.Layer) - 1 and i != 0:
                for b in range(self.widthOfOut):
                    out.append(self.Layer[i][b].number)
            if i == 0:
                for b in range(self.widthOfInput):
                    out.append(self.Layer[0][b].number)


        return out

    def buildWithGenetics(self, genetics):

        print("DUBUG:", self.width * self.layers + self.widthOfInput + self.widthOfOut)
        #assert len(genetics) == self.width * self.layers + self.widthOfInput + self.widthOfOut

        total = 0
        for i in range(self.layers + 2):
            if i != self.layers + 1 and i != 0:
                for b in range(self.width):
                    self.Layer[i][b].number = genetics[total]
                    total += 1
            elif i == self.layers + 1 and i != 0:
                for b in range(self.widthOfOut):
                    self.Layer[i][b].number = genetics[total]
                    total += 1
            else:
                for b in range(self.widthOfInput):
                    self.Layer[i][b].number = genetics[total]
                    total += 1





