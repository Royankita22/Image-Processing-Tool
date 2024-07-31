#morphological image processing

import cv2
import numpy as np

def custom_erosion(image, kernel):
    """
    Perform erosion operation on the input image using the specified kernel.

    Parameters:
        image: Input image (grayscale).
        kernel: Structuring element/kernel for erosion.

    Returns:
        eroded_image: Resulting image after erosion.
    """
    eroded_image = cv2.erode(image, kernel, iterations=1)
    return eroded_image

def custom_dilation(image, kernel):
    """
    Perform dilation operation on the input image using the specified kernel.

    Parameters:
        image: Input image (grayscale).
        kernel: Structuring element/kernel for dilation.

    Returns:
        dilated_image: Resulting image after dilation.
    """
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    return dilated_image

# Read the input image
image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element/kernel
kernel = np.ones((5,5), np.uint8)

# Perform erosion
eroded_image = custom_erosion(image, kernel)

# Perform dilation
dilated_image = custom_dilation(image, kernel)

# Display the original, eroded, and dilated images


# Display  the blue channel image
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/eroded.jpg",eroded_image)

cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/dilated.jpg",dilated_image)

