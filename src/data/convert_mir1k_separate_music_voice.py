#!/usr/bin/env python

import os
import numpy
import scipy.io.wavfile as wavfile

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = "\\".join(__location__.split("\\")[:-2])

input_directory_name = __location__ + "\\data\\MIR-1K\\Wavfile\\"
output_directory_name_music = __location__ + "\\data\\MIR-1K\\Wavfile_music\\"
output_directory_name_voice = __location__ + "\\data\\MIR-1K\\Wavfile_voice\\"
file_names = [file_name for file_name in os.listdir(input_directory_name) if file_name[-4:] is not ".wav"]

i = 1
file_count = len(file_names)
for file_name in file_names:
    print(f'Converting file {i}/{file_count}: {file_name}...')
    i = i + 1

    sample_rate, data = wavfile.read(input_directory_name + file_name)

    music_channel= numpy.array(list(map(lambda x: x[0], data)))
    voice_channel = numpy.array(list(map(lambda x: x[1], data)))
    
    wavfile.write(output_directory_name_music + file_name, sample_rate, music_channel)
    wavfile.write(output_directory_name_voice + file_name, sample_rate, voice_channel)
