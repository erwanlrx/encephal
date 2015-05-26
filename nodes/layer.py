__author__ = 'marechaux'

from numpy import *

from nodes.node import *


class PerceptronLayer(PipeNode):
    """
    A node representing a hidden layer of a perceptron network.

    Attributes:
      bias (numpy.ndarray): a matrix of the layer's bias value for each unit (neuron)
      activation_function : the function the layer will use on the sum to compute the output value. Usually a sigmoid.
    """

    def __init__(self, size, activation_function):
        super().__init__(Vector(float, size), Vector(float, size))
        self.bias = zeros(size.total_size)
        self.activation_function = activation_function

    def propagation(self, input_socket, output_socket):
        output_socket.prop_data[:] += self.activation_function.function(input_socket.prop_data + self.bias)

    def backpropagation(self, input_socket, output_socket):
        """Computes the propagated error gradient for the hidden perceptron layer"""
        input_socket.backprop_data[:] += self.activation_function.differential(output_socket.prop_data) * output_socket.backprop_data #TODO change differential name...

    def learn(self, alpha, input_socket, output_socket):
        """Modifies the bias array using the computed (and propagated) error gradient"""
        self.bias[:] -= alpha * input_socket.backprop_data

    def randomize(self):
        """Initialiazises all the biases for each internal neuron to a random value"""
        self.bias[:] = 0.01*(random.random_sample(self.input_size.total_size)-0.5)
        #TODO: make parameters

class DropoutLayer(PipeNode):

    def __init__(self, size, p):
        super().__init__(size, size)
        self.input_data_prop = zeros(size)
        self.output_data_prop = zeros(size)
        self.input_data_backprop = zeros(size)
        self.output_data_backprop = zeros(size)
        self.filter = ones(size)
        self.p = p

    def propagation(self, learning = True):
        if learning:
            self.filter[:] = random.binomial(1, self.p, self.input_size)
            self.output_data_prop[:] = self.input_data_prop * self.filter
        else:
            self.output_data_prop[:] = self.input_data_prop
        #print(self.output_data_prop)

    def backpropagation(self):
        self.input_data_backprop[:] = self.output_data_backprop * self.filter

    def learn(self, alpha):
        pass
