#!/usr/bin/env python

# What kind of info we want to separate. Options: "music", "voice".
# E.g. "music" means we will filter out voice and keep the music.
separation_target = "voice"
# How many samples to work with during this run
sample_count = 30
# Percentage of how big part of dataset should be the testing set (the rest is training set)
# E.g. "0.3" means that 30% will be test set, 70% will be train set
test_ratio = 0.2
