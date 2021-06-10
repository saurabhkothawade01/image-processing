import cv2
import numpy as np

# stored pictures/images in variable
virat = cv2.imread('virat.jpg')
rohit = cv2.imread('rohit.jpg')

# show single image
cv2.imshow("virat", virat)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("rohit", rohit)
cv2.waitKey()
cv2.destroyAllWindows()

# join / combine horizontally
combine_hor = np.hstack((virat, rohit))

# join / combine vertically
combine_ver = np.vstack((virat, rohit))

# show horizontal combine image
cv2.imshow("Horizontal", combine_hor)
cv2.waitKey()
cv2.destroyAllWindows()

# show vertical combine image
cv2.imshow("Vertical", combine_ver)
cv2.waitKey()
cv2.destroyAllWindows()





