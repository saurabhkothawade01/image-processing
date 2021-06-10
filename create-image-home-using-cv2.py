import cv2
import numpy as np

# create 3D array with all zeros - 1000*1000
photo = np.zeros((1000, 1000, 3))

# code for simple home 
cv2.line(photo,(200,150),(800,150),(0,0,255),5)
cv2.line(photo, (200, 150), (150, 230), (0,0,255),5)
cv2.line(photo, (200, 150), (250, 230), (0,0,255),5)
cv2.line(photo, (800, 150), (800, 600), (0,0,255),5)
cv2.line(photo, (150, 230), (800, 230), (0,0,255),5)
cv2.line(photo, (250, 230), (250, 600), (0,0,255),5)
cv2.line(photo, (150, 230), (150, 600), (0,0,255),5)
cv2.line(photo, (150, 600), (800, 600), (0,0,255),5)
cv2.rectangle(photo, (550, 300),(700, 450),(255,0,0),-1)
cv2.line(photo, (620, 300), (620,450), (255,255, 255), 2)
cv2.line(photo, (550, 380), (700,380), (255,255,255), 2)
cv2.rectangle(photo, (300, 400),(400, 596),(0,255,0),-1)
cv2.putText(photo, '- Arth & Summer Program  -', (270, 210), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow("homePhoto", photo)
cv2.waitKey()
cv2.destroyAllWindows()





