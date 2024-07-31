#flipping

import cv2
import numpy as np

image=cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")
shape = image.shape
height=shape[0]
width=shape[1]
ot_array2=np.zeros((height,width,3), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        ot_array2[i][j]=image[height-i-1][width-j-1]
# Display the result
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/flipped.jpg",ot_array2)