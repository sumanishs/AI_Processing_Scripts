#!/local/workspace/tools/anaconda2/bin/python2.7
import os
import struct
import sys
import numpy as np
import binascii
import argparse
import math
os.environ["GLOG_minloglevel"] = "1"
import caffe
np.set_printoptions(threshold='nan')

def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-w','--weights', help='caffemodel weights file', required=True)
	parser.add_argument('-p','--prototxt', help='prototxt file', required=True)
	parser.add_argument('-o','--output', help='output file', required=True)
	args = parser.parse_args()
	print "Caffemodel Weights File:", args.weights
	print "Prototxt File:", args.prototxt
	print "Output File:", args.output
	net = caffe.Net(args.prototxt, 1, weights=args.weights)
	print net
	for param_name in net.params.keys():
		print "Param name:", param_name
		weight = net.params[param_name][0].data
		bias = net.params[param_name][1].data
		print "Weight.shape:", weight.shape
		print "Bias.shape:", bias.shape

	print len(net.layers)
	for i in range(len(net.layers)):
		print net.layers[i].type
		for blob in range(0, len(net.layers[i].blobs)):
			print net.layers[i].blobs[blob].data.shape
			print net.layers[i].blobs[blob].data

if __name__ == "__main__":
	main(sys.argv)
