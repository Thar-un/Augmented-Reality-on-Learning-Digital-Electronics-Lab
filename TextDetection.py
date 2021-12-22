import cv2
import pytesseract
import tkinter as tk

def txtDetect(txt):

	img = cv2.imread(txt)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 199,7)
	blur = cv2.medianBlur(thresh1, 3)
	thresh1 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 199, 11)
	#cv2.imshow("Threshold_img",thresh1)
	#cv2.waitKey(0)
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))

	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
	cv2.imshow("Dilated_img",dilation)
	cv2.waitKey(0)
	file = open("recognized.txt", "w+")
	file.write("")
	file.close()

	file = open("recognized.txt", "a")

	text = pytesseract.image_to_string(dilation)
	file.write(text)
	file.write("\n")
	file.close
	return [img, thresh1]

def gateNumber():

	file = open("recognized.txt", "r")
	for i in file:
			word = i.strip()
			if( word == "SN74LS32N"):
				return "OR"
			if( word == "SN74LSO8N"):
				return ["AND - IC 7408","/home/qubercomm/Project/ARDE/ANDPINS.png"]
			if( word == "SN74LSO4N"):
				return "NOT"