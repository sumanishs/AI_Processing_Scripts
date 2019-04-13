#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
import sys


def main(argv):
    print ("Main...")
    data = input_data.read_data_sets('fashion', one_hot=True)
    print ("Train (images) shape :{shape}".format(shape = data.train.images.shape))
    print ("Train (labels) shape :{shape}".format(shape = data.train.labels.shape))

    print ("Test (images) shape :{shape}".format(shape = data.test.images.shape))
    print ("Test (labels) shape :{shape}".format(shape = data.test.labels.shape))

    #print ("Test label data: {tstdata}".format(tstdata = data.test.labels.data[0]))
    print (data.test.labels[0])
    print (data.test.images[0])


if __name__ == "__main__":
    main(sys.argv)
