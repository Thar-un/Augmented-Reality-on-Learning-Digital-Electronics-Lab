import cv2 as cv2


disp = 0

def click_event(event, x, y,
	flags, params):

	global a1,a2,a3,a4,a5,a6,a7,a8;
	if event == cv2.EVENT_LBUTTONDOWN:
		if ((x > 250) and (x < 270)):
			if((y > 390) and (y < 410)):
				a1 = 0;
				cv2.putText(img , "0", (15 ,25), font, fontScale, color, thickness, cv2.LINE_AA)
				cv2.putText(img , "0", (250 ,410), font, fontScale, color, thickness, cv2.LINE_AA)
				cv2.imshow(window_name,img)
		if((x > 285) and (x < 305)):
			if ((y > 390 ) and (y < 410)):
				a2 = 1
				cv2.putText(img , "0", (15 ,25), font, fontScale, color, thickness, cv2.LINE_AA)
				cv2.imshow(window_name,img)
		if( a1==0 and a2==1):
				cv2.putText(img , "0", (323 ,410), font, fontScale, color, 2, cv2.LINE_AA)
				cv2.imshow(window_name,img)




# path   
img = cv2.imread('E:\\Final-year Project\\ov-gui\\frame.jpg', 1)
window_name = 'Image'
# Start coordinate, here (5, 5)(column , row)
colour = (0,0,0)#bgr
cv2.rectangle(img, (3, 5), (50 ,30), colour, -2)
cv2.rectangle(img, (70 , 5), (120,30), colour, -2)
cv2.rectangle(img, (3, 45), (50 ,75), colour, -2)
cv2.rectangle(img, (70 , 43), (118,75), colour, -2)
cv2.rectangle(img, (3, 95), (50 ,130), colour, -2)
cv2.rectangle(img, (70 , 94), (120,130), colour, -2)
cv2.rectangle(img, (3, 150), (50 ,190), colour, -2)
cv2.rectangle(img, (70 , 150), (120,190), colour, -2)
#checkboxes-up
cv2.rectangle(img, (250,50), (270,70), (0,0,0), -2)
cv2.rectangle(img, (285,50), (305,70), (0,0,0), -2)
cv2.rectangle(img, (320,50), (340,70), (0,0,0), -2)
cv2.rectangle(img, (355,50), (375,70), (0,0,0), -2)
cv2.rectangle(img, (390,50), (410,70), (0,0,0), -2)
cv2.rectangle(img, (425,50), (445,70), (0,0,0), -2)
cv2.rectangle(img, (470,50), (490,70), (0,0,0), -2)
#checkboxes-down
cv2.rectangle(img, (250,390), (270,410), (0,0,0), -2)
cv2.rectangle(img, (285,390), (305,410), (0,0,0), -2)
cv2.rectangle(img, (320,390), (340,410), (0,0,0), -2)
cv2.rectangle(img, (355,390), (375,410), (0,0,0), -2)
cv2.rectangle(img, (390,390), (410,410), (0,0,0), -2)
cv2.rectangle(img, (425,390), (445,410), (0,0,0), -2)
cv2.rectangle(img, (470,390), (490,410), (0,0,0), -2)


font = cv2.FONT_HERSHEY_SIMPLEX
org = (15, 25)
fontScale = 0.85
color = (255,255,255) #bgr
thickness = 2
#cv2.putText(img , '', org, font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , '', (85, 25), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , '0', (15, 70), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , '1', (83, 73), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , '1', (15, 119), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , '0', (85, 123), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , '1', (15, 175), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , '1', (85, 180), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.waitKey(0)
cv2.destroyAllWindows()

