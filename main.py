import largestinteriorrectangle as lir
import cv2
import numpy as np

raw_image = cv2.imread('./tests/test3.png')
image = cv2.resize(raw_image, None, fx = 0.4, fy = 0.4)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarize the image (convert to binary format)
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Clean up grain
kernel = np.ones((60,60),np.uint8)
binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Extract the first contour
print("[+] Number of contours detected:", len(contours))
c = max(contours, key = cv2.contourArea)
contour = c

# Convert contour to NumPy array
contour_array = contour[:, 0, :]

# Convert the binary image to a boolean array
grid = (binary_image == 255)

# Call largestinteriorrectangle function
largest_rectangle = lir.lir(grid, contour_array)

top_left = lir.pt1(largest_rectangle)
bottom_right = lir.pt2(largest_rectangle)

image_with_contours = image.copy()
image_with_contours = cv2.drawContours(image_with_contours, contour, -1, (0, 255, 0), 3)
cv2.rectangle(image_with_contours, top_left, bottom_right, (255, 0, 0), 2)

# Calculate area of pixels
width = bottom_right[0] - top_left[0] + 1
height = bottom_right[1] - top_left[1] + 1

area = width * height

print("[+] Width in pixels:", width)
print("[+] Height in pixels:", height) 
print("[+] Area of rectangle:", area) 
print("[+] Area of contour:", cv2.contourArea(c))

cv2.imshow("",image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

