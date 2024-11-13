import numpy as np
import cv2

# import packages

# image preprocessing

# edge detection 

# region of interest selection 

# detect lines with Hough Transform 

# draw the lines & combine with original image 
def draw_lines(image, lines, color = [255, 0, 0], thickness = 2):

    # make a copy of the original image to avoid modifying it directly
    image = np.copy(image)

    # loop through each line segment in the list of lines (input parameter)
    for line in lines:
        for x1,y1,x2,y2 in line:
            # draw line using specified color & thickness
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)
    # return new image
    return image

# process image & final return 