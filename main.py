import numpy as np
import cv2
import os  # imports os to check for file existence
import matplotlib.pyplot as plt
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
#Detect edges in the image
def detect_edges(blurredframe):
    edges=cv2.Canny(blurredframe, 50, 150)  #Detect edges
    return edges  #Detect edges

#Display images
def display_images(original, edges):
    # Check and convert the data type if necessary
    if original.dtype != np.uint8 and original.dtype != np.float32:
        original = original.astype(np.uint8)

    plt.figure(figsize=(12, 6))  # Set the figure size
    plt.subplot(1, 2, 1)  # Create a subplot for the original image
    plt.imshow(original)  # Show the original image
    plt.title("Original Image")  # Title for original image
    plt.axis("off")  # Turn off the axis

    plt.subplot(1, 2, 2)  # Create a subplot for the edge-detected image
    plt.imshow(edges, cmap="gray")  # Show the edge-detected image
    plt.title("Edge Detected Image")  # Title for edge-detected image
    plt.axis("off")  # Turn off the axis

    plt.show()  # Display the images

#Main- running the code
image_path = "solidYellowLeft.and.brokenWhiteRight.png"  # Replace with image file path
img_rgb = imageprocessing(image_path)  # Read and convert the image
edges = detect_edges(img_rgb)  # Perform edge detection

# Display the original and edge-detected images
display_images(img_rgb, edges)

# region of interest selection 
def regionInterest(image):
    #creates a blank mask that is the same size as our image
    mask = np.zeros_like(image)
    #covers the central area of an image
    rows, cols = image.shape[:2]
    #30% across the width of the image & 40% down from the top
    topLeft = int(cols * 0.3), int(cols * 0.7)
    #finds a point 40% across the width of the image & 90% down from the top
    rightBottom = int(rows * 0.4), int(rows * 0.9)
    #draws a rectangle on the mask image, 255 is used for grayscale images
    cv2.rectangle(mask, topLeft, rightBottom, 255, thickness=-1)

    #performs a bitwise operation between the image and the mask and blacks out the rest of the image only keeping the 
    #rectangle part of the image with our specific points from topLeft and rightBottom
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

# detect lines with Hough Transform 
def hough_transform(image): 
    rho = 1              #looks at every pixels surrounding it to find lines
    theta = np.pi/180    #finds the pixels within a 1-pixel precision and finds angles within 1-degree precision
    threshold = 10       #Only lines that are greater than threshold will be returned; must be within 1-degree so it can still be considered “straight” line
    minLineLength = 10   #Line segments shorter than that are rejected; in this case, longer than 20 pixels
    maxLineGap = 350     #Maximum allowed gap between points on the same line to link them; necessary for broken lane lines
    lines = cv2.HoughLinesP(image, rho = rho, theta = theta, threshold = threshold, minLineLength = minLineLength, maxLineGap = maxLineGap)
    return lines if lines is not None else []

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
file_path = "solidYellowLeft.and.brokenWhiteRight.png"
validated_file = validate_file(file_path)
print(validated_file)
processedimage = imageprocessing(file_path)
edges = detect_edges(processedimage)
image = display_images(processedimage, edges)
print("images displayed")
focused_image = regionInterest(processedimage)
print("images focused")
transformed_image = hough_transform(focused_image)
draw_lines(transformed_image, transformed_image, 255, 2)
print("lines drawn")

# *processed outputs from imageprocessing() or videoprocessing()
# will be passed to edge detection and other stages here*
