import numpy as np
import cv2
from cv2 import *

def detect_colors():

    # creating an array to be exported
    output = []

    im = cv2.imread('data/face-down.png')
    im = cv2.bilateralFilter(im,9,75,75)
    im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,21)
    hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   # HSV image

    # color specific

    colors = [[np.array([20, 100, 100],np.uint8), np.array([30, 255, 255],np.uint8)],  # yellow
              [np.array([20, 100, 100],np.uint8), np.array([30, 255, 255],np.uint8)],  # orange
              [np.array([20, 100, 100],np.uint8), np.array([30, 255, 255],np.uint8)],  # white
              [np.array([20, 100, 100],np.uint8), np.array([30, 255, 255],np.uint8)],  # red
              [np.array([20, 100, 100],np.uint8), np.array([30, 255, 255],np.uint8)],  # green
              [np.array([20, 100, 100],np.uint8), np.array([30, 255, 255],np.uint8)]]  # blue

    # COLOR_MIN = np.array([20, 100, 100],np.uint8)       # HSV color code lower and upper bounds
    # COLOR_MAX = np.array([30, 255 , 255],np.uint8)       # color yellow

    for i in range(len(colors)):
        COLOR_MIN = colors[i][0]
        COLOR_MAX = colors[i][1]

        frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)     # Thresholding image
        ret,thresh = cv2.threshold(frame_threshed,127,255,0)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            print(x)
            print(y)
            output.append([x, y])
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Show",im)
    cv2.imwrite("detected.jpg", im)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

    print(output)
    return output

def export_array():
    array = detect_colors()
