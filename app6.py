#MEAN FILTERING

import cv2
import numpy as np

image=cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")


kernel_size = 16

image_filtered = np.array(image)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        window = image[y:y+kernel_size, x:x+kernel_size]
        mean = np.mean(window)
        image_filtered[y, x] = mean

# Display the result
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/filtered.jpg",image_filtered)