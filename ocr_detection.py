# -*- coding: utf-8 -*-
"""

@author: walid
"""
#import the libraries
from PIL import Image
import pytesseract
import cv2

#declaring the exe path for tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'


#loading the image from the disk
image_to_ocr = cv2.imread('images/testing/fox_sample2.png')

#preprocessing the image
# step 1 : covert to grey scale
preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)
# step 2 : Do binary and otsu thresholding
preprocessed_img = cv2.threshold(preprocessed_img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# step 3 : Smooth the image using median blur
preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

#save the preprocessed image temporarily into the disk
cv2.imwrite('temp_img.jpg',preprocessed_img)

#read the temp image from disk as pil image
preprocessed_pil_img = Image.open('temp_img.jpg')

#pass the pil image to tesseract to do OCR
text_extracted = pytesseract.image_to_string(preprocessed_pil_img)

#print the text
print(text_extracted)

#display the original image
cv2.imshow("Actual Image",image_to_ocr)



