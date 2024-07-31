#_______Blue Channel Extraction_______
import cv2
import matplotlib.pyplot as plt
import numpy as np

original_image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

# Split the image into its RGB channels
blue_channel = original_image[:, :, 0]

# Create an all-zero array with the same shape as the original image
zeros = np.zeros_like(original_image)

# Merge the blue channel with the zeros array to create a blue channel image
blue_channel_image = cv2.merge([blue_channel, zeros[:, :, 1], zeros[:, :, 2]])

# Display  the blue channel image
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/bluechannel.jpg",blue_channel_image)
