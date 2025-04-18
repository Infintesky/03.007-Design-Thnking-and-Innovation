import cv2
import numpy as np
import largestinteriorrectangle as lir

SCALE = 0.04

def find_LargestInteriorRectangle(binary_image, contour):
    contour_array = contour[:, 0, :]
    grid = (binary_image == 255)
    largest_rectangle = lir.lir(grid, contour_array)
    top_left = lir.pt1(largest_rectangle)
    bottom_right = lir.pt2(largest_rectangle)
    return top_left, bottom_right


class VideoProcessor:
    def __init__(self, camera_index=0, width=640, height=480):
        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)

    def process_frame(self, frame):
        kernel = np.ones((60, 60), np.uint8)
        reusability = False

        # Convert to grayscale and apply threshold
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        

        # Background subtraction and morphological filtering
        fgmask = self.bg_subtractor.apply(frame)
        fgmask = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

        # Find contours
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        if not contours:
            return frame

        contour = max(contours, key=cv2.contourArea)

        # Find the largest interior rectangle
        try:
            top_left, bottom_right = find_LargestInteriorRectangle(binary, contour)
            # Draw
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

            # Dimensions
            width_px = bottom_right[0] - top_left[0]
            height_px = bottom_right[1] - top_left[1]
            width_cm = round(width_px * SCALE, 2)
            height_cm = round(height_px * SCALE, 2)

            if (width_cm and height_cm) > 10.0:
                reusability = True
            
            # Add reusability text on the scaled-down image
            text = "Reusable" if reusability else "Not Reusable"
            print("[+] Width:", width_cm, "cm", "Height:", height_cm, "cm", text)

            cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2) if reusability else cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            font_color = (0, 0, 255) if not reusability else (0, 255, 0)
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
            text_x = top_left[0] + (width_px - text_size[0]) // 2
            text_y = top_left[1] + (height_px + text_size[1]) // 2
            cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, font_color, 1, cv2.LINE_AA)


        except Exception as e:
            # print("LIR computation failed:", e)
            return frame

        return frame

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            processed_frame = self.process_frame(frame)
            cv2.imshow('Frame', processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cleanup()

    def cleanup(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    processor = VideoProcessor()
    processor.run()
