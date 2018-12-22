import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    denominator = 0
    softmax_values = []
    for xi in L:
        exp_value = np.exp(xi)
        denominator = denominator + exp_value
        softmax_values.append(exp_value)
    for i in range(0, len(softmax_values)):
        softmax_values[i] = softmax_values[i] / denominator

    return softmax_values