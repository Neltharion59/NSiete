from scipy import signal
import numpy as np

def get_spectrogram(array, nfft=1024, padded=True):

    return signal.stft(array)

def get_magnitude(spectogram):
    return np.abs(spectogram)