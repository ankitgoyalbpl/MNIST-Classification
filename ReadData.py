# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 00:50:30 2016

@author: AnkitGoyal
"""

import os
import struct
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def ParseMNISTData(dataType = 'training', filePath = './../Data'):
    if dataType is 'training':
        imgFileName = os.path.join(os.path.abspath(filePath), 'train-images.idx3-ubyte')
        lblFileName = os.path.join(os.path.abspath(filePath), 'train-labels.idx1-ubyte')
    elif dataType is 'testing':
        imgFileName = os.path.join(os.path.abspath(filePath), 't10k-images.idx3-ubyte')
        lblFileName = os.path.join(os.path.abspath(filePath), 't10k-labels.idx1-ubyte')
    else:
        raise ValueError, 'DataType must be either "training" or "testing"'

    with open(lblFileName, 'rb') as inFile:
        struct.unpack('>II', inFile.read(8))
        labelData = np.fromfile(inFile, dtype=np.uint8)

    with open(imgFileName, 'rb') as inFile:
        _, _, rowCount, colCount = struct.unpack('>IIII', inFile.read(16))
        imageData = np.fromfile(inFile, dtype=np.uint8).reshape(len(labelData), rowCount, colCount)

    GetData = lambda dataIndex : (labelData[dataIndex], imageData[dataIndex])

    for dataIndex in range(len(labelData)):
        yield GetData(dataIndex)


def DrawNumber(numberImage):
    imgFigure = plt.figure().add_subplot(1, 1, 1)
    imgPlot = imgFigure.imshow(numberImage, cmap=matplotlib.cm.Greys)
    imgPlot.set_interpolation('nearest')
    imgFigure.xaxis.set_ticks_position('top')
    imgFigure.yaxis.set_ticks_position('left')
    plt.show()


for dataItem in ParseMNISTData():
    DrawNumber(dataItem[1])
    break
