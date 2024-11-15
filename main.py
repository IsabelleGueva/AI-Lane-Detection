import numpy as np
import cv2
import os  # imports os to check for file existence

# import packages

# beginning of image preprocessing
# validates file path from the user
def validate_file(filepath):
    # checks if the file exists and has a valid image or video extension
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.mp4', '.avi', '.mov', '.mkv')
    if os.path.isfile(filepath) and filepath.lower().endswith(valid_extensions):
        return True  # file is valid
    else:
        print("Invalid file. Please ensure the file exists and has a valid extension.")
        return False  # file is invalid

# function to convert the frame to grayscale
def grayscaleconversion(frame):
    # converts the frame from BGR to grayscale, luminosity is prioritized by default
    grayscaleframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    return grayscaleframe  # returns the grayscale frame

# function to apply Gaussian blur to the frame
def gaussianblur(grayscaleframe):
    # apply Gaussian blur to the grayscale frame
    blurredframe = cv2.GaussianBlur(grayscaleframe, (5, 5), 0)  # uses a 5x5 kernel for blurring
    return blurredframe  # returns the blurred frame

# main processing function for images
def imageprocessing(imagepath):
    # loads the image from the specified path
    image = cv2.imread(imagepath)  # reads the image file
    # preprocess the image: convert to grayscale
    grayscaleframe = grayscaleconversion(image)  
    # apply Gaussian blur to the grayscale image
    blurredframe = gaussianblur(grayscaleframe)
    # display the results
    cv2.imshow('Original Image', image)  # shows the original image
    cv2.imshow('Grayscale Image', grayscaleframe)  # shows the grayscale image
    cv2.imshow('Gaussian Blurred Image', blurredframe)  # shows the blurred image
    # the argument 0 means it will wait indefinitely until any key is pressed
    # helpful when displaying images so the image window doesn’t open and close immediately
    # gives the user time to view the images before they disappear
    cv2.waitKey(0)  
    # when you create windows using imshow(), OpenCV allocates system resources 
    # to manage those windows so calling this frees up these resources
    cv2.destroyAllWindows()  # closes all OpenCV windows (so no memory leaks)
    # return the processed (blurred) image
    return blurredframe

# main processing function for videos
def videoprocessing(videopath):
    # this part creates a VideoCapture object called videocapture
    # this object will handle reading the video frames from the specified path
    # loads the video from the specified path
    videocapture = cv2.VideoCapture(videopath)  # create a VideoCapture object
    processed_frames = []  # list to store processed frames
    # this loop will continue as long as the VideoCapture object is opened
    # if it’s open, the loop processes each frame in the video
    while videocapture.isOpened():
        # isframevalid is a boolean value that indicates whether the frame was successfully read
        # frame is the actual image data of the current frame 
        isframevalid, frame = videocapture.read()  # retrieves the next frame from the video
        if not isframevalid:
            break  # exits if there are no more frames to read
        # preprocesses the current frame, converts to grayscale
        grayscaleframe = grayscaleconversion(frame)
        # applies Gaussian blur to the grayscale frame
        blurredframe = gaussianblur(grayscaleframe)
        # append the processed frame to the list
        processed_frames.append(blurredframe)
    videocapture.release()  # releases the video capture object
    # return the list of processed frames
    return processed_frames
# end of image preprocessing

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

# *processed outputs from imageprocessing() or videoprocessing()
# will be passed to edge detection and other stages here*
