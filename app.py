#JPG to GIF

from PIL import Image

# Open the JPG image
image = Image.open("C:/xampp/htdocs/Image Processing Tool/uploads/input.jpg")

# Convert the image to GIF
image.save("C:/xampp/htdocs/Image Processing Tool/update/image.gif", "GIF")
image.save("C:/xampp/htdocs/Image Processing Tool/update/image.bmp", "BMP")
image.save("C:/xampp/htdocs/Image Processing Tool/update/image.png", "PNG")
image.save("C:/xampp/htdocs/Image Processing Tool/update/image.jpeg", "JPEG")
