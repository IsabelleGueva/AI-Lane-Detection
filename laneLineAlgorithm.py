"""Hi everyone! Use examples, references, and any resources you need to code a 
function that covers the topic you chose on the 10/19 Meeting Minutes. Use lots of 
comments to explain your code. If you need any help, make note of it and we can brainstorm next meeting. 
Don't merge your branches until after our code review.
Good luck everyone!"""
import numpy as np
import cv2

def hough_transform(image): 
    rho = 1              #looks at every pixels surrounding it to find lines
    theta = np.pi/180    #finds the pixels within a 1-pixel precision and finds angles within 1-degree precision
    threshold = 10       #Only lines that are greater than threshold will be returned; must be within 1-degree so it can still be considered “straight” line
    minLineLength = 10   #Line segments shorter than that are rejected; in this case, longer than 20 pixels
    maxLineGap = 350     #Maximum allowed gap between points on the same line to link them; necessary for broken lane lines
    return cv2.HoughLinesP(image, rho = rho, theta = theta, threshold = threshold, minLineLength = minLineLength, maxLineGap = maxLineGap)