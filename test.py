import sys
import os
import cv2
import easygui
import numpy as np
import imageio


# Reading the image
ImagePath = easygui.fileopenbox()
img = cv2.imread(ImagePath)
if img is None:
    print(" Can not find any image . Choose appropriate file ")
    sys.exit()


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.medianBlur(img_grey, 3)

edges = cv2.adaptiveThreshold(
    img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2 . THRESH_BINARY, 3, 3)


img_bb = cv2.bilateralFilter(img_blur, 15, 75, 75)

kernel = np.ones((1, 1), np . uint8)
img_erode = cv2.erode(img_bb, kernel, iterations=3)
img_dilate = cv2.dilate(img_erode, kernel, iterations=3)

img_style = cv2.stylization(img, sigma_s=150, sigma_r=0.25)

cv2.imshow('image', img_style)
cv2.waitKey(0)
cv2.destroyAllWindows()