# Camera Calibration

This repository contains two Python scripts for camera-calibration: capturing images from camera and performing camera calibration using a set of checkerboard images.

## Step 1: Capture Chessboard Images

The first script captures images from a camera at regular intervals and saves them to disk. Run the script `capture_images.py`.

### Description

- The script iterates through camera indices 0 to 5, attempting to open each camera.
- For each opened camera, it continuously captures frames and saves them by default. Since I was using only a single camera by default, it works for me. However, in case you have multiple cameras conencted, please select the index for the camera you want to calibrate and only use that to capture the images.
- Images are saved to the specified directory (`images` by default) every 5 seconds.

## Step 2: Perform Camera Calibration

This script performs camera calibration based on a set of chessboard images. Run the script `camera_calibration.py`.

### Description

- The script finds chessboard corners in the provided images and calculates object points and image points.
- Using the calculated points, it calibrates the camera and saves the calibration parameters.
- Finally, it undistorts a test image and saves the result.

## Requirements

- Python 3.x
- OpenCV

## More Information

For a detailed explanation of camera calibration and its implementation in this project, as well as insights into calibrating cameras and lidar sensors for sensor fusion, check out [my Medium story](https://medium.com/@shashankag14/lidar-camera-fusion-a-short-guide-34115a3055da).

## Reference

The camera calibration code has been adapted from the official OpenCV documentation. You can find the original documentation [here](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html).
