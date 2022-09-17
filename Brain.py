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
            out.append(Neuron(random.randint(0, 100) / 100))

        self.Layer.append(out)

        for i in range(self.layers):
            out = []
            for b in range(self.width):
                out.append(Neuron(random.randint(0, 100) / 100))

            self.Layer.append(out)

        out = []
        for i in range(self.widthOfOut):
            out.append(Neuron(random.randint(0, 100) / 100))

        self.Layer.append(out)



    def entscheide(self, input):

        assert self.widthOfInput == len(input)

        # there might be an error if this is not true
        assert self.layers > 1

        for i in range(self.widthOfInput):
            self.Layer[0][i].currentstate = input[i]

        for i in range(1, self.layers + 1):
            for b in range(self.width):
                if i == 1:
                    for c in range(self.widthOfInput):
                        self.Layer[i][b].currentstate += self.Layer[0][c].currentstate * self.Layer[i][b].number
                else:
                    for c in range(self.width):
                        self.Layer[i][b].currentstate += self.Layer[i-1][c].currentstate * self.Layer[i][b].number


        for i in range(self.widthOfOut):
            for b in range(self.width):
                self.Layer[-1][i].currentstate += self.Layer[-2][b].currentstate * self.Layer[-1][i].number


        return [self.Layer[-1][b].currentstate for b in range(self.widthOfOut)]


    def getGenetics(self):

        out = []
        for i in range(self.layers + 2):
            if i != len(self.Layer) - 1 and i != 0:
                for b in range(self.width):
                    out.append(self.Layer[i][b].number)
            if i == len(self.Layer) - 1 and i != 0:
                for b in range(self.widthOfOut):
                    out.append(self.Layer[i][b].number)


        return out




