def neuralNetwork(inp, weights):
    prediction = [0,0]
    for i in range(len(weights)):
        prediction[i] = inp * weights[i]
    return prediction

print(neuralNetwork(4, [0.2, 0.5]))