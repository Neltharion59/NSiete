import os
import numpy as np
from tensorflow.keras import layers, Layer, Model

__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
util_tools = run_path(__location__ + "/../util/signal_conversion.py")
config = run_path(__location__ + "/../../config.py")

class RecurrentNeuralNetwork(Model):
    def __init__(self, dim_output):
        super(RecurrentNeuralNetwork, self).__init__(name='recurrent_neural_network')
        self.preprocessing_layer = PreprocessingLayer()
        self.decomposing_layer = DecomposingLayer()
        self.composing_layer = ComposingLayer()

        self.inner_layers = [
            layers.LSTM(units=config["chunk_size"], return_sequences=True),
            layers.LSTM(units=config["chunk_size"], return_sequences=True),
            layers.LSTM(units=config["chunk_size"], return_sequences=True),
            layers.Dense(units=config["chunk_size"], activation="softmax")
        ]

    def call(self, x):
        for layer in self.model_layers:
            x = layer(x)
        return x

class PreprocessingLayer(Layer):
    def __init__(self):
        super(PreprocessingLayer, self).__init__()

    def call(self, input_mono):
        spectrogram = util_tools["get_spectrogram"](input_mono)
        magnitude = util_tools["get_magnitude"](spectrogram)
        phase = util_tools["get_phase"](spectrogram)

        return magnitude, phase


class DecomposingLayer(Layer):
    def __init__(self):
        super(DecomposingLayer, self).__init__()

    def call(self, input_mono):
        # 32768
        chunk_size = config["chunk_size"]

        chunk_count = np.floor(len(input_mono) / chunk_size)
        chunks = []
        for i in range(chunk_count):
            chunks.append(input_mono[i*chunk_size:(i+1)*chunk_size, :])
        
        return np.array(chunks), input_mono[chunk_count*chunk_size:]

class ComposingLayer(Layer):
    def __init__(self):
        super(ComposingLayer, self).__init__()

    def call(self, chunks, last_chunk):
        chunk_count = len(chunks)
        output_mono = []
        for i in range(chunk_count):
            output_mono = output_mono + chunks[i]
        else:
            if(last_chunk):
                output_mono = output_mono + last_chunk
        
        return np.array(output_mono)

class MaskingLayer(Layer):
    def __init__(self):
        super(MaskingLayer, self).__init__()

    def call(self, chunks, last_chunk):
        chunk_count = len(chunks)
        output_mono = []
        
        
        return np.array(output_mono)