# Color-based Object Detection
This project uses the OpenCV Python library to detect the objects based on colors. A trackbar is provided to select the desired color form the input image.

# Important functions used
1. **cv2.inRange()**

The [cv2.inRange()](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981) function is used to detect colors in an image. We provide the lower range and upper range of the desired color. This function returns an binary image where the value is 0 for the colors that are not in the given range. And 255 for the colors in the range.

2. **cv2.bitwise_and()**

The [cv2.bitwise_and()](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14) function is used to perform bitwise AND operation with the mask generated from **cv2.inRange()** function.
