import cv2


disp = 0
font = cv2.FONT_HERSHEY_SIMPLEX
org = (15, 25)
fontScale = 0.85
color = (255,255,255) #bgr
thickness = 2


def click_event(event, x, y,
    flags, params):

    global e1,a1,a2,a3,a4,a5,a6,a7,a8;
    cv2.imshow(window_name,img)
    if event == cv2.EVENT_LBUTTONDOWN:
        if ((x > 313) and (x < 340)):
            if((y > 600) and (y < 632)):
                e1 = 0;print("0")
                cv2.rectangle(img, (391,530), (410,550), (0,0,0), -2)
                cv2.putText(img , "0", (394 ,549), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 372) and (x < 398)):
            if ((y > 600 ) and (y < 630)):
                e1 = 1;print("1")
                cv2.rectangle(img, (391,530), (410,550), (0,0,0), -2)
                cv2.putText(img , "1", (394 ,549), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if ((x > 412) and (x < 442)):
            if((y > 600) and (y < 630)):
                a1 = 0;print("0")
                cv2.rectangle(img, (425,530), (445,550), (0,0,0), -2)
                cv2.putText(img , "0", (428 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 457) and (x < 485)):
            if ((y > 600 ) and (y < 630)):
                a1 = 1;print("1")
                cv2.rectangle(img, (425,530), (445,550), (0,0,0), -2)
                cv2.putText(img , "1", (428 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 501) and (x < 533)):
            if ((y > 600 ) and (y < 627)):
                a2 = 0;print("0")
                cv2.rectangle(img, (462,530), (480,550), (0,0,0), -2)
                cv2.putText(img , "0", (462 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 543) and (x < 570)):
            if ((y > 600 ) and (y < 624)):
                a2 = 1;print("1")
                cv2.rectangle(img, (462,530), (480,550), (0,0,0), -2)
                cv2.putText(img , "1", (462 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow(window_name,img)
        if((x > 467) and (x < 581)):#(545 , 678),(660 , 725)
            if((y > 678) and (y < 725)):
                    if (e1 == 0):
                        if a1 == 0 and a2 == 0:
                            cv2.rectangle(img, (494, 530), (514,550), color1, -2)
                            cv2.rectangle(img, (532, 530), (550,550), color1, -2)
                            cv2.rectangle(img, (568, 530), (584,550), color1, -2)
                            cv2.rectangle(img, (606, 530), (624,550), color1, -2)
                            cv2.putText(img , "1", (500 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (535 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (571 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (612 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                        if a1 == 0 and a2 == 1:
                            cv2.rectangle(img, (494, 530), (514,550), color1, -2)
                            cv2.rectangle(img, (532, 530), (550,550), color1, -2)
                            cv2.rectangle(img, (568, 530), (584,550), color1, -2)
                            cv2.rectangle(img, (606, 530), (624,550), color1, -2)
                            cv2.putText(img , "0", (500 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "1", (535 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (571 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (612 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                        if a1 == 1 and a2 == 0:
                            cv2.rectangle(img, (494, 530), (514,550), color1, -2)
                            cv2.rectangle(img, (532, 530), (550,550), color1, -2)
                            cv2.rectangle(img, (568, 530), (584,550), color1, -2)
                            cv2.rectangle(img, (606, 530), (624,550), color1, -2)
                            cv2.putText(img , "0", (500 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (535 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "1", (571 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (612 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                        if a1 == 1 and a2 == 1:
                            cv2.rectangle(img, (494, 530), (514,550), color1, -2)
                            cv2.rectangle(img, (532, 530), (550,550), color1, -2)
                            cv2.rectangle(img, (568, 530), (584,550), color1, -2)
                            cv2.rectangle(img, (606, 530), (624,550), color1, -2)
                            cv2.putText(img , "0", (500 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (535 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "0", (571 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "1", (612 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.imshow(window_name,img)
                    if e1 == 1:
                            cv2.rectangle(img, (494, 530), (514,550), color1, -2)
                            cv2.rectangle(img, (532, 530), (550,550), color1, -2)
                            cv2.rectangle(img, (568, 530), (584,550), color1, -2)
                            cv2.rectangle(img, (606, 530), (624,550), color1, -2)
                            cv2.putText(img , "1", (500 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "1", (535 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "1", (571 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.putText(img , "1", (612 ,550), font, fontScale, color, 2, cv2.LINE_AA)
                            cv2.imshow(window_name,img)                        



# path   
imag = cv2.imread('E:\\Final-year Project\\Dataset\\demux\\frame.jpg', 1)
window_name = 'Image'
img = cv2.resize(imag, (1100, 800))# Resize image

# Start coordinate, here (5, 5)(column , row)
color1 = (0,107,127)
colour = (0,0,0)#bgr
#checkboxes-up
x = 390
y = 290
cv2.rectangle(img, (x,y), (x+20,y+20), (0,0,0), -2)     #(250,290), (270,310)
cv2.rectangle(img, (x+35,y), (x+55,y+20), (0,0,0), -2)  #(505,290), (525,310)
cv2.rectangle(img, (x+70,y), (x+90,y+20), (0,0,0), -2)  #(540,290), (560,310)
cv2.rectangle(img, (x+105,y), (x+125,y+20), (0,0,0), -2)#(575,290), (595,310)
cv2.rectangle(img, (x+140,y), (x+160,y+20), color1, -2)#(610,290), (630,310)
cv2.rectangle(img, (x+175,y), (x+195,y+20), color1, -2)#(645,290), (665,310)
cv2.rectangle(img, (x+210,y), (x+230,y+20), color1, -2)#(680,290), (700,310)
cv2.rectangle(img, (x+240,y), (x+260,y+20), color1, -2)
#checkboxes-dow
x1 = 528    
y1 = 550
cv2.rectangle(img, (x,x1), (x+20,y1), (0,0,0), -2)     #(250,50), (270,70)
cv2.rectangle(img, (x+35,x1), (x+55,y1), (0,0,0), -2)  #(285,50), (305,70)
cv2.rectangle(img, (x+70,x1), (x+90,y1), (0,0,0), -2)  #(320,50), (340,70)
cv2.rectangle(img, (x+105,x1), (x+125,y1), color1, -2)#(355,50), (375,70)
cv2.rectangle(img, (x+140,x1), (x+160,y1), color1, -2)#(390,50), (410,70)
cv2.rectangle(img, (x+175,x1), (x+195,y1), color1, -2)#(425,50), (445,70)
cv2.rectangle(img, (x+215,x1), (x+235,y1), color1, -2)#(470,50), (490,70)
cv2.rectangle(img, (x+250,x1), (x+270,y1), (0,0,0), -2)#(720,528),(740,290)
#output-box
cv2.rectangle(img, (x+75,x1+150), (x+190,y1+175), (0,0,0), -2)#(545 , 678),(660 , 725)
cv2.putText(img , "Show Output", (470 ,710), cv2.FONT_HERSHEY_COMPLEX, 0.50, color, 1, cv2.LINE_AA)
#lines!
cv2.line(img, (400,550), (323,602), colour, 2)
cv2.line(img, (400 , 550), (383 , 600), colour, 2)
cv2.line(img, (436 , 550), (425 , 603), colour, 2)
cv2.line(img, (436 , 550), (468 , 602), colour, 2)
cv2.line(img, (475 , 550), (517 , 600), colour, 2)
cv2.line(img, (475 , 550), (557 , 600), colour, 2)


#input-boxes
cv2.rectangle(img, (312,600), (340,630), (0,0,0), -2)
cv2.rectangle(img, (370,600), (400,630), (0,0,0), -2)
cv2.putText(img , "0", (320 ,627), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (375 ,626), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (410,600), (440,630), (0,0,0), -2)
cv2.rectangle(img, (455,600), (485,630), (0,0,0), -2)
cv2.putText(img , "0", (417 ,625), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (472 ,623), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.rectangle(img, (500,600), (530,625), (0,0,0), -2)
cv2.rectangle(img, (540,600), (570,625), (0,0,0), -2)
cv2.putText(img , "0", (503 ,620), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(img , "1", (545 ,620), font, fontScale, color, thickness, cv2.LINE_AA)

cv2.putText(img , "IC 74139-DEMULTIPLEXER", (400 ,80), font, fontScale, (0,0,0), 2, cv2.LINE_AA)

#GND
cv2.line(img, (661 , 535), (802 , 535), colour, 2)
cv2.rectangle(img, (800 , 520), (865 , 560), (0,0,0), -2)
cv2.putText(img , "GND", (800 ,550), font, fontScale, color, thickness, cv2.LINE_AA)
#5V
cv2.line(img, (390 , 300), (300 , 300), colour, 2)
cv2.rectangle(img, (214 , 280), (303 , 324), (0,0,0), -2)
cv2.putText(img , "Vcc", (218 ,317), font, fontScale, color, thickness, cv2.LINE_AA)
#description
cv2.circle(img, (452,428), 10, (0,0,0), -2)
cv2.line(img, (453 , 430), (340 , 430), colour, 2)
cv2.rectangle(img, (120 , 350), (344 , 515), (0,0,0), 2)
cv2.putText(img , "DEMULTIPLEXER", (125 ,350), font, fontScale, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "Pin Details: ", (125 ,370), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "  Input(e1,s0,s1)Output", (125 ,390), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "        0, 0  0    D1", (125 ,410), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "        0, 0  1    D2", (125 ,430), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "        0, 1  0    D3", (125 ,455), font, 0.60, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(img , "        0, 1  1    D4", (125 ,480), font, 0.60, (0,0,0), 1, cv2.LINE_AA)

cv2.imwrite('butt.jpg',img)
cv2.imshow(window_name, img) 


cv2.setMouseCallback('Image', click_event) #finding mouse click


cv2.waitKey(0)
cv2.destroyAllWindows()

