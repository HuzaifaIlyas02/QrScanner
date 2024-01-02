import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('image.png')
code = decode(img)
print(code)

