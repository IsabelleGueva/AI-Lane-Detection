import cv2

# function to draw lines on the image 
# note: written in separate file for now, will be integrated into main function after code review
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