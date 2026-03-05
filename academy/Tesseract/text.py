import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\tesseract\tesseract.exe'

# image = cv2.imread("text.jpg")
# I = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(10, 10))
# plt.imshow(I)
# plt.show()
# string = pytesseract.image_to_string(image)
# print(string)

image = cv2.imread("messi.jpg")
I = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(I)
plt.show()
string = pytesseract.image_to_string(image, lang='eng+rus')
print(string)























































































