import cv2
import numpy as np


# Function to convert frame to cartoon
def cartoonize_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Convert the frame to color
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    # Combine the color frame with the edges mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


# Open the video file
cap = cv2.VideoCapture('porkFoot.mp4')

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Apply cartoon effect to the frame
    cartoon_frame = cartoonize_frame(frame)

    # Display the cartoonized frame
    cv2.imshow('Cartoon', cartoon_frame)

    # Check if the user pressed 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
