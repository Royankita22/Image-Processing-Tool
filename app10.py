#_______Green Channel Extraction_______
import cv2
import matplotlib.pyplot as plt
import numpy as np

original_image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")


# Split the image into its RGB channels
green_channel = original_image[:, :, 1]  # Green channel is at index 1

# Create an all-zero array with the same shape as the original image
zeros = np.zeros_like(original_image)

# Merge the green channel with the zeros array to create a green channel image
green_channel_image = cv2.merge([zeros[:, :, 0], green_channel, zeros[:, :, 2]])


# Display  the green channel image
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/greenchannel.jpg",green_channel_image)
