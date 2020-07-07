from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

# split image into channels B, G and R
channels = cv2.split(image)

# initialize a tuple
colors = ("b", "g", "r")

# setup pyplot figure
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")

for (channel, color) in zip(channels, colors):
    # create the histogram 
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])

plt.show()

cv2.waitKey(0)