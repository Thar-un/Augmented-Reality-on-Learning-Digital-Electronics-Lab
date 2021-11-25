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
        if ((x > 483) and (x < 505)):
            if((y > 535) and (y < 561)):
                a1 = 0;
                cv2.putText(img , "0", (530 ,478), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 538) and (x < 560)):
            if ((y > 535 ) and (y < 561)):
                a1 = 1;
                cv2.putText(img , "1", (530 ,478), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 570) and (x < 590)):
            if((y > 540) and (y < 560)):
                a2 = 0;
                cv2.putText(img , "0", (566 ,478), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 610) and (x < 637)):
            if ((y > 536 ) and (y < 561)):
                a2 = 1;
                cv2.putText(img , "1", (566 ,478), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 606) and (x < 720)):
            if((y > 610) and (y < 660)):
                    if ((a1 == 0) and (a2 == 0)):
                        print("1)",a1," ",a2)
                        cv2.putText(img , "0", (602 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (707 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (672 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (567 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                    elif ((a1 == 0) and (a2 == 1)):
                        print("2)",a1," ",a2)
                        cv2.putText(img , "0", (602 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (707 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (672 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (567 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                    elif ((a1 == 1) and (a2 == 0)):
                        print("3)",a1," ",a2)
                        cv2.putText(img , "0", (602 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (707 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (672 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "0", (567 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.imshow(window_name,img)
                    else:
                        print("4)",a1," ",a2)
                        cv2.putText(img , "1", (602 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "1", (707 ,481), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "1", (672 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.putText(img , "1", (567 ,240), font, fontScale, color, 2, cv2.LINE_AA)
                        cv2.imshow(window_name,img)

# path   
img = cv2.imread('‪‪E:\\Final-year Project\\Dataset\\and_gate_Moment.jpg', 1)
window_name = 'Image'
#img = cv2.resize(imag, (800, 800))                    # Resize image

# Start coordinate, here (5, 5)(column , row)
color1 = (0,107,127)
colour = (0,0,0)#bgr
#checkboxes-up
x = 530
y = 220
cv2.rectangle(img, (x,y), (x+20,y+20), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,y), (x+55,y+20), color1, -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,y), (x+90,y+20), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,y), (x+125,y+20), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,y), (x+160,y+20), color1, -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,y), (x+195,y+20), (0,0,0), -2)#(425,50), (445,70)
cv2.rectangle(img, (x+220,y), (x+240,y+20), (0,0,0), -2)#(470,50), (490,70)
#checkboxes-dow
x1 = 460
y1 = 480
cv2.rectangle(img, (x,x1), (x+20,y1), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,x1), (x+55,y1), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,x1), (x+90,y1), color1, -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,x1), (x+125,y1), (0,0,0), -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,x1), (x+160,y1), (0,0,0), -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,x1), (x+195,y1), color1, -2)#(425,50), (445,70)
cv2.rectangle(img, (x+220,x1), (x+240,y1), (0,0,0), -2)#(470,50), (490,70)
#output-box
cv2.rectangle(img, (x+75,x1+150), (x+190,y1+175), (0,0,0), -2)#(375 , 670),(320 , 715)
cv2.putText(img , "Show Output", (609 ,638), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)
#lines!
cv2.line(img, (540 , 480), (490 , 537), colour, 2)
cv2.line(img, (540 , 480), (540 , 537), colour, 2)
cv2.line(img, (575 , 480), (575 , 537), colour, 2)
cv2.line(img, (575 , 480), (620 , 535), colour, 2)
#input-box1
cv2.rectangle(img, (483,535), (503,560), (0,0,0), -2)
cv2.rectangle(img, (539,537), (560,560), (0,0,0), -2)
cv2.putText(img , "0", (485 ,555), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (539 ,555), font, fontScale, color, thickness, cv2.LINE_AA)
#input-box2
cv2.rectangle(img, (570 , 538), (590 , 560), (0,0,0), -2)
cv2.rectangle(img, (612 , 535), (635 , 560), (0,0,0), -2)
cv2.putText(img , "0", (571 ,557), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (613 ,555), font, fontScale, color, thickness, cv2.LINE_AA)
#GND
cv2.line(img, (760 , 480), (760 , 535), colour, 2)
cv2.line(img, (760 , 535), (805 , 535), colour, 2)
cv2.rectangle(img, (800 , 520), (865 , 560), (0,0,0), -2)
cv2.putText(img , "GND", (800 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
#5V
cv2.line(img, (540 , 225), (540 , 180), colour, 2)
cv2.line(img, (540 , 180), (470 , 180), colour, 2)
cv2.rectangle(img, (400 , 170), (470 , 195), (0,0,0), -2)
cv2.putText(img , "+5V", (400 ,190), font, fontScale, color, thickness, cv2.LINE_AA)
#description
cv2.circle(img, (520,371), 10, (0,161,191), -2)
cv2.line(img, (510 , 370), (340 , 370), colour, 2)
cv2.rectangle(img, (120 , 310), (340 , 520), (0,0,0), 2)
cv2.putText(img , "AND GATE", (125 ,340), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "The AND gate with ", (125 ,370), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "inputs A and B and ", (125 ,390), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "output C implements ", (125 ,410), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "the logical expression", (125 ,430), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "C = A.B also", (125 ,455), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "as C = A&B", (125 ,480), font, 0.60, (0,0,0), 1, cv2.LINE_AA)

cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.waitKey(0)
cv2.destroyAllWindows()

