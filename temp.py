import cv2
import numpy as np


def calc(img):
    img2 = cv2.resize(img, (600, 600))
    img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, img_thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    for i in range(600):
        for j in range(600):
            if img_thresh[i, j] == 255:
                img_thresh[i, j] = 255
            else:
                img_thresh[i, j] = 150
    yellow = np.sum(img_thresh == 255)
    return str(yellow)
