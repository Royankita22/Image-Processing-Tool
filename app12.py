#convolution of an image

import numpy as np
import cv2
import matplotlib.pyplot as plt


# Load the image
image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg", cv2.IMREAD_GRAYSCALE)

 #Define the kernel/filter
kernel = np.array([[1, 0, -1],
                  [2, 0, -2],
                  [1, 0, -1]])


# Get the dimensions of the image and kernel
image_height, image_width = image.shape
kernel_height, kernel_width = kernel.shape

# Define the output matrix (convolved image)
convolved_image = np.zeros_like(image)

# Perform convolution
for i in range(image_height - kernel_height + 1):
    for j in range(image_width - kernel_width + 1):
        # Extract the region of interest from the image
        roi = image[i:i+kernel_height, j:j+kernel_width]
        # Perform element-wise multiplication with the kernel
        convolved_pixel = np.sum(roi * kernel)
        # Store the result in the output matrix
        convolved_image[i, j] = convolved_pixel

# Save the convolved image
# Display  the blue channel image
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/convolved.jpg",convolved_image)

