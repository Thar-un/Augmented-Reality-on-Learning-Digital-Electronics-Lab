import cv2

def click_event(event, x, y,
    flags, params):

    global a1,a2,a3,a4,b1,b2,b3,b4;
    if event == cv2.EVENT_LBUTTONDOWN:
        if ((x > 360) and (x < 385)):
            if((y > 613) and (y < 630)):
                a4 = 0;print("0")
                cv2.putText(img , "0", (412 ,565), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 410) and (x < 435)):
            if ((y > 610 ) and (y < 630)):
                a4 = 1;print("1")
                cv2.putText(img , "1", (412 ,565), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 441) and (x < 465)):
            if((y > 613) and (y < 630)):
                a3 = 0;print("0")
                cv2.putText(img , "0", (482 ,565), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 493) and (x < 515)):
            if ((y > 610 ) and (y < 630)):
                a3 = 1;print("1")
                cv2.putText(img , "1", (482 ,565), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 522) and (x < 545)):
            if((y > 613) and (y < 630)):
                b3 = 0;print("0")
                cv2.putText(img , "0", (518 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 550) and (x < 575)):
            if ((y > 610 ) and (y < 630)):
                b3 = 1;print("1")
                cv2.putText(img , "1", (518 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 590) and (x < 616)):
            if((y > 613) and (y < 630)):
                b2 = 0;print("0")
                cv2.putText(img , "0", (627 ,568), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 640) and (x < 665)):
            if ((y > 610 ) and (y < 630)):
                b2 = 1;print("1")
                cv2.putText(img , "1", (627 ,568), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 670) and (x < 690)):
            if((y > 611) and (y < 630)):
                a2 = 0;print("0")
                cv2.putText(img , "0", (660 ,568), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 706) and (x < 732)):
            if ((y > 610 ) and (y < 630)):
                a2 = 1;print("1")
                cv2.putText(img , "1", (660 ,568), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 355) and (x < 375)):
            if((y > 221) and (y < 240)):
                b4 = 0;print("0")
                cv2.putText(img , "0", (412 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 420) and (x < 440)):
            if ((y > 220 ) and (y < 240)):
                b4 = 1;print("1")
                cv2.putText(img , "1", (410 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        #if ((x > 450) and (x < 475)):
         #   if((y > 220) and (y < 240)):
          #      a1 = 0;print("0")
           #     cv2.putText(img , "0", (483 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
            #    cv2.imshow(window_name,img)
        #if((x > 490) and (x < 517)):
         #   if ((y > 220 ) and (y < 240)):
          #      a1 = 1;print("1")
           #     cv2.putText(img , "1", (483 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
            #    cv2.imshow(window_name,img)
        #if ((x > 520) and (x < 540)):
         #   if((y > 220) and (y < 240)):
          #      a1 = 0;print("0")
           #     cv2.putText(img , "0", (518 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
            #    cv2.imshow(window_name,img)
        #if((x > 550) and (x < 565)):
         #   if ((y > 220 ) and (y < 240)):
          #      a1 = 1;print("1")
           #     cv2.putText(img , "1", (518 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
            #    cv2.imshow(window_name,img)
        if ((x > 570) and (x < 588)):
            if((y > 220) and (y < 240)):
                b1 = 0;print("0")
                cv2.putText(img , "0", (590 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 600) and (x < 616)):
            if ((y > 220 ) and (y < 240)):
                b1 = 1;print("1")
                cv2.putText(img , "1", (590 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 620) and (x < 636)):
            if((y > 220) and (y < 240)):
                a1 = 0;print("0")
                cv2.putText(img , "0", (622 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 655) and (x < 670)):
            if ((y > 220 ) and (y < 240)):
                a1 = 1;print("1")
                cv2.putText(img , "1", (622 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 485) and (x < 600)):
            if((y > 700) and (y < 745)):
                if a1 == 0:
                    d1 = 0;
                if a1 == 1:
                    d1 = 8;
                if a2 == 0:
                    d2 = 0;
                if a2 == 1:
                    d2 = 4;
                if a3 == 0:
                    d3 = 0;
                if a3 == 1:
                    d3 = 2;                
                if a4 == 0:
                    d4 = 0;
                if a4 == 1:
                    d4 = 1;
                if b1 == 0:
                    e1 = 0;
                if b1 == 1:
                    e1 = 8;
                if b2 == 0:
                    e2 = 0;
                if b2 == 1:
                    e2 = 4;
                if b3 == 0:
                    e3 = 0;
                if b3 == 1:
                    e3 = 2;
                if b4 == 0:
                    e4 = 0;
                if b4 == 1:
                    e4 = 1;
                d5 = d1 + d2 + d3 + d4 + e1 + e2 + e3 + e4;
                d6 = bin(d5).replace("0b", "")
                print(d6)
                cv2.putText(img , "The Output is", (805 ,386), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(img , d6, (805 ,420), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,0,0), 1, cv2.LINE_AA)
                cv2.imshow(window_name,img)


disp = 0
font = cv2.FONT_HERSHEY_SIMPLEX
org = (15, 25)
fontScale = 0.85
color = (255,255,255) #bgr
thickness = 2

image = cv2.imread('E:\\Final-year Project\\Dataset\\7483-3.jpg')
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
x = 410
y = 290
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
cv2.rectangle(img, (x+75,x1+150), (x+190,y1+175), (0,0,0), -2)#(375 , 670),(320 , 715)
cv2.putText(img , "Show Output", (486 ,730), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)
#lines!
cv2.line(img, (420 , 570), (370 , 610), colour, 2)
cv2.line(img, (420 , 570), (420 , 610), colour, 2)
cv2.line(img, (490 , 570), (450 , 610), colour, 2)
cv2.line(img, (490 , 570), (500 , 610), colour, 2)
cv2.line(img, (526 , 570), (528 , 610), colour, 2)
cv2.line(img, (526 , 570), (565 , 610), colour, 2)
cv2.line(img, (636 , 570), (600 , 610), colour, 2)
cv2.line(img, (636 , 570), (650 , 610), colour, 2)
cv2.line(img, (670 , 570), (675 , 610), colour, 2)
cv2.line(img, (670 , 570), (715 , 610), colour, 2)
#input-box1
cv2.rectangle(img, (361,611), (383,632), (0,0,0), -2)
cv2.rectangle(img, (410,611), (433,632), (0,0,0), -2)
#input-box2
cv2.rectangle(img, (440 , 611), (465 , 632), (0,0,0), -2)
cv2.rectangle(img, (492 , 611), (515 , 632), (0,0,0), -2)
cv2.putText(img , "0", (360 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (410 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (522 , 611), (545 , 632), (0,0,0), -2)
cv2.rectangle(img, (550 , 611), (575 , 632), (0,0,0), -2)
cv2.putText(img , "0", (440 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (495 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (590 , 611), (615 , 632), (0,0,0), -2)
cv2.rectangle(img, (640 , 611), (665 , 632), (0,0,0), -2)
cv2.putText(img , "0", (525 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (555 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (668 , 611), (690 , 632), (0,0,0), -2)
cv2.rectangle(img, (707 , 611), (734 , 632), (0,0,0), -2)
cv2.putText(img , "0", (595 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (643 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "0", (671 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (715 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#input-box2
cv2.line(img, (420 , 290), (365 , 240), colour, 2)
cv2.line(img, (420 , 290), (430 , 240), colour, 2)
cv2.rectangle(img, (355 , 240), (375 , 220), (0,0,0), -2)
cv2.rectangle(img, (417 , 240), (440 , 220), (0,0,0), -2)
cv2.putText(img , "0", (358 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (420 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
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
cv2.line(img, (590 , 290), (575 , 240), colour, 2)
cv2.line(img, (590 , 290), (610 , 240), colour, 2)
cv2.rectangle(img, (570 , 240), (585 , 220), (0,0,0), -2)
cv2.rectangle(img, (600 , 240), (615 , 220), (0,0,0), -2)
cv2.putText(img , "0", (570 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (600 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.line(img, (630 , 290), (625 , 240), colour, 2)
cv2.line(img, (630 , 290), (665 , 240), colour, 2)
cv2.rectangle(img, (618 , 220), (635 , 240), (0,0,0), -2)
cv2.rectangle(img, (655 , 240), (670 , 220), (0,0,0), -2)
cv2.putText(img , "0", (620 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (655 ,240), font, fontScale, color, thickness, cv2.LINE_AA)

#GND
cv2.line(img, (760 , 535), (555 , 535), colour, 2)
cv2.line(img, (760 , 535), (805 , 535), colour, 2)
cv2.line(img, (555 , 535), (555 , 550), colour, 2)
cv2.rectangle(img, (800 , 520), (865 , 560), (0,0,0), -2)
cv2.putText(img , "Vcc", (800 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
#5V
cv2.line(img, (470 , 180), (555 , 180), colour, 2)
cv2.line(img, (555 , 180), (555 , 290), colour, 2)
cv2.rectangle(img, (400 , 170), (470 , 195), (0,0,0), -2)
cv2.putText(img , "GND", (400 ,190), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.namedWindow(window_name)
cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.waitKey(0)
cv2.destroyAllWindows()

