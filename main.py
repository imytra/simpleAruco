# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2 as cv


def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	gray = cv.GaussianBlur(gray, (5, 5), 0)
	edged = cv.Canny(gray, 35, 125)
	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	cnts = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv.contourArea)
	# compute the bounding box of the of the paper region and return it
	return cv.minAreaRect(c)

# Get image (Localy saved jpg)
img = cv.imread("download.jpg")

# Convert image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply a gaussian blur to gray scaled img (gray)
gaus = cv.GaussianBlur(gray, (5, 5), 0)

# Draw edges from gray scaled img (gray)
edged = cv.Canny(gray, 35, 125)

cnts = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key = cv.contourArea)

ret = cv.minAreaRect(c)


cv.imshow("raw", img)
cv.imshow("gray", gray)
cv.imshow("gaussian blur", gaus)
cv.imshow("image edges", edged)
print(cnts)

k = cv.waitKey(0) # Wait for a keystroke in the window