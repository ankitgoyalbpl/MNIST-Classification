# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 00:50:30 2016

@author: AnkitGoyal
"""

import numpy as np
from scipy import ndimage as nd

def TranslateImage(originalImage):
    
    shiftSize = 2                                           # TODO: Parametrize
    directionVectors = [[0, 1, 0, 0, 0, 0, 0, 0, 0],        # Up Direction
                        [0, 0, 0, 1, 0, 0, 0, 0, 0],        # Left Direction
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],        # Right Direction
                        [0, 0, 0, 0, 0, 0, 0, 1, 0]]        # Down Direction
                        
    directionVectors += [[shiftSize * shiftValue for shiftValue in shiftVector] for shiftVector in directionVectors]
    
    TranslateFunction = lambda imageMatrix, shiftVector: np.convolve(imageMatrix.flatten(), shiftVector, mode = 'same')

    translateImageSet = [TranslateFunction(originalImage, shiftVector) for shiftVector in directionVectors] 
    return translateImageSet
    

def RotateImage(originalImage):
    
    rotationAngle = [5, 10, 15]                             # TODO: Parametrize
    rotationAngle += [-rotateVal for rotateVal in rotationAngle]
    
    RotateFunction = lambda imageMatrix, rotateAngle: nd.rotate(imageMatrix, rotateAngle, reshape=False, mode='constant')
    
    rotateImageSet = [RotateFunction(originalImage, rotateAngle) for rotateAngle in rotationAngle]
    return rotateImageSet

    

