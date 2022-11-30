import cv2
import numpy as np

cap = cv2.VideoCapture('Week3/content/input/Groovy Dancing Girl-Sr2JneittqQ.mp4')
# out = cv2.VideoWriter('Week3/content/output.mp4', -1, 20.0, (640,480))
# out = cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))
ret, frame = cap.read()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fheight = frame.shape[0]
fwidth = frame.shape[1]
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (fwidth,fheight))
while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([0, 0, 100])
        upper_blue = np.array([180, 38, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        b, g, r = cv2.split(result)  
        filter = g.copy()
        ret,mask = cv2.threshold(filter,10,255, 1)
        frame[ mask == 255] = 0
        # cv2.imshow('frame',frame)
        out.write(frame)
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()