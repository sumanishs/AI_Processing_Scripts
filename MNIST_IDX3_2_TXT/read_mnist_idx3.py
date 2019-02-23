#!/usr/bin/python2.7

import os
import struct
import sys
import numpy as np
import binascii
import argparse
import math



def bytes2int(str):
 return int(str.encode('hex'), 16)

def read_label(inf, of): 
	data = inf.read(4)
	i = bytes2int(data)
	if i != 2049:
		print "This is not a label set..."
		quit()
	of.write("Magic number:%d\n" % i)
	data = inf.read(4)
	i = bytes2int(data)
	of.write("Number of items:%d\n" % i)
	while True:
		data = inf.read(1)
		if not data:
			break
		i = bytes2int(data)
		of.write("%d\n" % i)

def read_data(inf, of):
	data = inf.read(4)
	i = bytes2int(data)
	if i != 2051:
		print "This is not an image data set..."
		quit()
	of.write("Magic number:%d\n" % i)
	data = inf.read(4)
	i = bytes2int(data)
	of.write("Number of images:%d\n" % i)
	data = inf.read(4)
	i = bytes2int(data)
	of.write("Number of rows:%d\n" % i)
	data = inf.read(4)
	i = bytes2int(data)
	of.write("Number of columns:%d\n" % i)
	while True:
		data = inf.read(1)
		if not data:
			break
		i = bytes2int(data)
		of.write("%d\n" % i)



def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--infile', help='Input file', required=True)
	parser.add_argument('-o','--output', help='Output file', required=True)
	parser.add_argument('-t','--type', help='Input type (DATA/LABEL)', required=True)
	args = parser.parse_args()
	print "Input file:", args.infile
	print "Output file:", args.output
	of = open(args.output, "wb")
	inf = open(args.infile, "rb")
	if args.type == "DATA":
		read_data(inf, of)
	elif args.type == "LABEL":
		read_label(inf, of)
	else:
		print "Wrong input type!!"
		quit()

	of.close()
	inf.close()

if __name__ == "__main__":
	main(sys.argv)
