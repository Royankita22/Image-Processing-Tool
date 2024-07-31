#quardrant shuffle

import random
import cv2
import numpy as np
img = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

image_height = img.shape[0]
image_width = img.shape[1]

image_height_mid = image_height // 2
image_width_mid = image_width // 2

quadrant = []

quadrant.append( img[ 0:image_height_mid, 0:image_width_mid] )
quadrant.append( img[ 0:image_height_mid, image_width_mid:image_width] )
quadrant.append( img[ image_height_mid:image_height, 0:image_width_mid] )
quadrant.append( img[ image_height_mid:image_height, image_width_mid:image_width] )

random.shuffle(quadrant)

upper_quadrant = np.concatenate((quadrant[0], quadrant[2]), axis = 1 )
lower_quadrant = np.concatenate((quadrant[1], quadrant[3]), axis = 1 )
full_quadrant = np.concatenate((upper_quadrant, lower_quadrant), axis = 0 )

# Display  the blue channel image
cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/shuffel.jpg",full_quadrant )
