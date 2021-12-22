import cv2
import FrameSeg as fs
import TextDetection as td
import ChipDetect as cd
import PinDisp as pd

from tkinter import *

path = '/home/qubercomm/Project/video.mp4'  # path to the video file

for j in range(64):
    txt = "/home/qubercomm/Project/ARDE/Frames/frame"+str(j)+".png" # path to the extracted frames.
    #fs.vidSegment(path)
    img, thresh = td.txtDetect(txt)
    tagPath = td.gateNumber()

    cont = cd.spotxy(img, thresh)
    x = round(cont[1]) - 108
    y = round(cont[0]) + 25

    img  = pd.overlay_pinTags(img, tagPath, int(x), int(y))

    cv2.imshow(tagPath[0], img)
    cv2.waitKey(0)
