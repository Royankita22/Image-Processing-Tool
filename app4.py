#Image Resizing

import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

# Define the new dimensions
new_height = 300
new_width = 400

# Get the current dimensions
height, width, _ = image.shape

# Create a new blank image with the new dimensions
resized_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

# Calculate scaling factors
scale_x = width / new_width
scale_y = height / new_height

# Iterate through each pixel in the new image
for y in range(new_height):
    for x in range(new_width):
        # Calculate corresponding position in the original image
        px = int(x * scale_x)
        py = int(y * scale_y)

        # Set the pixel value in the resized image
        resized_image[y, x] = image[py, px]

# Display the original and resized images
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/resized_image.jpg",resized_image)