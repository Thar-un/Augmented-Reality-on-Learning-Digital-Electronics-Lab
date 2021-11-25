import cv2

def click_event(event, x, y,
    flags, params):

    global a1,a2,a3,a0,b1,b2,b3,b0,d5,e5;
    if event == cv2.EVENT_LBUTTONDOWN:
        if ((x > 360) and (x < 383)):
            if((y > 611) and (y < 632)):
                b3 = 0;print("0")
                cv2.putText(img , "0", (383 ,567), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 410) and (x < 433)):
            if ((y > 611 ) and (y < 632)):
                b3 = 1;print("1")
                cv2.putText(img , "1", (383 ,567), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 389) and (x < 408)):
            if((y > 263) and (y < 280)):
                a3 = 0;print("0")
                cv2.putText(img , "0", (417 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 420) and (x < 434)):
            if ((y > 260 ) and (y < 283)):
                a3 = 1;print("1")
                cv2.putText(img , "1", (417 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 437) and (x < 450)):
            if((y > 260) and (y < 284)):
                b2 = 0;print("0")
                cv2.putText(img , "0", (453 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 460) and (x < 478)):
            if ((y > 262 ) and (y < 288)):
                b2 = 1;print("1")
                cv2.putText(img , "1", (453 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 481) and (x < 497)):
            if((y > 260) and (y < 284)):
                a2 = 0;print("0")
                cv2.putText(img , "0", (487 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 500) and (x < 516)):
            if ((y > 262 ) and (y < 286)):
                a2 = 1;print("1")
                cv2.putText(img , "1", (487 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 517) and (x < 534)):
            if((y > 260) and (y < 284)):
                b1 = 0;print("0")
                cv2.putText(img , "0", (524 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 536) and (x < 553)):
            if ((y > 260 ) and (y < 286)):
                b1 = 1;print("1")
                cv2.putText(img , "1", (524 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 556) and (x < 570)):
            if((y > 260) and (y < 284)):
                a1 = 0;print("0")
                cv2.putText(img , "0", (557 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 572) and (x < 586)):
            if ((y > 260 ) and (y < 286)):
                a1 = 1;print("1")
                cv2.putText(img , "1", (557 ,367), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 590) and (x < 605)):
            if((y > 260) and (y < 285)):
                b0 = 0;print("0")
                cv2.putText(img , "0", (593 ,371), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 613) and (x < 628)):
            if ((y > 263 ) and (y < 288)):
                b0 = 1;print("1")
                cv2.putText(img , "1", (593 ,371), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 647) and (x < 671)):
            if((y > 275) and (y < 295)):
                a0 = 0;print("0")
                cv2.putText(img , "0", (625 ,368), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 682) and (x < 711)):
            if ((y > 321 ) and (y < 338)):
                a0 = 1;print("1")
                cv2.putText(img , "1", (625 ,368), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 457) and (x < 600)):
            if((y > 700) and (y < 748)):
                if a1 == 0:
                    d1 = 0;
                if a1 == 1:
                    d1 = 2;
                if a2 == 0:
                    d2 = 0;
                if a2 == 1:
                    d2 = 4;
                if a3 == 0:
                    d3 = 0;
                if a3 == 1:
                    d3 = 8;                
                if a0 == 0:
                    d0 = 0;
                if a0 == 1:
                    d0 = 1;
                if b1 == 0:
                    e1 = 0;
                if b1 == 1:
                    e1 = 2;
                if b2 == 0:
                    e2 = 0;
                if b2 == 1:
                    e2 = 4;
                if b3 == 0:
                    e3 = 0;
                if b3 == 1:
                    e3 = 8;
                if b0 == 0:
                    e0 = 0;
                if b0 == 1:
                    e0 = 1;
                d5 = d1 + d2 + d3 + d0; 
                e5 = e0 + e1 + e2 + e3;
                if d5 > e5:
                    print("a>b");
                    cv2.putText(img , "1", (522 ,570), cv2.FONT_HERSHEY_COMPLEX, 0.75, color, 1, cv2.LINE_AA)
                    cv2.imshow(window_name,img)
                if d5 == e5:
                    print("a==b");
                    cv2.putText(img , "1", (557 ,570), cv2.FONT_HERSHEY_COMPLEX, 0.75, color, 1, cv2.LINE_AA)
                    cv2.imshow(window_name,img)
                if d5 < e5:
                    print("a<b");
                    cv2.putText(img , "1", (597 ,570), cv2.FONT_HERSHEY_COMPLEX, 0.75, color, 1, cv2.LINE_AA)
                    cv2.imshow(window_name,img)





disp = 0
font = cv2.FONT_HERSHEY_SIMPLEX
org = (15, 25)
fontScale = 0.85
color = (255,255,255) #bgr
thickness = 2

