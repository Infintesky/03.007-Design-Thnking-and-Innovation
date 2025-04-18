import cv2
import numpy as np
import largestinteriorrectangle as lir

# Initialize video capture from webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Create the background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Binarize the image (convert to binary format)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Optional: remove noise
    kernel = np.ones((60,60),np.uint8)
    fgmask = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    
    # Find contours (detected objects)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contour = max(contours, key = cv2.contourArea)

    # Convert contour to NumPy array
    contour_array = contour[:, 0, :]

    # Convert the binary image to a boolean array
    grid = (binary_image == 255)

    # Call largestinteriorrectangle function
    largest_rectangle = lir.lir(grid, contour_array)

    top_left = lir.pt1(largest_rectangle)
    bottom_right = lir.pt2(largest_rectangle)

    # Draw bounding boxes and lir around detected objects
    cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
    cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)

    # Calculate width and height of the rectangle
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]

    # Add text to the rectangle
    text = f"W: {width}, H: {height}"
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
    text_x = top_left[0] + (width - text_size[0]) // 2
    text_y = top_left[1] + (height + text_size[1]) // 2

    cv2.imshow('Frame', edges)
    # cv2.imshow('FG Mask', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

