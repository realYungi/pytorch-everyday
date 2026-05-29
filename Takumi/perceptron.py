import numpy as np


class Perceptron:
    def __init__(self, train_data):
        self.train_data = train_data
        self.param = None

    def train(self):
        self.param = np.zeros(self.train_data[0][0].shape)

        while True:
            mistakes = 0
            for x, y in self.train_data:
                if y * np.dot(self.param, x) <= 0:
                    self.param += y * x
                    mistakes += 1
            if mistakes == 0:
                break

    def predict(self, x):
        return 1 if np.dot(self.param, x) >= 0 else -1
    
if __name__ == "__main__":
    train_data = [
        (np.array([1, 1]), 1),
        (np.array([1, -1]), -1),
        (np.array([-1, 1]), -1),
        (np.array([-1, -1]), -1)
    ]
    perceptron = Perceptron(train_data)
    perceptron.train()
    
    test_data = [
        np.array([2, 2]),
        np.array([2, -2]),
        np.array([-2, 2]),
        np.array([-2, -2])
    ]
    
    for x in test_data:
        print(f"Prediction for {x}: {perceptron.predict(x)}")