image = cv2.imread('E:\\Final-year Project\\Dataset\\mag\\frame0.jpg')
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
x = 380
y = 350
cv2.rectangle(img, (x,y), (x+20,y+20), (0,0,0), -2)     #(250,290), (270,310)
cv2.rectangle(img, (x+35,y), (x+55,y+20), (0,0,0), -2)  #(505,290), (525,310)
cv2.rectangle(img, (x+70,y), (x+90,y+20), (0,0,0), -2)  #(540,290), (560,310)
cv2.rectangle(img, (x+105,y), (x+125,y+20), (0,0,0), -2)#(575,290), (595,310)
cv2.rectangle(img, (x+140,y), (x+160,y+20), (0,0,0), -2)#(610,290), (630,310)
cv2.rectangle(img, (x+175,y), (x+195,y+20), (0,0,0), -2)#(645,290), (665,310)
cv2.rectangle(img, (x+210,y), (x+230,y+20), (0,0,0), -2)#(680,290), (700,310)
cv2.rectangle(img, (x+240,y), (x+260,y+20), color1, -2)
#checkboxes-dow
x1 = 550    
y1 = 570
cv2.rectangle(img, (x,x1), (x+20,y1), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,x1), (x+55,y1), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,x1), (x+90,y1), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,x1), (x+125,y1), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,x1), (x+160,y1), (0,0,0), -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,x1), (x+195,y1), (0,0,0), -2)#(425,50), (445,70)
cv2.rectangle(img, (x+215,x1), (x+235,y1), color1, -2)#(470,50), (490,70)
cv2.rectangle(img, (x+250,x1), (x+270,y1), (0,0,0), -2)
#output-box
cv2.rectangle(img, (457,701), (598,747), (0,0,0), -2)#(375 , 670),(320 , 715)
cv2.putText(img , "Show Output", (475 ,730), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)
#lines!
cv2.line(img, (390 , 570), (420 , 610), colour, 2)
cv2.line(img, (390 , 570), (371 , 610), colour, 2)
cv2.line(img, (425 , 350), (400 , 280), colour, 2)
cv2.line(img, (425 , 350), (425 , 280), colour, 2)
cv2.line(img, (460 , 350), (440 , 285), colour, 2)
cv2.line(img, (460 , 350), (470 , 285), colour, 2)
cv2.line(img, (495 , 350), (490 , 285), colour, 2)
cv2.line(img, (495 , 350), (510 , 280), colour, 2)
cv2.line(img, (530 , 350), (520 , 285), colour, 2)
cv2.line(img, (530 , 350), (546 , 280), colour, 2)
cv2.line(img, (565 , 350), (558 , 283), colour, 2)
cv2.line(img, (565 , 350), (581 , 283), colour, 2)
cv2.line(img, (600 , 350), (594 , 283), colour, 2)
cv2.line(img, (600 , 350), (620 , 283), colour, 2)
cv2.line(img, (630 , 350), (655 , 290), colour, 2)
cv2.line(img, (630 , 350), (686 , 330), colour, 2)

#input-box1
cv2.rectangle(img, (361,611), (383,632), (0,0,0), -2)
cv2.rectangle(img, (410,611), (433,632), (0,0,0), -2)
cv2.putText(img , "0", (364 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (410 ,627), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (407,281), (390,265), (0,0,0), -2)
cv2.rectangle(img, (420,281), (433,260), (0,0,0), -2)
cv2.putText(img , "0", (390 ,282), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (420 ,282), font, fontScale, color, thickness, cv2.LINE_AA)
########
cv2.rectangle(img, (438,283), (450,260), (0,0,0), -2)
cv2.rectangle(img, (460,262), (478,288), (0,0,0), -2)
cv2.putText(img , "0", (436 ,282), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (462 ,286), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (481,262), (498,286), (0,0,0), -2)
cv2.rectangle(img, (502,261), (515,285), (0,0,0), -2)
cv2.putText(img , "0", (482 ,286), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (505 ,283), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (517,262), (530,286), (0,0,0), -2)
cv2.rectangle(img, (536,286), (552,260), (0,0,0), -2)
cv2.putText(img , "0", (520 ,284), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (540 ,285), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (568,286), (556,260), (0,0,0), -2)
cv2.rectangle(img, (572,286), (586,260), (0,0,0), -2)
cv2.putText(img , "0", (556 ,281), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (575 ,283), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (588,262), (605,284), (0,0,0), -2)
cv2.rectangle(img, (611,263), (628,286), (0,0,0), -2)
cv2.putText(img , "0", (590 ,283), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (613 ,287), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (648,275), (671,294), (0,0,0), -2)
cv2.rectangle(img, (681,320), (710,340), (0,0,0), -2)
cv2.putText(img , "0", (650 ,294), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (685 ,340), font, fontScale, color, thickness, cv2.LINE_AA)

#input-box2

#input-box2

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

cv2.namedWindow(window_name)
cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.waitKey(0)
cv2.destroyAllWindows()

