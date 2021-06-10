import cv2 
import numpy as np

# stored photo in perticular variable
viratPhoto = cv2.imread('virat.jpg')
rohitPhoto = cv2.imread('rohit.jpg')

# show images using python code

# for virat photo
cv2.imshow("virat", viratPhoto)
cv2.waitKey()
cv2.destroyAllWindows()

# for rohit photo
cv2.imshow("rohit", rohitPhoto)
cv2.waitKey()
cv2.destroyAllWindows()

# crop face: virat
cropViratPhoto = viratPhoto[10:120, 50:170]
cv2.imshow("crop-virat", cropViratPhoto)
cv2.waitKey()
cv2.destroyAllWindows()

# crop face: rohit
cropRohitPhoto = rohitPhoto[10:120, 50:170]
cv2.imshow("crop-rohit", cropRohitPhoto)
cv2.waitKey()
cv2.destroyAllWindows()

# swap / exchanging face between two photos

viratPhoto = cv2.imread('virat.jpg')
viratPhoto[10:120, 50:170] = cropRohitPhoto
cv2.imshow("virat", viratPhoto)
cv2.waitKey()
cv2.destroyAllWindows()

rohitPhoto = cv2.imread('rohit.jpg')
rohitPhoto[10:120, 50:170] = cropViratPhoto
cv2.imshow("rohit", rohitPhoto)
cv2.waitKey()
cv2.destroyAllWindows()
