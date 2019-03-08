#./caffe2txt.py -w lenet_simple/lenet_simple_iter_10000.caffemodel -p lenet_simple/simple.prototxt -o SIM_Q6_10_IPreordered.txt -b ACT -t SIMULATION --qmn
./caffe2txt.py -w 20CH_50CH_500ip1/lenet_snapshot_20conv_50conv_500ip1_iter_10000.caffemodel -p 20CH_50CH_500ip1/lenet.prototxt -o BOARD_Q9_7_20ch_50ch_500ip1.txt -b ACT -t BOARD --qmn

