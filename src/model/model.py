import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.layers import Layer
from runpy import run_path

__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
config = run_path(__location__ + "/../../config.py")

class ConvolutionalNeuralNetwork(Model):
    def __init__(self):
        super(ConvolutionalNeuralNetwork, self).__init__(name='convolutional_neural_network')

        self.inner_layers = [
            layers.Conv1D(
                filters=50,
                kernel_size=5,
                padding='same',
                activation='sigmoid'
            ),
            layers.Conv1D(
                filters=50,
                kernel_size=5,
                padding='same',
                activation='relu'
            ),
            layers.Conv1D(
                filters=50,
                kernel_size=5,
                padding='same',
                activation='relu'
            )
        ]
        # self.flatten =  Flatten()
        # self.dense = Dense(
        #         units=input_dim,
        #         activation='relu'),

    def call(self, x):
        for layer in self.inner_layers:
            x = layer(x)

        # x = flatten(x)
        # x = dense(x)

        return x
