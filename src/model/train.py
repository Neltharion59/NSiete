import os
import numpy as np
import tensorflow as tf
import scipy.io.wavfile as wavfile
from runpy import run_path
from model import ConvolutionalNeuralNetwork
from tensorflow import keras
from datetime import datetime

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
# model.load_weights('training_07_12_2019_13_54_32/cp-{epoch:04d}.ckpt'.format(epoch=2))

now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
checkpoint_path = "training_" + dt_string + "/cp-{epoch:04d}.ckpt"

file_name = "marisa_hq.wav"
sample, phase, sample_rate = data_reading["read_sample_file_val"](file_name)
predict_samples = []

for i in range(sample.shape[1]):
    predict_samples.append(sample[:,i])

predict_samples = np.array(predict_samples)
predict_samples = np.expand_dims(predict_samples, axis=2)
print(predict_samples.shape)
print(train_set_samples.shape)

callbacks = [ # callbacks for logging
    keras.callbacks.TensorBoard(
        log_dir=os.path.join("logs", "pretrained_non-trainable_bidirectional"),
        histogram_freq=1,
        profile_batch=0),
    keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path, 
        verbose=1, 
        save_weights_only=True,
        period=2)
    ]

print('Compiling...')
model.compile(
    optimizer='adam',
    loss='mean_squared_error',
    metrics=['accuracy'])

print('Fitting...')
# print(train_set_samples[1])
print(train_set_samples[0].shape)
print(train_set_labels[0].shape)

model.fit(
    x=train_set_samples,
    y=train_set_labels,
    batch_size=1,
    epochs=12,
    callbacks=callbacks,
    validation_data=(test_set_samples, test_set_labels))

# file_name = "abjones_2_01.wav"
# sample, phase, sample_rate = data_reading["read_sample_file_val"](file_name)

# print(sample.shape)
# sample = np.expand_dims(sample, axis=2)

print('Predicting...')

res = model.predict(predict_samples)
res = np.swapaxes(res, 0, 1)
print(res.shape)
res = np.median(res, axis=2)
print(res.shape)
# res = np.squeeze(res, axis=2)
# print(res.shape)

out = util_tools["construct_audio"](res, phase)

path_out = __location__ + "/../../data/out/"
wavfile.write(path_out + file_name + "_" + dt_string + ".wav", sample_rate, out)

