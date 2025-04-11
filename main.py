import largestinteriorrectangle as lir
import cv2
from PIL import Image
import numpy as np

# Capture image from webcam and save
# ret, frame = cv2.VideoCapture(0).read()
# cv2.imwrite("img2.png", frame)

img = Image.open("./tests/test3.png")
img.save("output.jpg", quality=5)  # For JPEG

image = cv2.imread('output.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarize the image (convert to binary format)
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Clean up grain
kernel = np.ones((60,60),np.uint8)
binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Extract the first contour
print("number of contours:", len(contours))
c = max(contours, key = cv2.contourArea)
contour = c

# Convert contour to NumPy array
contour_array = contour[:, 0, :]

# Convert the binary image to a boolean array
grid = (binary_image == 255)

# Call largestinteriorrectangle function
largest_rectangle = lir.lir(grid, contour_array)

image_with_contours = image.copy()
image_with_contours = cv2.drawContours(image_with_contours, contour, -1, (0, 255, 0), 3)
cv2.rectangle(image_with_contours, lir.pt1(largest_rectangle), lir.pt2(largest_rectangle), (255, 0, 0), 2)

top_left = lir.pt1(largest_rectangle)
bottom_right = lir.pt2(largest_rectangle)

width = bottom_right[0] - top_left[0] + 1
height = bottom_right[1] - top_left[1] + 1

area = width * height
print(area)  

cv2.imshow("",image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

