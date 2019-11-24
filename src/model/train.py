import os
import numpy as np
import tensorflow as tf
from runpy import run_path
from model import RecurrentNeuralNetwork
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
    test_set_samples = test_set_samples + sample
    test_set_labels = test_set_labels + sample_label

for sample_name in train_set_names:
    sample, sample_label, sample_rate = data_reading["read_sample_file"](sample_name)
    train_set_samples = train_set_samples + sample
    train_set_labels = train_set_labels + sample_label

# convert to np.array
#train_set_samples = np.array(train_set_samples)
# train_set_labels = np.array(train_set_labels)
# test_set_labels = np.array(test_set_labels)
# test_set_samples = np.array(test_set_samples)

# train_set_labels = np.array([np.array(x) for x in train_set_labels])
# test_set_labels = np.array([np.array(x) for x in test_set_labels])

model = RecurrentNeuralNetwork()

callbacks = [ # callbacks for logging
    keras.callbacks.TensorBoard(
        log_dir=os.path.join("logs", "pretrained_non-trainable_bidirectional"),
        histogram_freq=1,
        profile_batch=0)]

model.compile(
    optimizer='adam',
    loss='mean_squared_error',
    metrics=['accuracy'])

# print(test_set_samples)
# print(test_set_labels)

model.fit(
    x=tf.cast(train_set_samples, tf.float64),
    y=tf.cast(train_set_labels, tf.float64),
    batch_size=10,
    epochs=1,
    # callbacks=callbacks,
    validation_data=(tf.cast(test_set_samples, tf.float64), tf.cast(test_set_labels, tf.float64)),
    steps_per_epoch=10)
