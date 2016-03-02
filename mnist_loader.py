import struct
import numpy as np
from array import array


# reads data sets and returns a list of tuples on the form (image, label), where
# image is an one-dimensional array of pixel values in range [0.0, 1.0] and label is a number
def load_data(data_set):
    if data_set == 'training':
        image_filename = 'data/train-images.idx3-ubyte'
        label_filename = 'data/train-labels.idx1-ubyte'
    elif data_set == 'testing':
        image_filename = 'data/t10k-images.idx3-ubyte'
        label_filename = 'data/t10k-labels.idx1-ubyte'
    else:
        print('Invalid name for data set in loader')

    # _ denotes unused variables
    # read labels
    label_file = open(label_filename, 'rb')
    _, label_amount = struct.unpack('>II', label_file.read(8))
    labels = array('b', label_file.read())
    label_file.close()

    # read images
    image_file = open(image_filename, 'rb')
    _, image_amount, rows, cols = struct.unpack('>IIII', image_file.read(16))
    images = array('B', image_file.read())
    image_file.close()

    # find size of images
    image_size = rows*cols

    # create a list of tuples (image, label) and
    # reduce range from [0, 255] to [0.0, 1.0]
    data = []
    for i in range(image_amount):
        data.append((np.array(images[i*image_size:(i+1)*image_size])/255.0, labels[i]))

    return data
