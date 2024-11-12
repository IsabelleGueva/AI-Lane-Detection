import numpy as np
import cv2

# import packages

# image preprocessing

# edge detection 

# region of interest selection 

# detect lines with Hough Transform 
def hough_transform(image): 
    rho = 1              #looks at every pixels surrounding it to find lines
    theta = np.pi/180    #finds the pixels within a 1-pixel precision and finds angles within 1-degree precision
    threshold = 10       #Only lines that are greater than threshold will be returned; must be within 1-degree so it can still be considered “straight” line
    minLineLength = 10   #Line segments shorter than that are rejected; in this case, longer than 20 pixels
    maxLineGap = 350     #Maximum allowed gap between points on the same line to link them; necessary for broken lane lines
    return cv2.HoughLinesP(image, rho = rho, theta = theta, threshold = threshold, minLineLength = minLineLength, maxLineGap = maxLineGap)
# draw the lines & combine with original image 

# process image & final return 
