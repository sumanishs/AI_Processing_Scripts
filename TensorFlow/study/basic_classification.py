#!/usr/bin/python3
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print (tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


#print (type(train_images))
#print (train_images.shape)
#print (train_images)
#
#print (type(train_labels))
#print (train_labels.shape)
#print (train_labels)
#
#print (class_names)

#plt.figure()
#plt.imshow(train_images[0])
#plt.colorbar()
#plt.grid(False)
#plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

#plt.figure(figsize=(10, 10))
#for i in range(25):
#    plt.subplot(5, 5, i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(True)
#    plt.imshow(train_images[i], cmap=plt.cm.binary)
#    plt.xlabel(class_names[train_labels[i]])
#plt.show()
#
#plt.figure(figsize=(10, 10))
#for i in range(25):
#    plt.subplot(5, 5, i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(True)
#    plt.imshow(test_images[i], cmap=plt.cm.binary)
#    plt.xlabel(class_names[test_labels[i]])
#plt.show()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
model.summary()
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print ('Test loss:', test_loss)
print ('Test acc:', test_acc)

prediction = model.predict(test_images)
print (prediction[1])
print (class_names[np.argmax(prediction[1])])

img = test_images[1]
print (img.shape)
img = (np.expand_dims(img, 0))
print (img.shape)

pred = model.predict(img)
print (class_names[np.argmax(pred)])


plt.figure()
plt.imshow(test_images[1])
plt.grid(False)
plt.show()
