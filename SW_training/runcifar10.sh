for i in {1..999}
do
./predict_cifar10.py -i cifar10_data/data_batch_1/cat_${i}.png -p cifar10_caffemodel/cifar10_full.prototxt -w cifar10_caffemodel/cifar10_full_iter_60000.caffemodel -m cifar10_caffemodel/mean.binaryproto
done
