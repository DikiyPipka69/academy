import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
import re
from bs4 import BeautifulSoup

pytesseract.pytesseract.tesseract_cmd = r'C:\tesseract\tesseract.exe'

image = cv2.imread("text.jpg")
I = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(I)
plt.show()

hocr = pytesseract.image_to_pdf_or_hocr(image, extension='hocr', lang='eng')
soup = BeautifulSoup(hocr, 'html.parser')

COORDINATES_PATTERN = re.compile(r"bbox\s(-?[0-9]+)\s(-?[0-9]+)\s(-?[0-9]+)\s(-?[0-9]+)")
CONF_PATTERN = re.compile(r"x_wconf\s(-?[0-9]+)")
WORD_PATTERN = re.compile(r">(.*?)</span>")

# создадим список слов и будем запоминать номер строки
word_list = []
s_n = 0

# построчные области
for s in soup.find_all(class_='ocr_line'):

    text = s.text.split()
    if len(text) > 0:

        # пословные области
        for s_word in s.find_all(class_='ocrx_word'):
            
            # слово, его координаты и мера уверенности
            match_word = WORD_PATTERN.search(str(s_word))
            match_coord = COORDINATES_PATTERN.search(str(s_word))
            match_conf = CONF_PATTERN.search(str(s_word))

            word = []
            match_word = match_word.group().strip()
            word.append(match_word[1:len(match_word) - 7])
            word.append([int(match_coord.group(1)),
                         int(match_coord.group(2)),
                         int(match_coord.group(3)),
                         int(match_coord.group(4))])
            word.append(int(match_conf.group(1)))
            word.append(s_n)

            word_list.append(word)

        s_n += 1

np.mean([i[2] for i in word_list])

print(f'')
print(f'word list: {word_list}')
print(f'')
print(f's_n: {s_n}')


























































































