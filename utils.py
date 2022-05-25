import math

import numpy as np


# step function
def step(value, _):
    if value < 0:
        return 0
    else:
        return 1


# sigmoid function
def sigmoid(value, _):
    return 1 / (1 + math.exp(-value))


def sigmoid_choose_random(value, iter_count):
    # todo use iter_count to define temperature
    temperature = 1
    p_1 = sigmoid(value/temperature)
    print(f"Iter count: {iter_count}\n")
    return np.random.choice([0, 1], p=[1 - p_1, p_1])
