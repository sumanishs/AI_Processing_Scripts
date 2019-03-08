#!/local/workspace/tools/anaconda2/bin/python2.7
import os
import struct
import sys
import numpy as np
import argparse
import cv2
os.environ["GLOG_minloglevel"] = "1"
import caffe


def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--infile', help='Input file', required=True)
	parser.add_argument('-m','--netmodel', help='Net model prototxt', required=True)
	parser.add_argument('-w','--weights', help='Weight file', required=True)
	args = parser.parse_args()
	print "Input file:", args.infile
	print "Net model:", args.netmodel
	print "Weights file:", args.weights
	#print img
	caffe.set_mode_cpu()
	#net = caffe.Net(args.netmodel,args.weights,caffe.TEST);
	net = caffe.Classifier(args.netmodel,args.weights,caffe.TEST)
	caffe.set_mode_cpu()
	img = cv2.imread(args.infile, -1)
	if img.shape != [28,28]:
	    img2 = cv2.resize(img,(28,28))
	    img = img2.reshape(28,28,-1);
	else:
	    img = img.reshape(28,28,-1);
	img = img/255.0
	out = net.forward_all(data=np.asarray([img.transpose(2,0,1)]))
	pred = out.values()[0]
	for s in pred[0]:
		print "%.10f" % s
	print "Prediction:", pred.argmax()

if __name__ == "__main__":
    main(sys.argv)

