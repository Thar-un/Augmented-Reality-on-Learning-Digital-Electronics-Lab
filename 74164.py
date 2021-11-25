import cv2

def click_event(event, x, y,
    flags, params):

    global a1,a2,a3,a4,b1,b2,b3,b4,clk;
    if event == cv2.EVENT_LBUTTONDOWN:
        if ((x > 342) and (x < 365)):
            if((y > 550) and (y < 575)):
                a1 = 0;print("0")
                cv2.putText(img , "0", (383 ,500), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 385) and (x < 410)):
            if ((y > 550 ) and (y < 575)):
                a1 = 1;print("1")
                cv2.putText(img , "1", (383 ,500), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 415) and (x < 436)):
            if((y > 550) and (y < 575)):
                a2 = 0;print("0")
                cv2.putText(img , "0", (420 ,500), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 445) and (x < 466)):
            if ((y > 545 ) and (y < 575)):
                a2 = 1;print("1")
                cv2.putText(img , "1", (420 ,500), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 590) and (x < 610)):
            if ((y > 210 ) and (y < 310)):
                clk = clk + 1;
                print(clk)
                cv2.putText(img , "1", (590 ,307), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if clk == 1 and a1 == 0:
                cv2.putText(img ,"0", (450 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if clk == 1 and a1 == 1:
                cv2.putText(img ,"1", (450 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if clk == 2:
            if a1 == 0:
                cv2.rectangle(img, (450,480), (470,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"0", (487 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a1 == 1:
                cv2.rectangle(img, (450,480), (470,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"1", (487 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a2 == 0:
                cv2.rectangle(img, (450,480), (470,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"0", (451 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a2 == 1:
                cv2.rectangle(img, (450,480), (470,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"1", (451 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if clk == 3:
            if a1 == 0:
                cv2.rectangle(img, (485,480), (505,500), (0,0,0), -2)
                cv2.putText(img ,"0", (523 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a1 == 1:
                cv2.rectangle(img, (485,480), (505,500), (0,0,0), -2)
                cv2.putText(img ,"1", (523 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a2 == 0:
                cv2.rectangle(img, (450,480), (470,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"0", (487 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a2 == 1:
                cv2.rectangle(img, (450,480), (470,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"1", (487 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if clk == 4:
            if a1 == 0:
                cv2.rectangle(img, (520,480), (540,500), (0,0,0), -2)
                cv2.putText(img ,"0", (558 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a1 == 1:
                cv2.rectangle(img, (520,480), (540,500), (0,0,0), -2)
                cv2.putText(img ,"1", (558 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a2 == 0:
                cv2.rectangle(img, (485,480), (505,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"0", (525 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
            if a2 == 1:
                cv2.rectangle(img, (485,480), (505,500), (0,0,0), -2)  #(320,50), (340,70)
                cv2.putText(img ,"1", (525 ,497), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)


disp = 0
font = cv2.FONT_HERSHEY_SIMPLEX
org = (15, 25)
fontScale = 0.85
color = (255,255,255) #bgr
thickness = 2

image = cv2.imread('E:\\Final-year Project\\Dataset\\74164_1.jpg')
window_name = 'Image'
if(type(image) == type(None)):
    pass
else:
    img = cv2.resize(image, (1100, 800), interpolation=cv2.INTER_AREA)
    #cv2.imshow('image',image)
# Start coordinate, here (5, 5)(column , row)
color1 = (160,250,250)
colour = (0,0,0)#bgr
#checkboxes-up
x = 380
y = 290
cv2.rectangle(img, (x,y), (x+20,y+20), (0,0,0), -2)     #(250,290), (270,310)
cv2.rectangle(img, (x+35,y), (x+55,y+20), (0,0,0), -2)  #(505,290), (525,310)
cv2.rectangle(img, (x+70,y), (x+90,y+20), (0,0,0), -2)  #(540,290), (560,310)
cv2.rectangle(img, (x+105,y), (x+125,y+20), (0,0,0), -2)#(575,290), (595,310)
cv2.rectangle(img, (x+140,y), (x+160,y+20), (0,0,0), -2)#(610,290), (630,310)
cv2.rectangle(img, (x+175,y), (x+195,y+20), (0,0,0), -2)#(645,290), (665,310)
cv2.rectangle(img, (x+210,y), (x+230,y+20), (0,0,0), -2)#(680,290), (700,310)
#cv2.rectangle(img, (x+240,y), (x+260,y+20), (0,0,0), -2)
#checkboxes-dow
x1 = 480    
y1 = 500
cv2.rectangle(img, (x,x1), (x+20,y1), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,x1), (x+55,y1), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (450,480), (470,500), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (485,480), (505,500), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (520,480), (540,500), (0,0,0), -2)#(390,50), (410,70)
cv2.rectangle(img, (555,480), (575,500), (0,0,0), -2)#(425,50), (445,70)
cv2.rectangle(img, (595,480), (615,500), (0,0,0), -2)#(470,50), (490,70)
#cv2.rectangle(img, (x+250,x1), (x+270,y1), (0,0,0), -2)
#output-box
cv2.rectangle(img, (x+75,x1+150), (x+190,y1+175), (0,0,0), -2)#(375 , 670),(320 , 715)
cv2.putText(img , "Show Output", (458 ,660), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)
#lines!
cv2.line(img, (390 , 500), (350 , 555), colour, 2)
cv2.line(img, (390 , 500), (395 , 555), colour, 2)
cv2.line(img, (425 , 500), (420 , 555), colour, 2)
cv2.line(img, (425 , 500), (455 , 555), colour, 2)
#input-box1
cv2.rectangle(img, (341,550), (363,575), (0,0,0), -2)
cv2.rectangle(img, (383,550), (405,575), (0,0,0), -2)
cv2.putText(img , "0", (345 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (385 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
#input-box2
cv2.rectangle(img, (413,550), (433,575), (0,0,0), -2)
cv2.rectangle(img, (443,550), (465,575), (0,0,0), -2)
#cv2.rectangle(img, (440 , 611), (465 , 632), (0,0,0), -2)
#cv2.rectangle(img, (492 , 611), (515 , 632), (0,0,0), -2)
#cv2.putText(img , "0", (360 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (410 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.rectangle(img, (522 , 611), (545 , 632), (0,0,0), -2)
#cv2.rectangle(img, (550 , 611), (575 , 632), (0,0,0), -2)
#cv2.putText(img , "0", (440 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (495 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
##cv2.rectangle(img, (590 , 611), (615 , 632), (0,0,0), -2)
#cv2.rectangle(img, (640 , 611), (665 , 632), (0,0,0), -2)
#cv2.putText(img , "0", (525 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (555 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.rectangle(img, (668 , 611), (690 , 632), (0,0,0), -2)
#cv2.rectangle(img, (707 , 611), (734 , 632), (0,0,0), -2)
#cv2.putText(img , "0", (595 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (643 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "0", (671 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (715 ,630), font, fontScale, color, thickness, cv2.LINE_AA)
#input-box2
#cv2.line(img, (420 , 290), (365 , 240), colour, 2)
#cv2.line(img, (420 , 290), (430 , 240), colour, 2)
#cv2.rectangle(img, (355 , 240), (375 , 220), (0,0,0), -2)
#cv2.rectangle(img, (417 , 240), (440 , 220), (0,0,0), -2)
#cv2.putText(img , "0", (358 ,240), font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(img , "1", (420 ,240), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(img , "IC- 74164 SIRIAL INPUT PARALLEL OUTPUT", (480 ,70), font, fontScale, (0,0,0), thickness, cv2.LINE_AA)
cv2.putText(img , "74LS164 is a high ", (8 ,400), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "speed shift register", (8 ,430), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "with serial input  ", (8 ,460), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "of data and parallel ", (8 ,490), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "output of data.That ", (8 ,515), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "means data goes into", (8 ,550), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "IC bit by bit serially ", (8 ,580), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "and 8-bit data ", (8 ,610), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "appears on the output pins", (8 ,640), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
clk = 0
 
#GND
cv2.line(img, (800 , 535), (610 , 535), colour, 2)
cv2.line(img, (610 , 535), (610 , 500), colour, 2)
cv2.rectangle(img, (800 , 520), (865 , 560), (0,0,0), -2)
cv2.putText(img , "GND", (800 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
#CLK
cv2.line(img, (610 , 300), (800 , 300), colour, 2)
cv2.rectangle(img, (800 , 280), (895 , 320), (0,0,0), -2)
cv2.putText(img , "CLOCK", (805 ,315), font, fontScale, color, thickness, cv2.LINE_AA)
#5V
cv2.line(img, (250 , 180), (390 , 180), colour, 2)
cv2.line(img, (390 , 180), (390 , 290), colour, 2)
cv2.rectangle(img, (200 , 150), (250 , 195), (0,0,0), -2)
cv2.putText(img , "Vcc", (200 ,190), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(img , "0", (416 ,570), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (447 ,570), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.namedWindow(window_name)
cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.waitKey(0)
cv2.destroyAllWindows()

