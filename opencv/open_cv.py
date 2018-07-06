# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:41:44 2018

@author: hp
"""
'''
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()


'''
'''

import numpy as np
import cv2 as cv
filename = 'messi5.jpg'
img = cv.imread(filename) #loaded a color image 

px = img[100,100]#BGR image
print(px)

blue = img[100,100,0]# accessing only blue pixel

img[100,100] = [255,255,255]#modify the pixel values 

img.item(100,100,2)#accessing RED value

img.itemset((100,100,2),100)#modifying RED value

print( img.shape )
#If an image is grayscale, the tuple returned contains only the number of rows
#and columns, so it is a good method to check whether the loaded image is grayscale or color.

'''
import cv2
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# Importing html smaples for Face and Eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Reading the given Image and converting it to Grayscale
img = cv2.imread('baby.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Detecting Faces from image using Face_Samples
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Iterating for the dimentions of the Detected faces to draw rectangle
for (x,y,w,h) in faces:
    # Creating Rectangle around Face with color Red and of width 2
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Getting start and end points of face to detect eyes within the Face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # Detecting Eyes from image using Eye_Samples
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    # Iterating for the dimentions of the Detected Eyes to draw rectangle
    for (ex,ey,ew,eh) in eyes:
        # Creating Rectangle around Eyes with color Green and of width 2
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img) # Displays the Image with rectangles on Face and Eyes

k = cv2.waitKey(0)
stop = ord("S") # To Stop press capital S (While on the output image)
if k == stop:
    cv2.destroyAllWindows()

elif k == ord('q'):   # To Save and close press q
    cv2.imwrite('marked1.png',img)
    cv2.destroyAllWindows()

