import cv2


disp = 0
font = cv2.FONT_HERSHEY_SIMPLEX
org = (15, 25)
fontScale = 0.85
color = (255,255,255) #bgr
thickness = 2


def click_event(event, x, y,
    flags, params):

    global a1,a2,a3,a4,a5,a6,a7,a8;
    if event == cv2.EVENT_LBUTTONDOWN:
        if ((x > 275) and (x < 295)):
            if((y > 580) and (y < 605)):
                a1 = 0;
                cv2.putText(img , "0", (301 ,538), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 330) and (x < 345)):
            if ((y > 580 ) and (y < 605)):
                a1 = 1;
                cv2.putText(img , "1", (301 ,538), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 355) and (x < 380)):
            if((y > 580) and (y < 609)):
                a2 = 0;
                cv2.putText(img , "0", (337 ,538), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 395) and (x < 430)):
            if ((y > 580 ) and (y < 608)):
                a2 = 1;
                cv2.putText(img , "1", (337 ,538), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 376) and (x < 491)):
            if((y > 670) and (y < 715)):
                    if ((a1 == 0)):
                        #print("1",a1," ",a2)
                        cv2.putText(img , "1", (375 ,540), font, fontScale, color, 2, cv2.LINE_AA)
                        #cv2.putText(img , "1", (378 ,300), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                    if a1 == 1:
                        cv2.putText(img , "0", (375 ,540), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.imshow(window_name,img)

# path   
imag = cv2.imread('E:\\Final-year Project\\ov-gui\\frame.jpg', 1)
window_name = 'Image'
img = cv2.resize(imag, (990, 800))                    # Resize image

# Start coordinate, here (5, 5)(column , row)
colour = (0,0,0)#bgr
#checkboxes-up
x = 300
y = 220
cv2.rectangle(img, (x,y), (x+20,y+20), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,y), (x+55,y+20), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,y), (x+90,y+20), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,y), (x+125,y+20), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,y), (x+160,y+20), (0,0,0), -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,y), (x+195,y+20), (0,0,0), -2)#(425,50), (445,70)
cv2.rectangle(img, (x+220,y), (x+240,y+20), (0,0,0), -2)#(470,50), (490,70)
#checkboxes-down
x1 = 520
y1 = 540
cv2.rectangle(img, (x,x1), (x+20,y1), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,x1), (x+55,y1), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,x1), (x+90,y1), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,x1), (x+125,y1), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,x1), (x+160,y1), (0,0,0), -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,x1), (x+195,y1), (0,0,0), -2)#(425,50), (445,70)
cv2.rectangle(img, (x+220,x1), (x+240,y1), (0,0,0), -2)#(470,50), (490,70)
#output-box
cv2.rectangle(img, (x+75,x1+150), (x+190,y1+175), (0,0,0), -2)#(375 , 670),(320 , 715)
cv2.putText(img , "Show Output", (380 ,700), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)


cv2.line(img, (310 , 537), (282 , 583), colour, 2)
cv2.line(img, (310 , 537), (336 , 583), colour, 2)
#cv2.line(img, (346 , 535), (361 , 584), colour, 2)
#cv2.line(img, (346 , 535), (405 , 583), colour, 2)

cv2.rectangle(img, (275,580), (293,605), (0,0,0), -2)
cv2.rectangle(img, (327,580), (346,605), (0,0,0), -2)
cv2.putText(img , "0", (275 ,600), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (328 ,600), font, fontScale, color, thickness, cv2.LINE_AA)

#cv2.rectangle(img, (355 , 581), (377 , 606), (0,0,0), -2)
#cv2.rectangle(img, (396 , 581), (426 , 606), (0,0,0), -2)
#cv2.putText(img , "0", (359 ,600), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (403 ,600), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(img , "IC - 7414 NOT GATE", (320 ,120), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
cv2.putText(img , "In digital logic,an inverter", (630 ,290), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
cv2.putText(img , "or NOT gate is a logicgate", (630 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
cv2.putText(img , "which implements logical ", (630 ,360), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
cv2.putText(img , "negation.In mathematical ", (630 ,390), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
cv2.putText(img , "logic it isequivalent to the logical negation operator", (630 ,420), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
cv2.putText(img , " logical negation operator", (630 ,450), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)


 #  

cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.waitKey(0)
cv2.destroyAllWindows()

