"""
Python script to capture images from multiple cameras at regular intervals and save them to disk.

This script iterates through camera indices 0 to 5, attempting to open each camera. 
For each opened camera, it continuously captures frames and displays them. Images are saved to the specified directory ('images' by default) every 5 seconds. 
"""

import cv2
import time
from pathlib import Path

num = 0
save_interval = 5  # Save image every 5 seconds
last_save_time = time.time()

# Specify the path tpo store captured images
directory = "cali_result" # change this to "cali_result" in case test images needs to be captured
Path(directory).mkdir(parents=True, exist_ok=True)

for i in range(6):  # Try indices 0 to 5
    cap = cv2.VideoCapture(i)

    if not cap.isOpened():
        print("Camera not found at index", i)
        continue

    print("Camera found at index", i)

    while cap.isOpened():
        success, img = cap.read()

        if not success:
            print("Failed to read frame")
            break

        cv2.imshow('Img', img)
        current_time = time.time()

        # Save image if save interval has elapsed
        if current_time - last_save_time >= save_interval:
            cv2.imwrite('cali_result/img' + str(num) + '.png', img)
            print("Image saved as 'img" + str(num) + ".png'")
            num += 1
            last_save_time = current_time

        k = cv2.waitKey(1)
        if k == 27:
            break

    cap.release()

cv2.destroyAllWindows()
