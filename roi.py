import numpy as np
import cv2
import matplotlib.pyplot as plt

def regionInterest(image):
  #creates a blank mask that is the same size as our image
  mask = np.zeros_like(image)
  
  #covers the central area of an image
  rows, cols = image.shape[:2]
  
  #30% across the width of the image & 40% down from the top
  topLeft = int(cols * 0.3), int(cols * 0.7)
  
  #finds a point 40% across the width of the image & 90% down from the top
  rightBottom = int(rows * 0.4), int(rows * 0.9)
  
  #i just drew a random rectangle on my image and found the corner points to test the output
  #topLeft = 136, 204
  #rightBottom = 336, 265
  
  #draws a rectangle on the mask image, 255 is used for grayscale images
  cv2.rectangle(mask, topLeft, rightBottom, 255, thickness=-1)
  
  #performs a bitwise operation between the image and the mask and blacks out the rest of the image only keeping the 
  #rectangle part of the image with our specific points from topLeft and rightBottom
  masked_image = cv2.bitwise_and(image, mask)

return masked_image
