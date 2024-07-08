
# load calibration.pkl from ./camera_calib_pkl

import pickle
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in the saved objpoints and imgpoints
dist_pickle = pickle.load( open( "./camera_calib_pkl/calibration.pkl", "rb" ) )

print(dist_pickle)
