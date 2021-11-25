import cv2

def click_event(event, x, y,
    flags, params):

    global a1,a2,a3,a4,clk;
    if event == cv2.EVENT_LBUTTONDOWN:
        if ((x > 472) and (x < 491)):
            if((y > 611) and (y < 632)):
                a1 = 0;print("0")
                cv2.putText(img , "0", (542 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 501) and (x < 521)):
            if ((y > 611 ) and (y < 632)):
                a1 = 1;print("1")
                cv2.putText(img , "1", (542 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 527) and (x < 546)):
            if((y > 610) and (y < 630)):
                a2 = 0;print("0")
                cv2.putText(img , "0", (576 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 555) and (x < 572)):
            if ((y > 610 ) and (y < 630)):
                a2 = 1;print("1")
                cv2.putText(img , "1", (576 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 585) and (x < 605)):
            if((y > 610) and (y < 630)):
                a3 = 0;print("0")
                cv2.putText(img , "0", (612 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 615) and (x < 635)):
            if ((y > 610 ) and (y < 630)):
                a3 = 1;print("1")
                cv2.putText(img , "1", (612 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 642) and (x < 665)):
            if((y > 610) and (y < 630)):
                a4 = 0;print("0")
                cv2.putText(img , "0", (648 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 675) and (x < 700)):
            if ((y > 610 ) and (y < 630)):
                a4 = 1;print("1")
                cv2.putText(img , "1", (648 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 645) and (x < 665)):
            if((y > 300) and (y < 320)):
                clk = clk + 1;print(clk);
                if clk == 1 and a1 == 0:
                        cv2.putText(img ,"0", (611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                if clk == 1 and a1 == 1:
                        cv2.putText(img ,"1", (611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                if clk == 2:
                    if a2 == 0:
                        cv2.rectangle(img, (610,300), (630,320), color1, -2)  #(320,50), (340,70)
                        cv2.putText(img ,"0", (611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                    if a2 == 1:
                        cv2.rectangle(img, (610,300), (630,320), color1, -2)  #(320,50), (340,70)
                        cv2.putText(img ,"1", (611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                if clk == 3:
                    if a3 == 0:
                        cv2.rectangle(img, (610,300), (630,320), color1, -2)  #(320,50), (340,70)
                        cv2.putText(img ,"0",(611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                    if a3 == 1:
                        cv2.rectangle(img, (610,300), (630,320), color1, -2)  #(320,50), (340,70)
                        cv2.putText(img ,"1", (611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                if clk == 4:
                    if a4 == 0:
                        cv2.rectangle(img,(610,300), (630,320), color1, -2)
                        cv2.putText(img ,"0", (611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                    if a4 == 1:
                        cv2.rectangle(img, (610,300), (630,320), color1, -2)
                        cv2.putText(img ,"1", (611 ,320), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
                        cv2.imshow(window_name,img)




disp = 0
font = cv2.FONT_HERSHEY_SIMPLEX
org = (15, 25)
fontScale = 0.85
color = (255,255,255) #bgr
thickness = 2

image = cv2.imread('E:\\Final-year Project\\74194\\frame.jpg')
window_name = 'Image'
if(type(image) == type(None)):
    pass
else:
    img = cv2.resize(image, (1100, 800), interpolation=cv2.INTER_AREA)
    #cv2.imshow('image',image)
# Start coordinate, here (5, 5)(column , row)
color1 = (0,107,127)
colour = (0,0,0)#bgr
#checkboxes-up
x = 470
y = 300
cv2.rectangle(img, (x,y), (x+20,y+20), (0,0,0), -2)     #(250,290), (270,310)
cv2.rectangle(img, (x+35,y), (x+55,y+20), (0,0,0), -2)  #(505,290), (525,310)
cv2.rectangle(img, (x+70,y), (x+90,y+20), (0,0,0), -2)  #(540,290), (560,310)
cv2.rectangle(img, (x+105,y), (x+125,y+20),(0,0,0), -2)#(575,290), (595,310)
cv2.rectangle(img, (x+140,y), (x+160,y+20), (160,250,250), -2)#(610,290), (630,310)
cv2.rectangle(img, (x+175,y), (x+195,y+20), (0,0,0), -2)#(645,290), (665,310)
cv2.rectangle(img, (x+210,y), (x+230,y+20), (0,0,0), -2)#(680,290), (700,310)
cv2.rectangle(img, (x+240,y), (x+260,y+20), (0,0,0), -2)
#checkboxes-dow
x1 = 550    
y1 = 570
cv2.rectangle(img, (x,x1), (x+20,y1), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,x1), (x+55,y1), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,x1), (x+90,y1), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,x1), (x+125,y1), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,x1), (x+160,y1), (0,0,0), -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,x1), (x+195,y1), (0,0,0), -2)#(425,50), (445,70)
cv2.rectangle(img, (x+215,x1), (x+235,y1), (0,0,0), -2)#(470,50), (490,70)
cv2.rectangle(img, (x+250,x1), (x+270,y1), (0,0,0), -2)
#output-box
cv2.rectangle(img, (457,701), (598,747), (0,0,0), -2)#(375 , 670),(320 , 715)
cv2.putText(img , "Show Output", (475 ,730), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)
#lines!
cv2.line(img, (550 , 570), (480 , 610), colour, 2)
cv2.line(img, (550 , 570), (510 , 610), colour, 2)
cv2.line(img, (585 , 570), (530 , 610), colour, 2)
cv2.line(img, (585 , 570), (565 , 610), colour, 2)
cv2.line(img, (620 , 570), (595 , 610), colour, 2)
cv2.line(img, (620 , 570), (625 , 610), colour, 2)
cv2.line(img, (655 , 570), (650 , 610), colour, 2)
cv2.line(img, (655 , 570), (680 , 610), colour, 2)
cv2.line(img, (650 , 300), (650 , 260), colour, 2)
cv2.line(img, (650 , 260), (796 , 260), colour, 2)
cv2.rectangle(img, (797 , 248), (850 , 278), (0,0,0), -2)
cv2.putText(img , "CLK", (800 ,275), font, fontScale, color, 2, cv2.LINE_AA)
#input-box
cv2.rectangle(img, (472 , 610), (490 , 630), (0,0,0), -2)
cv2.rectangle(img, (500 , 610), (520 , 630), (0,0,0), -2)
cv2.putText(img , "0", (470 ,630), font, fontScale, color, 2, cv2.LINE_AA)
cv2.putText(img , "1", (500 ,630), font, fontScale, color, 2, cv2.LINE_AA)
cv2.rectangle(img, (527 , 610), (545 , 630), (0,0,0), -2)
cv2.rectangle(img, (552 , 610), (570 , 630), (0,0,0), -2)
cv2.putText(img , "0", (528 ,630), font, fontScale, color, 2, cv2.LINE_AA)
cv2.putText(img , "1", (553 ,630), font, fontScale, color, 2, cv2.LINE_AA)
cv2.rectangle(img, (585 , 610), (605 , 630), (0,0,0), -2)
cv2.rectangle(img, (615 , 610), (635 , 630), (0,0,0), -2)
cv2.putText(img , "0", (585 ,630), font, fontScale, color, 2, cv2.LINE_AA)
cv2.putText(img , "1", (618 ,630), font, fontScale, color, 2, cv2.LINE_AA)
cv2.rectangle(img, (640 , 610), (663 , 630), (0,0,0), -2)
cv2.rectangle(img, (673 , 610), (698 , 630), (0,0,0), -2)
cv2.putText(img , "0", (642 ,630), font, fontScale, color, 2, cv2.LINE_AA)
cv2.putText(img , "1", (675 ,630), font, fontScale, color, 2, cv2.LINE_AA)
#cv2.rectangle(img, (615 , 258), (638 , 233), (0,0,0), -2)
#cv2.rectangle(img, (662 , 257), (686 , 233), (0,0,0), -2)
#cv2.putText(img , "0", (615 ,257), font, fontScale, color, 2, cv2.LINE_AA)
#cv2.putText(img , "1", (665 ,257), font, fontScale, color, 2, cv2.LINE_AA)

#input-box2
#      , 

cv2.putText(img , "IC- 74194 SERIAL IN PARALLEL OUT", (420 ,70), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "This configuration has ", (7 ,309), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "the data input in ", (7 ,330), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "parallel format, ", (7 ,360), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "It stores data and ", (7 ,390), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "shifts it on a clock ", (7 ,420), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "by clock basis ", (7 ,450), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "and delays it by the ", (7 ,480), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "number of stages times", (7 ,510), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "the clock period", (7 ,540), font, fontScale, (0,0,0), 1, cv2.LINE_AA)

#cv2.line(img, (490 , 290), (460 , 240), colour, 2)
#cv2.line(img, (490 , 290), (505 , 240), colour, 2)
#cv2.rectangle(img, (450 , 240), (475 , 220), (0,0,0), -2)
#cv2.rectangle(img, (490 , 240), (515 , 220), (0,0,0), -2)
#cv2.putText(img , "0", (455 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (495 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.line(img, (525 , 290), (530 , 240), colour, 2)
#cv2.line(img, (525 , 290), (560 , 240), colour, 2)
#cv2.rectangle(img, (520 , 240), (540 , 220), (0,0,0), -2)
#cv2.rectangle(img, (550 , 240), (566 , 220), (0,0,0), -2)
#cv2.putText(img , "0", (525 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (550 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
#GND
#cv2.line(img, (760 , 535), (555 , 535), colour, 2)
#cv2.line(img, (760 , 535), (805 , 535), colour, 2)
#cv2.line(img, (555 , 535), (555 , 550), colour, 2)
#cv2.rectangle(img, (800 , 520), (865 , 560), (0,0,0), -2)
#cv2.putText(img , "Vcc", (800 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
#5V
#cv2.line(img, (470 , 180), (555 , 180), colour, 2)
#cv2.line(img, (555 , 180), (555 , 290), colour, 2)
#cv2.rectangle(img, (400 , 170), (470 , 195), (0,0,0), -2)
#cv2.putText(img , "GND", (400 ,190), font, fontScale, color, thickness, cv2.LINE_AA)
clk = 0
cv2.namedWindow(window_name)
cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.waitKey(0)
cv2.destroyAllWindows()

