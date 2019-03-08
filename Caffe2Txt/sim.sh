#./caffe2txt.py -w lenet_simple/lenet_simple_iter_10000.caffemodel -p lenet_simple/simple.prototxt -o SIM_Q6_10_IPreordered.txt -b ACT -t SIMULATION --qmn
./caffe2txt.py -w 2CH_50CH_500ip1/lenet_snapshot_2conv_50conv_500ip1_iter_10000.caffemodel -p 2CH_50CH_500ip1/lenet.prototxt -o SIM_Q9_7_2ch_50ch_500ip1_t.txt -b ACT -t SIMULATION --qmn

