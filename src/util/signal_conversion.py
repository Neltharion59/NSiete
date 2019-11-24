import scipy as sp
import numpy as np

def get_spectrogram(array):
    return sp.signal.stft(array)

def get_magnitude(spectogram):
    return np.abs(spectogram)