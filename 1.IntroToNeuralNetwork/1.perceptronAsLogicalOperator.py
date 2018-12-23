'''
    Code to Implement single perceptron as Logical Operator
        - AND operator
        - OR operator
'''


import pandas as pd

# Code for single perceptron
def singlePerceptron(correct_inputs, weight1, weight2, bias):
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    outputs = []
    for test_input, correct_input in zip(test_inputs, correct_inputs):
        linear_combination = weight1*test_input[0] + weight2*test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output ==correct_input else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination , output, is_correct_string])
    # Print output
    output_frame = pd.DataFrame(outputs , columns=['Input1','Input2', 'LinearOmbination', 'Activation Output', 'Is correct'])
    print(output_frame)


## AND OPERATOR
weight1 = 0.5
weight2 = 0.5
bias = -1.0
correct_inputs = [False, False, False, True]
singlePerceptron(correct_inputs, weight1, weight2,bias)

## OR OPERATOR
weight1 = 1
weight2 = 1
bias = -1.0
correct_inputs = [False, True, True, True]
singlePerceptron(correct_inputs, weight1, weight2,bias)

## NOT OPERATOR
# For uniary operators, first input of tuple is used
weight1 = -1
weight2 = 0
bias = 0.0
correct_inputs = [True, True, False, False]
singlePerceptron(correct_inputs, weight1, weight2,bias)

