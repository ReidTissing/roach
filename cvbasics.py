#This is a good test for getting a read on which color method is best
import cv2
import numpy as np
def gallery():
    image = cv2.imread("quiz.jpg")
    cv2.imshow('hello world',image)
    print(image.shape)
    #we use cvtcolor, to convert to greyscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('grayscale', gray_image)
    hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV image',hsv_image)
    cv2.imshow('Hue channel',hsv_image[:,:,0])
    cv2.imshow('saturation channel',hsv_image[:,:,1])
    cv2.imshow('value channel',hsv_image[:,:,2])

my_img = np.zeros((400, 400, 3), dtype = "uint8")
# creating a rectangle
cv2.line(my_img, (202, 220), (202, 220), (0, 20, 200), 10)
cv2.imshow('Window', my_img)
# allows us to see image
# until closed forcefully
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey()

cv2.destroyAllWindows()