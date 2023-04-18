""" This code detects the objects based on color"""

# Import the necessary libraries
import cv2
import numpy as np

# Create a dummy function. It is required for cv2.createTrackbar()
def do_nothing(x):
    pass

# Create a named window to create trackbars
cv2.namedWindow("Tracking")

# Create trackbars to adjust the cut-off color range
cv2.createTrackbar("Lower Hue", "Tracking", 0, 255, do_nothing)
cv2.createTrackbar("Lower Sat", "Tracking", 0, 255, do_nothing)
cv2.createTrackbar("Lower Val", "Tracking", 0, 255, do_nothing)
cv2.createTrackbar("Upper Hue", "Tracking", 255, 255, do_nothing)
cv2.createTrackbar("Upper Sat", "Tracking", 255, 255, do_nothing)
cv2.createTrackbar("Upper Val", "Tracking", 255, 255, do_nothing)

while True:
    # Read the image
    img = cv2.imread('Images/coloredballs.jpg')
    
    # Resize the image
    img = cv2.resize(img, None, fx=0.24,fy=0.24)
    
    # Convert BGR image to HSV color
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Get the track bars to get lower & upper 
    # HSV (actually BGR) color values.
    l_h = cv2.getTrackbarPos("Lower Hue", "Tracking")
    l_s = cv2.getTrackbarPos("Lower Sat", "Tracking")
    l_v = cv2.getTrackbarPos("Lower Val", "Tracking")
    u_h = cv2.getTrackbarPos("Upper Hue", "Tracking")
    u_s = cv2.getTrackbarPos("Upper Sat", "Tracking")
    u_v = cv2.getTrackbarPos("Upper Val", "Tracking")
    
    # Convert the HSV (BGR) color values to array
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    
    # Create the mask 
    # The function gives the values within the
    # lower_bound & upper_bound range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Perform the bitwise AND of image with itself
    # & using the mask of cut-off colors
    result = cv2.bitwise_and(img, img, mask=mask)
    
    # Display all the images
    cv2.imshow("Input Image", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Wait for 1 millisecond
    key = cv2.waitKey(1)
    
    # When "Escape" key is pressed, save the images 
    # & close all windows
    if key == 27:
        # Save the images
        cv2.imwrite("Mask.jpg",mask)
        cv2.imwrite("Result.jpg",result)
        cv2.imwrite("resize.jpg",img)
        break
    
# Close all windows
cv2.destroyAllWindows()
