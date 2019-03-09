#!/usr/bin/python2.7
import os
import numpy as np
os.environ["GLOG_minloglevel"] = "1"
import caffe

label_map = {}
label_map[0] = "airplane"
label_map[1] = "automobile"
label_map[2] = "bird"
label_map[3] = "cat"
label_map[4] = "deer"
label_map[5] = "dog"
label_map[6] = "frog"
label_map[7] = "horse"
label_map[8] = "ship"
label_map[9] = "truck"

CAFFE_PATH = "/home/sumanish/AI_CNN_FPGA/caffe/"
MEAN_PATH = CAFFE_PATH + "examples/cifar10/mean.binaryproto"
PROTOTXT = CAFFE_PATH + "examples/cifar10/cifar10_full.prototxt"
WEIGHT = CAFFE_PATH + "examples/cifar10/cifar10_full_iter_10000.caffemodel"
INPUT_IMG = "/home/sumanish/AI_CNN_FPGA/cifar-10/data_batch_1/bird_2.png" 

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( MEAN_PATH , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )

net = caffe.Classifier(PROTOTXT, WEIGHT, image_dims=(32, 32), mean=arr[0], raw_scale=255 )
out = net.predict( [ caffe.io.load_image(INPUT_IMG) ])
print out
print out.shape
for s in range(out.shape[1]):
    print out[0][s]
print "Prediction:", out[0].argmax(), ":",  label_map[out[0].argmax()]

