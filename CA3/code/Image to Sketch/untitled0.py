# -*- coding: utf-8 -*-
"""
Created on Tue May 14 01:35:01 2024

@author: Mhsa
"""
#https://github.com/codewithpom/Get-Sketch-from-image
# Python program to Convert Image into sketch
 
 
import cv2
# read the image file
image = cv2.imread('input2-300x295.jpg')

# add gray effect
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# invert the image
inverted_image = cv2.bitwise_not(gray_image)

# blur the image
blur_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# create inverted blur image
inverted_blur = cv2.bitwise_not(blur_image)

# divide the gray image and inverted blur

sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

# save the file to the folder

cv2.imwrite("sketch.png", sketch)
