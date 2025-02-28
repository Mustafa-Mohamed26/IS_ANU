import numpy as np


def step_function(x):
    return np.where(x > 0, 1, 0)


def neural_network(X, weights, bias):
    z = np.dot(X, weights) + bias
    return step_function(z)


X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 1, 1, 1])

weights = np.random.rand(2)
bias = np.random.rand()

learning_rate = 0.1
epochs = 5

for epoch in range(epochs):
    for i in range(len(X)):
        prediction = neural_network(X[i], weights, bias)
        error = y[i] - prediction

        weights += learning_rate * error * X[i]
        bias += learning_rate * error

    print(f"Epoch {epoch + 1}: Weights = {weights}, Bias = {bias}")

print("\nTesting Neural Network:")
for i in range(len(X)):
    prediction = neural_network(X[i], weights, bias)
    print(f"Input: {X[i]}, Prediction: {prediction[0]}, Expected: {y[i]}")