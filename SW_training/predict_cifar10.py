#!/usr/bin/python2.7
import os
import sys
import argparse
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
WEIGHT = CAFFE_PATH + "examples/cifar10/cifar10_full_iter_60000.caffemodel"
INPUT_IMG = "/home/sumanish/AI_CNN_FPGA/cifar-10/data_batch_1/bird_3.png" 

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--infile', help='Input file', required=True)
    parser.add_argument('-p','--prototxt', help='Net model prototxt', required=True)
    parser.add_argument('-w','--weights', help='Weight file', required=True)
    parser.add_argument('-m','--meanfile', help='Mean file', required=True)
    args = parser.parse_args()
    print "Input file:", args.infile
    print "Net model prototxt:", args.prototxt
    print "Weights file:", args.weights
    print "Mean file:", args.meanfile
    caffe.set_mode_cpu()
    blob = caffe.proto.caffe_pb2.BlobProto()
    data = open( args.meanfile , 'rb' ).read()
    blob.ParseFromString(data)
    arr = np.array( caffe.io.blobproto_to_array(blob) )
    
    net = caffe.Classifier(args.prototxt, args.weights, image_dims=(32, 32), mean=arr[0], raw_scale=255 )
    out = net.predict( [ caffe.io.load_image(args.infile) ])
    for s in range(out.shape[1]):
        print "%.10f" % out[0][s]
    print "Prediction:", out[0].argmax(), ":",  label_map[out[0].argmax()]


if __name__ == "__main__":
    main(sys.argv)
