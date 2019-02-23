#!/usr/bin/python2.7
import os
import struct
import sys
import numpy as np
import argparse
import cv2

def toQmn(number, m, n):
	print "Number to convert:", number
	print "Qm.n","==>", m, ".", n
	prod = int(number * (2 ** n))
	print prod
	return prod

def bin2hex(binstr):
	tmp = "{0:0>4X}".format(int(binstr, 2))
	print "Hex:", tmp
	return tmp

def to16BitBin(number):
	print "Number to convert:", number
	binary = '{0:016b}'.format(number)
	print binary
	return binary

def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--infile', help='Input file', required=True)
	parser.add_argument('-o','--outfile', help='Output file', required=True)
	args = parser.parse_args()
	print "Input file:", args.infile
	print "Output file:", args.outfile
	chunk = 64
	padding = 8
	img = cv2.imread(args.infile, -1)
	if img.shape != [28,28]:
	    img2 = cv2.resize(img,(28,28))
	    img = img2.reshape(28,28,-1);
	else:
	    img = img.reshape(28,28,-1);
	img = img/256.0
	print type(img)
	w = img.shape[0]
	h = img.shape[1]
	tf = open("temp.txt", 'w')
	out = open(args.outfile, 'w')
	#print img
	print "Rows:", h
	print "Cols:", w
	for x in range(h):
		for y in range(w):
			val = img[x][y]
			qnm = toQmn(val, 5, 11)
			bin = to16BitBin(qnm)
			hex = bin2hex(bin)
			tf.write("%f " % img[x][y])
			out.write(hex)
			out.write("\n")
		for i in range(padding/2):
			out.write("0000\t#padding\n")
		tf.write("\n")

	#cv2.imwrite(args.outfile, img)


if __name__ == "__main__":
	main(sys.argv)
