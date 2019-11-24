#!/usr/bin/env python

import os
import random
import scipy.io.wavfile as wavfile
import numpy as np
import librosa
from runpy import run_path

__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
# __location__ = "\\".join(__location__.split("\\")[:-2])

#input_directory_name_stereo = __location__ + "/../../data/MIR-1K/Wavfile/"
input_directory_name_mono = __location__ + "/../../data/MIR-1K/Wavfile_mono/"
input_directory_name_voice = __location__ + "/../../data/MIR-1K/Wavfile_voice/"
input_directory_name_music = __location__ + "/../../data/MIR-1K/Wavfile_music/"

config = run_path(__location__ + "/../../config.py")
util_tools = run_path(__location__ + "/../util/signal_conversion.py")

def initialize_sample_pool():

    file_names = [file_name for file_name in os.listdir(input_directory_name_mono) if file_name[-4:] == ".wav"]

    file_count = min(config["sample_count"], len(file_names))
    work_file_names = random.sample(file_names, file_count)

    #work_file_names = ["abjones_2_01.wav", "abjones_1_01.wav"]

    return work_file_names

def read_sample_file(file_name):
    data_merged, sample_rate = librosa.load(input_directory_name_mono + file_name)
    data_separate = librosa.load((input_directory_name_voice if config["separation_target"] == "voice" else input_directory_name_music) + file_name)[0]

    chunk_size = config["chunk_size"]
    chunk_count = int(np.floor(len(data_merged) / chunk_size))

    # data_merged = data_merged[:int(chunk_size * chunk_count)]
    # data_separate = data_separate[:int(chunk_size * chunk_count)]

    spectrogram_m = util_tools["get_spectrogram"](data_merged)
    magnitude_m = util_tools["get_magnitude"](spectrogram_m).tolist()
    chunks_m = []
    for i in range(chunk_count):
        chunks_m.append(magnitude_m[i*chunk_size:(i+1)*chunk_size])

    spectrogram_s = util_tools["get_spectrogram"](data_separate)
    magnitude_s = util_tools["get_magnitude"](spectrogram_s).tolist()
    chunks_s = []
    for i in range(chunk_count):
        chunks_s.append(magnitude_s[i*chunk_size:(i+1)*chunk_size])

    return chunks_m, chunks_s, sample_rate
