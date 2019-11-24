import os
from runpy import run_path
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
    sample, sample_label = data_reading["read_sample_file"](sample_name)
    test_set_samples.append(sample)
    test_set_labels.append(sample_label)
for sample_name in train_set_names:
    sample, sample_label = data_reading["read_sample_file"](sample_name)
    train_set_samples.append(sample)
    train_set_labels.append(sample_label)

