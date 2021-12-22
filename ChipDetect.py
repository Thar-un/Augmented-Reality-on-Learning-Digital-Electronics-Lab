import cv2
import numpy as np

def spotxy(img, thresh):
        
        thresh = cv2.medianBlur(thresh, 15)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        thresh = cv2.dilate(thresh, rect_kernel, iterations = 1)
        threshold = 250 # initial threshold
        # Canny Edge Detection
        canny_output = cv2.Canny(thresh, 2*threshold, 255)
        
        # Applying Contours
        contours,_ = cv2.findContours(canny_output, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
                        
        contours_poly = [None]*len(contours)
        boundRect = [None]*len(contours)
        for i, c in enumerate(contours):
                contours_poly[i] = cv2.approxPolyDP(c, 3, True)
                boundRect[i] = cv2.boundingRect(contours_poly[i])
    
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)   
    
        for i in range(len(contours)):
                color = (0,255,0)
                area = cv2.contourArea(contours[i])
                if(area >= 1100):
                        cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
                            (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)

                        added_image = cv2.addWeighted(img,0.4,drawing,1,0)
                        cv2.imshow("Contour", added_image)
                        cv2.waitKey(0)
                        return [boundRect[i][0],boundRect[i][1],boundRect[i][2],boundRect[i][3]]             