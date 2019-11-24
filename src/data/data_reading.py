#!/usr/bin/env python

import os
import random
import scipy.io.wavfile as wavfile
import numpy as np
from runpy import run_path

__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
# __location__ = "\\".join(__location__.split("\\")[:-2])

#input_directory_name_stereo = __location__ + "/../../data/MIR-1K/Wavfile/"
input_directory_name_mono = __location__ + "/../../data/MIR-1K/Wavfile_mono/"
input_directory_name_voice = __location__ + "/../../data/MIR-1K/Wavfile_voice/"
input_directory_name_music = __location__ + "/../../data/MIR-1K/Wavfile_music/"

config = run_path(__location__ + "/../../config.py")

def initialize_sample_pool():

    file_names = [file_name for file_name in os.listdir(input_directory_name_mono) if file_name[-4:] == ".wav"]

    file_count = min(config["sample_count"], len(file_names))
    work_file_names = random.sample(file_names, file_count)

    return work_file_names

def read_sample_file(file_name):
    data_merged = wavfile.read(input_directory_name_mono + file_name)[1]
    data_separate = wavfile.read((input_directory_name_voice if config["separation_target"] == "voice" else input_directory_name_music) + file_name)[1]

    return np.array(data_merged), np.array(data_separate)
