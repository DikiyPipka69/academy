import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt


# распознование фигур
figures = cv2.imread('pictures\Figures.png')
gray = cv2.cvtColor(figures, cv2.COLOR_RGB2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("gray.jpg", gray)

# распознавание контуров
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("edged.jpg", edged)
plt.figure(figsize=(15, 15))
# plt.imshow(edged)
# plt.show()

# создайте и примените перекрытие
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closed.jpg", closed)
# plt.figure(figsize=(15, 15))
# plt.imshow(closed)
# plt.show()

# найти контуры в изображении и подсчитайте количество книг
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
triangle = 0
quadrilateral = 0
pentagon = 0
hexagon = 0
circle = 0

# цикл по контурам
for c in cnts[0]:
    # аппроксимируем (сглаживаем) контур
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

# найдём и обведём фигуры
    # треугольник
    if len(approx) == 3:
        cv2.drawContours(figures, [approx], -1, (25, 255, 25), 4) # зелёный
        triangle += 1
    # четырёхугольник
    if len(approx) == 4:
        cv2.drawContours(figures, [approx], -1, (25, 255, 255), 4) # голубой
        quadrilateral += 1
    # пятиугольник
    if len(approx) == 5:
        cv2.drawContours(figures, [approx], -1, (148, 0, 211), 4) # фиолетовый
        pentagon += 1
    # шестиугольник
    if len(approx) == 6:
        cv2.drawContours(figures, [approx], -1, (255, 0, 0), 4) # красный
        hexagon += 1
    # круг
    if len(approx) >= 8:
        cv2.drawContours(figures, [approx], -1, (255, 255, 255), 4) # белый
        circle += 1


# показываем полученное изображение и выводим информацию
print("Найдено треугольников: {0}".format(triangle))
print("Найдено четырёхугольников: {0}".format(quadrilateral))
print("Найдено пятиугольников: {0}".format(pentagon))
print("Найдено шестиугольников: {0}".format(hexagon))
print("Найдено кругов: {0}".format(circle))
# cv2.imwrite("output.jpg", figures)
image = cv2.cvtColor(figures, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(15, 15))
# plt.imshow(figures)

plt.subplot(2, 2, 1)
plt.imshow(figures)
plt.title('Итог')

plt.subplot(2, 2, 2)
plt.imshow(edged)

plt.subplot(2, 2, 3) 
plt.imshow(gray)

plt.subplot(2, 2, 4)
plt.imshow(closed)


plt.show()














































