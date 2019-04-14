#!/usr/bin/python3
import sys
import os
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print (tf.__version__)

def main(argv):
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    checkpoint_path = "training_1/cp.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    #model = create_model()
    print ("Loading model from:", "training_1/my_model.h5")
    model = keras.models.load_model('training_1/my_model.h5')
    model.summary()
    loss, acc = model.evaluate(test_images, test_labels)
    print ("Loss: {:5.2f}%".format(loss * 100))
    print ("Acc: {:5.2f}%".format(acc * 100)) 



if __name__ == "__main__":
    main(sys.argv)
