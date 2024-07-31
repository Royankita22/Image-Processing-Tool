#13-histogram equilazation

import cv2
import numpy as np

image=cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

histogram = np.zeros(256)

for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        histogram[image[i][j]] = histogram[image[i][j]] + 1

cummulative_histogram = np.cumsum(histogram)
normalized_histogram = cummulative_histogram / cummulative_histogram[255]
equalized_histogram = np.ceil(normalized_histogram * 255)

for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        image[i][j] = equalized_histogram[image[i][j]]

# Display the result
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/histogram_image.jpg",image)