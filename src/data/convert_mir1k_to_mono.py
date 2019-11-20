#!/usr/bin/env python

import os
# https://github.com/jiaaro/pydub#installation
from pydub import AudioSegment

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = "\\".join(__location__.split("\\")[:-2])

input_directory_name = __location__ + "\\data\\MIR-1K\\Wavfile\\"
output_directory_name = __location__ + "\\data\\MIR-1K\\Wavfile_mono\\"
file_names = [file_name for file_name in os.listdir(input_directory_name) if file_name[-4:] is not ".wav"]

i = 1
file_count = len(file_names)
for file_name in file_names:
        print(f'Converting file {i}/{file_count}: {file_name}...')
        i = i +1

        sound = AudioSegment.from_wav(input_directory_name + file_name)
        sound = sound.set_channels(1)
        sound.export(output_directory_name + file_name, format="wav")
