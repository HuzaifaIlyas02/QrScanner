import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('image.png')

cap = cv2.VideoCapture(0) # for webcam
cap.set(3,640) #width
cap.set(4,480) #height

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()

while True:
    success, img = cap.read()
    # For multiple bar codes in a picture
    for barcode in decode(img):
        # Decoding the actual data from the Bar code
        myData = barcode.data.decode('utf-8')
        print(myData)

        # Authentication
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0,255,0) # Green
        else:
            myOutput = 'Un-Authorized'
            myyColor = (0,0,255) # Red
            
        # bounding polygon around the barcode
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)

        # Displaying the message above the barcode
        cv2.putText(img,myOutput,(barcode.rect[0],barcode.rect[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)
    cv2.imshow('Result', img)
    cv2.waitKey(1)