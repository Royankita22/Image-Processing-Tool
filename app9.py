#_______Red Channel Extraction_______
import cv2
import matplotlib.pyplot as plt
import numpy as np

original_image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

# Split the image into its RGB channels
red_channel = original_image[:, :, 2]  # Accessing the red channel instead of blue

# Create an all-zero array with the same shape as the original image
zeros = np.zeros_like(original_image)

# Merge the red channel with the zeros array to create a red channel image
red_channel_image = cv2.merge([zeros[:, :, 0], zeros[:, :, 1], red_channel])

# Display  the red channel image
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/redchannel.jpg",red_channel_image)