#sketch of and image with hue and saturation
import cv2
import numpy as np

def sketch(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_gray_image = 255 - gray_image

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_image = 255 - blurred_image

    # Create the sketch image
    sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    return sketch_image

# Load an image
image = cv2.imread("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

# Get the sketch of the image
sketch_image = sketch(image)

# Convert the sketch image to BGR color space
sketch_bgr = cv2.cvtColor(sketch_image, cv2.COLOR_GRAY2BGR)

# Convert the sketch image to HSV color space
hsv_sketch = cv2.cvtColor(sketch_bgr, cv2.COLOR_BGR2HSV)

# Define the amount by which you want to increase the hue and saturation
hue_shift = 20  # Change this value to adjust the hue shift
saturation_scale = 1.5  # Change this value to adjust the saturation scale

# Shift the hue
hsv_sketch[:, :, 0] = (hsv_sketch[:, :, 0] + hue_shift) % 180

# Scale the saturation
hsv_sketch[:, :, 1] = np.clip(hsv_sketch[:, :, 1] * saturation_scale, 0, 255)

# Convert the image back to BGR color space
modified_sketch_bgr = cv2.cvtColor(hsv_sketch, cv2.COLOR_HSV2BGR)

cv2.imwrite("C:/xampp/htdocs/Image Processing Tool/update/modified_sketch_bgr.jpg",modified_sketch_bgr)