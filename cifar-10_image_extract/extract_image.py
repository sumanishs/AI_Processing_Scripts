#!/usr/bin/python2.7
import os
import struct
import sys
import numpy as np
import argparse
import cv2

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

idx_map = {}
idx_map [0] = 0
idx_map [1] = 0
idx_map [2] = 0
idx_map [3] = 0
idx_map [4] = 0
idx_map [5] = 0
idx_map [6] = 0
idx_map [7] = 0
idx_map [8] = 0
idx_map [9] = 0

def bytes2int(str):
 return int(str.encode('hex'), 16)

def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--infile', help='Input file', required=True)
	parser.add_argument('-o','--outdir', help='Output folder', required=True)
	parser.add_argument('-t','--type', help='Output type(SIMULATION/BOARD (default SIMULATION))', default='SIMULATION', required=False)
	args = parser.parse_args()
	print "Input file:", args.infile
	print "Output folder:", args.outdir
        if not os.path.exists(args.outdir):
            os.mkdir(args.outdir)
            print("Directory <" + args.outdir + "> created...")
        row = 32
        col = 32
        chunk = 3073   # 1 byte label + 1024 * 3 bytes (R + G + B)
	inf = open(args.infile, "rb")
        while True:
            data = inf.read(chunk)
            if not data:
                break    
            label = bytes2int(data[0])
            next_idx = idx_map[label]
            imgf = label_map[label] + "_" + str(next_idx) + ".png"
            imgf = args.outdir + "/" + imgf
            #print label, ":", imgf
            
            next_idx = next_idx + 1
            idx_map[label] = next_idx
            R = data[1:1025]
            G = data[1025:2049]
            B = data[2049:3073]
            image = np.zeros((32, 32, 3), np.uint8)
            #print len(R)
            #print len(G) 
            #print len(B)
            #btidx = 0
            for ridx in range(row):
                for cidx in range(col):
                    #print ridx*32+cidx
                    r = bytes2int(R[ridx * 32 + cidx]) 
                    g = bytes2int(G[ridx * 32 + cidx]) 
                    b = bytes2int(B[ridx * 32 + cidx]) 
                    image[ridx, cidx, 2] = r        # OpenCV BGR 
                    image[ridx, cidx, 1] = g 
                    image[ridx, cidx, 0] = b 
            cv2.imwrite(imgf, image)

if __name__ == "__main__":
	main(sys.argv)
