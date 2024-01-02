import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('image.png')

cap = cv2.VideoCapture(0) # for webcam
cap.set(3,640) #width
cap.set(4,480) #height

while True:
    success, img = cap.read()
    # For multiple bar codes in a picture
    for barcode in decode(img):
        print(barcode.data)

        # Decoding the actual data from the Bar code
        myData = barcode.data.decode('utf-8')
        print(myData)

    cv2.imshow('Result', img)
    cv2.waitKey(1)