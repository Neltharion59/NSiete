from librosa import stft, istft
import numpy as np

def get_spectrogram(X, fs=16000, wd_size=2046, overlap=0, pad=True):
    res = stft(X, n_fft=wd_size, hop_length=wd_size//2, center=pad)
    return res

def get_magnitude(spectogram):
    return np.abs(spectogram)

def get_phase(spectrogram):
    return np.angle(spectrogram)

def construct_audio(magnitude, phase, wd_size=2046):
    tmp = magnitude * np.exp(1.j * phase)
    res = istft(tmp, wd_size//2)

    return res
    

