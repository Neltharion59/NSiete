import os
import numpy as np
import tensorflow as tf
import scipy.io.wavfile as wavfile
from runpy import run_path
from model import ConvolutionalNeuralNetwork
from tensorflow import keras

# tf.logging.set_verbosity(tf.logging.ERROR)

# Get absolute location of this file
__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
# Load custom dependencies (other .py files of this project)
data_reading = run_path(__location__ + "/../../src/data/data_reading.py")
config = run_path(__location__ + "/../../config.py")
util_tools = run_path(__location__ + "/../util/signal_conversion.py")

# Prepare the dataset and split it into train/test
dataset_names = data_reading["initialize_sample_pool"]()
split_index = int(len(dataset_names) * config["test_ratio"])
test_set_names = dataset_names[:split_index]
train_set_names = dataset_names[split_index:]

# Load the actual data of the dataset
test_set_samples = []
test_set_labels = []
train_set_samples = []
train_set_labels = []

for sample_name in test_set_names:
    sample, sample_label, sample_rate = data_reading["read_sample_file"](sample_name)
    for i in range(sample.shape[1]):
        test_set_samples.append(sample[:,i])
        test_set_labels.append(sample_label[:,i])

    # print(sample)
    # test_set_samples.append(sample)
    # # test_set_samples = np.append(test_set_samples, sample)
    # test_set_labels.append(sample_label)
    # # test_set_labels = np.append(test_set_labels, sample_label)

for sample_name in train_set_names:
    sample, sample_label, sample_rate = data_reading["read_sample_file"](sample_name)
    for i in range(sample.shape[1]):
        train_set_samples.append(sample[:,i])
        train_set_labels.append(sample_label[:,i])
    
    # train_set_samples.append(sample)
    # train_set_samples = np.append(train_set_samples, sample)
    # train_set_labels.append(sample_label)
    # train_set_labels = np.append(train_set_labels, sample_label)

# convert to np.array
train_set_samples = np.array(train_set_samples)
train_set_labels = np.array(train_set_labels)
test_set_labels = np.array(test_set_labels)
test_set_samples = np.array(test_set_samples)

train_set_samples = np.expand_dims(train_set_samples, axis=2)
train_set_labels = np.expand_dims(train_set_labels, axis=2)
test_set_samples = np.expand_dims(test_set_samples, axis=2)
test_set_labels = np.expand_dims(test_set_labels, axis=2)

model = ConvolutionalNeuralNetwork()

callbacks = [ # callbacks for logging
    keras.callbacks.TensorBoard(
        log_dir=os.path.join("logs", "pretrained_non-trainable_bidirectional"),
        histogram_freq=1,
        profile_batch=0)]

print('Compiling...')
model.compile(
    optimizer='adam',
    loss='mean_squared_error',
    metrics=['accuracy'])

print('Fittinf...')
# print(train_set_samples[1])
print(train_set_samples[0].shape)
print(train_set_labels[0].shape)

model.fit(
    x=train_set_samples,
    y=train_set_labels,
    batch_size=1,
    epochs=5,
    callbacks=callbacks,
    validation_data=(test_set_samples, test_set_labels))

file_name = "abjones_2_01.wav"
sample, phase, sample_rate = data_reading["read_sample_file"](file_name)

print(sample.shape)
sample = np.expand_dims(sample, axis=2)

res = model.predict(sample)
print(res.shape)
res = np.squeeze(res, axis=2)
print(res.shape)

out = util_tools["construct_audio"](res, phase)

path_out = __location__ + "/../../data/out/"
wavfile.write(path_out + file_name, sample_rate, out)
