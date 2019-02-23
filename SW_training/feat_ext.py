#!/usr/bin/python2.7
import os
import struct
import sys
import numpy as np
import argparse
import cv2
os.environ["GLOG_minloglevel"] = "1"
import caffe
import qmn as q

def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--infile', help='Input file', required=True)
	parser.add_argument('-m','--netmodel', help='Net model prototxt', required=True)
	parser.add_argument('-w','--weights', help='Weight file', required=True)
	parser.add_argument('--mat', help="If matrix format output", action="store_true")
	args = parser.parse_args()
	print "Input file:", args.infile
	print "Net model:", args.netmodel
	print "Weights file:", args.weights
	#print img
	caffe.set_mode_cpu()
	net = caffe.Classifier(args.netmodel,args.weights,caffe.TEST)
	img = cv2.imread(args.infile, -1)
	if img.shape != [28,28]:
	    img2 = cv2.resize(img,(28,28))
	    img = img2.reshape(28,28,-1);
	else:
	    img = img.reshape(28,28,-1);
	img = img/256.0
	out = net.forward_all(data=np.asarray([img.transpose(2,0,1)]))
	pred = out.values()[0]
	for s in pred[0]:
		print "%.10f" % s
	print "Prediction:", pred.argmax()

	print_3d_feat(net, "conv1")	
	print_3d_feat(net, "pool1")	
	print_3d_feat(net, "conv2")
	print_3d_feat(net, "pool2")
	print_1d_feat(net, "ip1")
	print_1d_feat(net, "ip2")
	print_1d_feat(net, "prob")

	#print "conv1"
	#print net.blobs["conv1"].data[0].shape
	#print net.blobs["conv1"].data[0]

	#print "conv2"
	#print net.blobs["conv2"].data[0].shape
	#print net.blobs["conv2"].data[0]

	#print "ip1"
	#print net.blobs["ip1"].data[0].shape
	#print net.blobs["ip1"].data[0]

	#print "ip2"
	#print net.blobs["ip2"].data[0].shape
	#print net.blobs["ip2"].data[0]
	#
	#print "prob"
	#print net.blobs["prob"].data[0].shape
	#print net.blobs["prob"].data[0]

def print_3d_feat(net, layer):
	print "Printing:", layer
	data = net.blobs[layer].data[0]
	print "Shape:", data.shape 
	no = data.shape[0]
	row = data.shape[1]
	col = data.shape[2]
	filename = "txtdata/" + layer + ".txt"
	qmnfile = "txtdata/" + layer + ".qmn"
	tf = open(filename, 'w')
	qmntf = open(qmnfile, 'w')
	for n in range(no):
		for h in range(row):
			for w in range(col):
				tf.write("%.10f\n" % data[n][h][w])
				t = data[n][h][w]
				qmn = q.toQmn(t, 1, 15)
				if t < 0:
					bin = q.twosComplementBin(qmn)
				else:
					bin = q.to16BitBin(qmn)
				bhex = q.bin2hex(bin)
				qmntf.write(bhex)				
				qmntf.write("\n")				
			tf.write("\n")
		tf.write("\n")	
	tf.close()

def print_1d_feat(net, layer):
	print "Printing:", layer
	data = net.blobs[layer].data[0]
	print "Shape:", data.shape 
	no = data.shape[0]
	filename = "txtdata/" + layer + ".txt"
	tf = open(filename, 'w')
	for n in range(no):
		tf.write("%.10f\n" % data[n])
	tf.write("\n")	
	tf.close()
	
	
if __name__ == "__main__":
    main(sys.argv)

