import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.layers import Layer
from runpy import run_path

tf.compat.v1.disable_eager_execution()

__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
util_tools = run_path(__location__ + "/../util/signal_conversion.py")
config = run_path(__location__ + "/../../config.py")

class RecurrentNeuralNetwork(Model):
    def __init__(self):
        super(RecurrentNeuralNetwork, self).__init__(name='recurrent_neural_network')
        # self.preprocessing_layer = PreprocessingLayer()
        # self.decomposing_layer = DecomposingLayer()
        # self.composing_layer = ComposingLayer()
        self.masking_layer = MaskingLayer()

        self.inner_layers = [
            layers.LSTM(units=config["chunk_size"], return_sequences=True),
            layers.LSTM(units=config["chunk_size"], return_sequences=True),
            layers.LSTM(units=config["chunk_size"], return_sequences=True),
            layers.Dense(units=config["chunk_size"], activation="softmax")
        ]

    def call(self, x):
        magnitude = self.preprocessing_layer(x)
        chunks = self.decomposing_layer(x)
        modified_chunks = []
        for i in range(len(chunks)):
           tmp = chunks[i]
           for layer in self.inner_layers:
               tmp = layer(tmp)
           tmp = masking_layer(tmp, magnitude)
           modified_chunks.append(tmp)
        out = self.composing_layer(modified_chunks)

        return x

class PreprocessingLayer(Layer):
    def __init__(self):
        super(PreprocessingLayer, self).__init__()

    def call(self, input_mono):
        spectrogram = util_tools["get_spectrogram"](input_mono)
        magnitude = util_tools["get_magnitude"](spectrogram)
        # phase = util_tools["get_phase"](spectrogram)

        return magnitude  #, phase


class DecomposingLayer(Layer):
    def __init__(self):
        super(DecomposingLayer, self).__init__()

    def call(self, magnitude):
        # 32768
        chunk_size = config["chunk_size"]

        chunk_count = np.floor(len(magnitude) / chunk_size)
        chunks = []
        for i in range(chunk_count):
            chunks.append(magnitude[i*chunk_size:(i+1)*chunk_size, :])
        
        return np.array(chunks)  # , magnitude[chunk_count*chunk_size:]

class ComposingLayer(Layer):
    def __init__(self):
        super(ComposingLayer, self).__init__()

    def call(self, chunks):
        chunk_count = len(chunks)
        output_mono = []
        for i in range(chunk_count):
            output_mono = output_mono + chunks[i]
        # else:
        #     if(last_chunk):
        #         output_mono = output_mono + last_chunk
        
        return np.array(output_mono)

class MaskingLayer(Layer):
    def __init__(self):
        super(MaskingLayer, self).__init__()

    def call(self, prediction, orig_mixed):
        output = prediction / (prediction + np.finfo(float).eps) * orig_mixed
        return output