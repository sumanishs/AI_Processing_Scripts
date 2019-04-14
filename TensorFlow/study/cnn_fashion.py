#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
import sys

label_dict = {
 0: 'T-shirt/top',
 1: 'Trouser',
 2: 'Pullover',
 3: 'Dress',
 4: 'Coat',
 5: 'Sandal',
 6: 'Shirt',
 7: 'Sneaker',
 8: 'Bag',
 9: 'Ankle boot',
}

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
    print (np.max(data.train.images[0]))
    print (np.min(data.train.images[0]))

    train_X = data.train.images.reshape(-1, 28, 28, 1)
    test_X = data.test.images.reshape(-1, 28, 28, 1)

    train_Y = data.train.labels
    test_Y = data.test.labels

    print (train_X.shape)
    print (test_X.shape)

    print (train_Y.shape)
    print (test_Y.shape)

if __name__ == "__main__":
    main(sys.argv)
