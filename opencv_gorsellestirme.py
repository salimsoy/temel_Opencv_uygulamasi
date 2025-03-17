import cv2 as cv

img=cv.imread('deneme.jpg')

cv.imshow("bee", img)


cv.waitKey(0)
cv.destroyAllWindows()
