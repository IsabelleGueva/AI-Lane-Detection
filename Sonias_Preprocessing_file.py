# written by Sonia Pandey
import cv2  # imports the OpenCV library for image and video processing
import os  # imports os to check for file existence

# function to get the file path from the user
def getfilepath():
    # asks user to enter '1' for image or '2' for video
    filetype = input("Enter '1' for uploading an image or '2' for a video: ")
    
    if filetype == '1':
        # asks for the image file path
        filepath = input("Please enter the image file path: ")
        # this part checks if the file exists and has a valid image extension
        # basically checks whether the specified file path (filepath) refers to an existing file
        # os.path is part of python's built-in tools & works with file/folder paths on your computer
        if not os.path.isfile(filepath) or not filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            print("Invalid image file. Please ensure the file exists and has a valid image extension.")
            return getfilepath()  # asks again if the input is invalid
        return filepath  # returns the valid file path
    
    elif filetype == '2':
        # asks for the video file path
        filepath = input("Please enter the video file path: ")
        # this part checks if the file exists and has a valid video extension
        if not os.path.isfile(filepath) or not filepath.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            print("Invalid video file. Please ensure the file exists and has a valid video extension.")
            return getfilepath()  # asks again if the input is invalid
        return filepath  # returns the valid file path
    
    else:
        print("Invalid selection. Please enter '1' or '2'.")
        return getfilepath()  # asks again if the selection number is invalid

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

# main processing function for videos
def videoprocessing(videopath):
    
    # this part creates a VideoCapture object called videocapture
    # this object will handle reading the video frames from the specified path
    # loads the video from the specified path
    videocapture = cv2.VideoCapture(videopath)  # create a VideoCapture object

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

    videocapture.release()  # releases the video capture object

    # prints a message to show processing is done
    print("Video processing is complete, the frames have been altered and are ready for further processing :)")

# implementations
# gets the file path from the user
filepath = getfilepath()

# decides if processing an image or a video based on the file extension
if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
    imageprocessing(filepath)  # processes the image
else:
    videoprocessing(filepath)  # processes the video