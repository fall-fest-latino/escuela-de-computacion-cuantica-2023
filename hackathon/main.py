import numpy as np
import cv2
import matplotlib.pyplot as plt

imageLocal = cv2.imread("bancos/COVID/1.jpg",cv2.IMREAD_GRAYSCALE)
print(imageLocal.shape)