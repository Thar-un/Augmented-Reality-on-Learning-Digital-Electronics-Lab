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
    cv2.imshow(window_name,img)
    if event == cv2.EVENT_LBUTTONDOWN:
        if ((x > 460) and (x < 480)):
            if((y > 600) and (y < 620)):
                a1 = 0;print("0")
                cv2.putText(img , "0", (504 ,547), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 490) and (x < 510)):
            if ((y > 600 ) and (y < 620)):
                a1 = 1;print("1")
                cv2.putText(img , "1", (504 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 520) and (x < 540)):
            if((y > 600) and (y < 620)):
                a2 = 0;print("0")
                cv2.putText(img , "0", (540 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 550) and (x < 570)):
            if ((y > 600 ) and (y < 620)):
                a2 = 1;print("1")
                cv2.putText(img , "1", (540 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 580) and (x < 600)):
            if ((y > 600 ) and (y < 620)):
                a3 = 0;print("0")
                cv2.putText(img , "0", (575 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 610) and (x < 630)):
            if ((y > 600 ) and (y < 620)):
                a3 = 1;print("1")
                cv2.putText(img , "1", (575 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 640) and (x < 660)):
            if ((y > 600 ) and (y < 620)):
                a4 = 0;print("0")
                cv2.putText(img , "0", (610 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 670) and (x < 690)):
            if ((y > 600 ) and (y < 620)):
                a4 = 1;print("1")
                cv2.putText(img , "1", (610 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 705) and (x < 725)):
            if ((y > 600 ) and (y < 620)):
                a5 = 0;print("0")
                cv2.putText(img , "0", (645 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 740) and (x < 760)):
            if ((y > 600 ) and (y < 620)):
                a5 = 1;print("1")
                cv2.putText(img , "1", (645 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 520) and (x < 540)):
            if ((y > 240 ) and (y < 260)):
                a6 = 0;print("0")
                cv2.putText(img , "0", (540 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 550) and (x < 570)):
            if ((y > 240 ) and (y < 260)):
                a6 = 1;print("1")
                cv2.putText(img , "1", (540 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 545) and (x < 660)):#(545 , 678),(660 , 725)
            if((y > 678) and (y < 725)):
                    #a1 = s0 , a6 = s1 , a3=d1,a4=d2,a5=d3,a2=d4 ,
                    if ((a1 == 0) and (a6 == 0)):
                        print("1)",a1," ",a2)
                        if(a2 == 0):
                            cv2.putText(img , "0", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                        if(a2 == 1):
                            cv2.putText(img , "1", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                    elif ((a1 == 0) and (a6 == 1)):
                        print("2)",a1," ",a2)
                        if(a3 == 0):
                            cv2.putText(img , "0", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                        if(a3 == 1):
                            cv2.putText(img , "1", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                    elif ((a1 == 1) and (a6 == 0)):
                        print("3)",a1," ",a2)
                        if(a4 == 0):
                            cv2.putText(img , "0", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                        if(a4 == 1):
                            cv2.putText(img , "1", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                    elif ((a1 == 1) and (a6 == 1)):                        
                        print("4)",a1," ",a2)
                        if(a5 == 0):
                            cv2.putText(img , "0", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                        if(a5 == 1):
                            cv2.putText(img , "1", (690 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (710 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
                            cv2.imshow(window_name,img)

# path   
img = cv2.imread('E:\\Final-year Project\\Dataset\\and\\7485.jpg', 1)
window_name = 'Image'
#img = cv2.resize(imag, (1100, 800))# Resize image

# Start coordinate, here (5, 5)(column , row)
color1 = (0,107,127)
colour = (0,0,0)#bgr
#checkboxes-up
x = 470
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
x1 = 528    
y1 = 550
cv2.rectangle(img, (x,x1), (x+20,y1), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,x1), (x+55,y1), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,x1), (x+90,y1), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,x1), (x+125,y1), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,x1), (x+160,y1), (0,0,0), -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,x1), (x+195,y1), (0,0,0), -2)#(425,50), (445,70)
cv2.rectangle(img, (x+215,x1), (x+235,y1), color1, -2)#(470,50), (490,70)
cv2.rectangle(img, (x+250,x1), (x+270,y1), (0,0,0), -2)#(720,528),(740,290)
#output-box
cv2.rectangle(img, (x+75,x1+150), (x+190,y1+175), (0,0,0), -2)#(545 , 678),(660 , 725)
cv2.putText(img , "Show Output", (545 ,710), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)
#lines!
cv2.line(img, (505,550), (470,610), colour, 2)
cv2.line(img, (515 , 550), (500 , 610), colour, 2)
cv2.line(img, (550 , 550), (530 , 610), colour, 2)
cv2.line(img, (550 , 550), (560 , 610), colour, 2)
cv2.line(img, (585 , 550), (585 , 610), colour, 2)
cv2.line(img, (585 , 550), (625 , 610), colour, 2)
cv2.line(img, (620 , 550), (655 , 610), colour, 2)
cv2.line(img, (620 , 550), (685 , 610), colour, 2)
cv2.line(img, (660 , 550), (718 , 610), colour, 2)
cv2.line(img, (660 , 550), (757 , 600), colour, 2)
cv2.line(img, (550 , 300), (530 , 250), colour, 2)
cv2.line(img, (550 , 300), (560 , 250), colour, 2)

#input-boxes
cv2.rectangle(img, (460,600), (480,620), (0,0,0), -2)
cv2.rectangle(img, (490,600), (510,620), (0,0,0), -2)
cv2.putText(img , "0", (460 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (490 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (520,600), (540,620), (0,0,0), -2)
cv2.rectangle(img, (550,600), (570,620), (0,0,0), -2)
cv2.putText(img , "0", (520 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (550 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (580,600), (600,620), (0,0,0), -2)
cv2.rectangle(img, (610,600), (630,620), (0,0,0), -2)
cv2.putText(img , "0", (580 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (610 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (640,600), (660,620), (0,0,0), -2)
cv2.rectangle(img, (670,600), (690,620), (0,0,0), -2)
cv2.putText(img , "0", (640 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (670 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (705,600), (725,620), (0,0,0), -2)
cv2.rectangle(img, (740,600), (760,620), (0,0,0), -2)
cv2.putText(img , "0", (705 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (740 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (520,240), (540,260), (0,0,0), -2)
cv2.rectangle(img, (550,240), (570,260), (0,0,0), -2)
cv2.putText(img , "0", (520 ,260), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (550 ,260), font, fontScale, color, thickness, cv2.LINE_AA)

#GND
#cv2.line(img, (725 , 535), (760 , 535), colour, 2)
#cv2.line(img, (760 , 535), (805 , 535), colour, 2)
#cv2.rectangle(img, (800 , 520), (865 , 560), (0,0,0), -2)
#cv2.putText(img , "GND", (800 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
#5V
#cv2.line(img, (540 , 225), (540 , 180), colour, 2)
#cv2.line(img, (420 , 300), (470 , 300), colour, 2)
#cv2.rectangle(img, (350 , 280), (420 , 320), (0,0,0), -2)
#cv2.putText(img , "Vcc", (360 ,310), font, fontScale, color, thickness, cv2.LINE_AA)
#description
#cv2.circle(img, (500,430), 10, (0,0,0), -2)
#cv2.line(img, (500 , 430), (340 , 430), colour, 2)
#cv2.rectangle(img, (120 , 310), (340 , 700), (0,0,0), 2)
#cv2.putText(img , "Pin Details: ", (125 ,370), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "  Input(s0,s1) Output", (125 ,390), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "         0  0    D1", (125 ,410), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "         0  1    D2", (125 ,430), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "         1  0    D3", (125 ,455), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "         1  1    D4", (125 ,480), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "An electronic ", (125 ,520), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "multiplexer can ", (125 ,540), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "be considered as a ", (125 ,560), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "multiple-input,", (125 ,580), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "single-output switch", (125 ,600), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "and a demultiplexer ", (125 ,620), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "as single-input,", (125 ,640), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
#cv2.putText(img , "multiple-output switch", (125 ,660), font, 0.60, (0,0,0), 1, cv2.LINE_AA)

cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.waitKey(0)
cv2.destroyAllWindows()

