import cv2
import numpy as np

def back(*args):
    pass

cv2.namedWindow("Frame")
cv2.createButton("Back",back,None,cv2.QT_PUSH_BUTTON,1)



cv2.destroyAllWindows()