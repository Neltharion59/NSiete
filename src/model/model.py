from tensorflow.keras import layers, Layer, Model

class RecurrentNeuralNetwork(Model):
    
    def __init__(self, dim_output):
        super(RecurrentNeuralNetwork, self).__init__(name='recurrent_neural_network')

        # self.model_layers = [
        #     Conv2D()     
        # ]

    def call(self, x):
        for layer in self.model_layers:
            x = layer(x)
        return x

class PreprocessingLayer(Layer):
    def __init__(self):
        super(PreprocessingLayer, self).__init__()

    def call(self, input_mono):
        


        return x
