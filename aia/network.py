# coding: utf-8
import numpy as np
import pickle
from aia.layers import Relu, Affine, SoftmaxWithLoss, MSELoss
from collections import OrderedDict

class NeuralNetwork:
    def __init__(self, input_size, output_size, hidden_sizes = [50], weight_init_std=0.01):
        self.params = {}

        self.params['W1'] = np.random.randn(input_size, hidden_sizes[0]) / np.sqrt(input_size)
        self.params['b1'] = np.zeros(hidden_sizes[0])
        
        for i in range(1, len(hidden_sizes)):
            self.params['W' + str(i+1)] = np.random.randn(hidden_sizes[i-1], hidden_sizes[i]) / np.sqrt(hidden_sizes[i-1])
            self.params['b' + str(i+1)] = np.zeros(hidden_sizes[i])
            
        self.params['W' + str(len(hidden_sizes)+1)] = np.random.randn(hidden_sizes[-1], output_size) / np.sqrt(hidden_sizes[-1])
        self.params['b' + str(len(hidden_sizes)+1)] = np.zeros(output_size)

        self.layers = OrderedDict()
        
        for i in range(1, len(hidden_sizes)+1):
            self.layers['Affine' + str(i)] = Affine(self.params['W' + str(i)], self.params['b' + str(i)])
            self.layers['Relu' + str(i)] = Relu()
        
        self.layers['Affine' + str(len(hidden_sizes)+1)] = Affine(self.params['W' + str(len(hidden_sizes)+1)], self.params['b' + str(len(hidden_sizes)+1)])
        self.lastLayer = SoftmaxWithLoss()
        
        self.affine_layers_count = len(hidden_sizes) + 1

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        
        return x
        
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
    def gradient(self, x, t):
        # forward
        self.loss(x, t)
        
        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)
        
        # setting
        grads = {}

        for i in range(1, self.affine_layers_count + 1):
            grads['W' + str(i)] = self.layers['Affine' + str(i)].dW
            grads['b' + str(i)] = self.layers['Affine' + str(i)].db
        
        return grads

    def save_params(self, file_name="params.pkl"):
        params = {}
        for key, val in self.params.items():
            params[key] = val
        with open(file_name, 'wb') as f:
            pickle.dump(params, f)
    
    def load_params(self, file_name="params.pkl"):
        with open(file_name, 'rb') as f:
            params = pickle.load(f)
        for key, val in params.items():
            self.params[key] = val

        for i in range(1, self.affine_layers_count + 1):
            self.layers['Affine' + str(1)].W = self.params['W' + str(1)]
            self.layers['Affine' + str(1)].b = self.params['b' + str(1)]

class RegressionNetwork(NeuralNetwork):
    def __init__(self, input_size, output_size, hidden_sizes = [50], weight_init_std=0.01):
        self.params = {}

        self.params['W1'] = np.random.randn(input_size, hidden_sizes[0]) / np.sqrt(input_size)
        self.params['b1'] = np.zeros(hidden_sizes[0])
        
        for i in range(1, len(hidden_sizes)):
            self.params['W' + str(i+1)] = np.random.randn(hidden_sizes[i-1], hidden_sizes[i]) / np.sqrt(hidden_sizes[i-1])
            self.params['b' + str(i+1)] = np.zeros(hidden_sizes[i])
            
        self.params['W' + str(len(hidden_sizes)+1)] = np.random.randn(hidden_sizes[-1], output_size) / np.sqrt(hidden_sizes[-1])
        self.params['b' + str(len(hidden_sizes)+1)] = np.zeros(output_size)
        
        self.layers = OrderedDict()
        
        for i in range(1, len(hidden_sizes)+1):
            self.layers['Affine' + str(i)] = Affine(self.params['W' + str(i)], self.params['b' + str(i)])
            self.layers['Relu' + str(i)] = Relu()

        self.layers['Affine' + str(len(hidden_sizes)+1)] = Affine(self.params['W' + str(len(hidden_sizes)+1)], self.params['b' + str(len(hidden_sizes)+1)])
        self.lastLayer = MSELoss()
        
        self.affine_layers_count = len(hidden_sizes) + 1