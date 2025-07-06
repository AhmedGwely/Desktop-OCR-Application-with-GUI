import cv2
import pytesseract
import pandas as pd
import os
os.chdir(r"F:\text recognition")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread(r"F:\text recognition\License_plate_Egypt_private.jpg")
#image = cv2.imread(r"img2.png")
#image = cv2.imread(r"x2.jpg")


gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)



text = pytesseract.image_to_string(image)
boxes  = pytesseract.image_to_boxes(image)
#print(text)
# Draw each bounding box on the image

data = []

for itm in boxes.splitlines():
    b = itm.split()
    data.append(itm)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(image, (x, image.shape[0] - y), (w, image.shape[0] - h), (0, 255, 0), 2)
    cv2.putText(image, b[0], (x, image.shape[0] - y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with bounding boxes
cv2.imshow('Image with Bounding Boxes', image)

print(text)




cv2.imshow("gary",gray_img)
cv2.waitKey(0)
