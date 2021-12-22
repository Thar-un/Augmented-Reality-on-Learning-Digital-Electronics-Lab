import cv2

def vidSegment(vid):
        
        count = 0  # to find no.of frames
        while True: 
            flag, image = vid.read() 
            if(flag == 0):
                break
            
            cv2.imwrite("/home/qubercomm/Project/ARDE/Frames/frame" +str(count)+".jpg", image) 
            count += 1
            
        vid.release()
        return count
