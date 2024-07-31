#Edge Detection

import cv2
import numpy as np

def custom_edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Sobel operator for gradient calculation
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)

    # Compute the gradient magnitude
    gradient_magnitude = np.sqrt(sobelx*2 + sobely*2)

    # Normalize the gradient magnitude to the range [0, 255]
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient_magnitude

# Load the image
image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

# Perform edge detection using the custom function
edges = custom_edge_detection(image)

# Display the original and edge-detected images
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/edegs.jpg",edges)