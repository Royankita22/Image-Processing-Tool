import cv2

def remove_watermark(image_path, output_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding to obtain a binary image
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Inpaint the binary image to remove the watermark
    result = cv2.inpaint(img, thresh, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # Save the image without watermark
    cv2.imwrite(output_path, result)

    return result

# Example input:
input_image_path = "C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg"
output_image_path = "C:/xampp/htdocs/Image Processing Tool/update/watermark_removed.jpg"

# Remove watermark and save the result
watermark_removed_img = remove_watermark(input_image_path, output_image_path)
