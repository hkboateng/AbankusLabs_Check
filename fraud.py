# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Created by: Hubert Kyeremateng-Boateng
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("data/10_front.jpg")
#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#img_heatmap = cv.applyColorMap(img, cv.COLORMAP_CIVIDIS)

cv.imshow('Image',img)
