#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:35:22 2018

@author: srikanthnarayanan

Usage: python data_conversion_tf_api.py -real --output_path output_file_name.rec
Usage: python data_conversion_tf_api.py -sim --output_path output_file_name.rec
"""

import tensorflow as tf
import yaml
import os
from utilities import dataset_util

flags = tf.app.flags
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS

LABELS = {
        "Green" : 1,
        "Red"   : 2,
        "Yellow": 3,
        "off"   : 4}


def main(_):



