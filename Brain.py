from keras import models, layers
import numpy as np


class Brain:
    def __init__(self):
        self.model = models.Sequential()
        self.model.add(layers.Dense(16, input_shape=(4, ), activation="relu"))
        self.model.add(layers.Dense(16, activation="relu"))
        self.model.add(layers.Dense(16, activation="relu"))
        self.model.add(layers.Dense(4, activation="sigmoid"))
        self.model.compile(optimizer="rmsprop", loss="mae", metrics=["mse", "accuracy"])

    def entscheide(self, data):
        out = self.model.predict(np.asarray([data]), verbose=None)
        out = list(out[0])
        return out

    def learn(self, dataX, dataY, tragedic):
        self.model.fit(np.asarray(dataX), np.asarray(dataY), epochs=tragedic, batch_size=4, verbose=None)

