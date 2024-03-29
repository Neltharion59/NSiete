import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.layers import Layer, Average
from runpy import run_path

__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
config = run_path(__location__ + "/../../config.py")

class ConvolutionalNeuralNetwork(Model):
    def __init__(self):
        super(ConvolutionalNeuralNetwork, self).__init__(name='convolutional_neural_network')

        self.inner_layers = [
            layers.Conv1D(
                filters=25,
                kernel_size=10,
                padding='same',
                activation='relu'
            ),
            layers.MaxPooling1D(
                pool_size=2,
                strides=1,
                padding='same',
                data_format='channels_last'
            ),
            layers.Conv1D(
                filters=50,
                kernel_size=10,
                padding='same',
                activation='relu'
            ),
            layers.MaxPooling1D(
                pool_size=2,
                strides=1,
                padding='same',
                data_format='channels_last'
            ),
            # layers.Conv1D(
            #     filters=100,
            #     kernel_size=10,
            #     padding='same',
            #     activation='relu'
            # ),
            # layers.MaxPooling1D(
            #     pool_size=2,
            #     strides=1,
            #     padding='same',
            #     data_format='channels_last'
            # ),
            # layers.Conv1D(
            #     filters=60,
            #     kernel_size=10,
            #     padding='same',
            #     activation='relu'
            # ),
            # layers.MaxPooling1D(
            #     pool_size=2,
            #     strides=1,
            #     padding='same',
            #     data_format='channels_last'
            # ),
            # layers.Conv1D(
            #     filters=50,
            #     kernel_size=10,
            #     padding='same',
            #     activation='relu'
            # ),
            # layers.Flatten(),
            # layers.Dense(
            #     units=1024,
            #     activation='relu'
            # ),
        ]

        # self.flatten =  Flatten()
        # self.dense = Dense(
        #         units=input_dim,  
        #         activation='relu'),

    def call(self, x):
        for layer in self.inner_layers:
            x = layer(x) 

        return x
