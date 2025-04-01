import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image_path = "img.jpg"
img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding to classify dark and light regions
_, binary = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

canny_e = cv.Canny(binary, 10, 1000)

# Display results
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2), plt.imshow(binary, cmap='gray')
plt.title('Thresholded Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3), plt.imshow(canny_e, cmap='gray')
plt.title('Canny Filter'), plt.xticks([]), plt.yticks([])

plt.show()