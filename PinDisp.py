import cv2
import numpy as np

def overlay_pinTags( img, tag_img, x, y):

	img =  cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

	overlay_t = cv2.imread(tag_img[1],-1)
	scale_percent = 55

	#calculate the 50 percent of original dimensions
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	y = int(y * scale_percent / 100)
	x = int(x * scale_percent / 100)
	# dsize
	dsize = (width, height)

	# resize image
	img = cv2.resize(img, dsize)

	cv2.putText(img, tag_img[0], (int(width/6), 50 ), cv2.FONT_HERSHEY_PLAIN, 2,(10,0,10),4)

	#img = overlay_transparent(img, overlay_t,68, 211, (200,200))
	img = overlay_transparent(img, overlay_t,x, y, (200,200))

	return img


def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):

	bg_img = background_img.copy()
	
	if overlay_size is not None:
		img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

	# Extract the alpha mask of the RGBA image, convert to RGB 
	b,g,r,a = cv2.split(img_to_overlay_t)
	overlay_color = cv2.merge((b,g,r))
	
	# Apply some simple filtering to remove edge noise
	mask = cv2.medianBlur(a,1)

	h, w, _ = overlay_color.shape
	roi = bg_img[y:y+h, x:x+w]

	# Black-out the area behind the logo in our original ROI
	img1_bg = cv2.bitwise_and(roi.copy(),roi.copy(),mask = cv2.bitwise_not(mask))
	
	# Mask out the logo from the logo image.
	img2_fg = cv2.bitwise_and(overlay_color,overlay_color,mask = mask)

	# Update the original image with our new ROI
	bg_img[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)

	return bg_img
