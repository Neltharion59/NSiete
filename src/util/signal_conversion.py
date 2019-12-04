from librosa import stft
import numpy as np

def get_spectrogram(X, fs=16000, wd_size=1024, seg_size=1024, overlap=0, pad=True):

    return stft(X, n_fft=wd_size, hop_length=wd_size)
    # return signal.stft(array, fs=fs, nfft=nfft, nperseg=nperseg, noverlap=noverlap, padded=padded)

def get_magnitude(spectogram):
    return np.abs(spectogram)

def get_phase(spectrogram):
    return np.angle(spectrogram)

def construct_audio(magnitude, phase, seg_size=1024):
    pass
    

