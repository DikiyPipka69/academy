import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

# вывод дефолт картинки
image = cv2.imread("pictures/card.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 8))
# plt.imshow(image)
# plt.title('Дефолт картинка')
# plt.show()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(1,1),1000)
flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(1,1),1000)
flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

contours = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

total = 0
# цикл по контурам
for c in contours[0]:
    # аппроксимируем (сглаживаем) контур
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    # если у контура 4 вершины, предполагаем, что это карта
    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1
        # сделаем это только для одного контура
        break

# выводим карту без цвета
print("Cadrs found: {0}".format(total))
cv2.imwrite("output.jpg", image)
image_without_color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 8))
# plt.title('Нашли карту без цвета')
# plt.imshow(image_without_color)
# plt.show()

# вывод ориг картинки с распознанной картой
image_with_found_card = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 8))
# plt.title('Ориг картинка с распознанной картой')
# plt.imshow(image_with_found_card)
# plt.show()

h = np.array([[0,0],[449,0],[449,449],[0,449]], np.float32)
transform = cv2.getPerspectiveTransform(np.array(approx.reshape(4,2), np.float32), h) #зачем применяем reshape?
warp = cv2.warpPerspective(image, transform,(450,450))

# вывод онли распознанной карты
warp = cv2.cvtColor(warp, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 8))
# plt.title('Распознанная карта с контуром')
# plt.imshow(warp)
# plt.show()

# score_card = 0

# image = cv2.imread("pictures/card.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# total = 0
# # цикл по контурам
# for c in contours[0]:
#     # аппроксимируем (сглаживаем) контур
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#     # если у контура 4 вершины, предполагаем, что это карта
#     if len(approx) == 4:
#     # cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
#         total += 1
#         h = np.array([[0,0],[449,0],[449,449],[0,449]], np.float32)
#         transform = cv2.getPerspectiveTransform(np.array(approx.reshape(4,2), np.float32), h) #зачем применяем reshape?
#         warp = cv2.warpPerspective(image, transform,(450,450))
#         warp = cv2.cvtColor(warp, cv2.COLOR_BGR2RGB)
#         cv2.imwrite(str("card"+str(total)+".jpg"), warp)
#         plt.figure(figsize=(15, 8))
#         plt.title(f'Распознанная карта без контура')
#         plt.imshow(warp)
#         plt.show()

def preprocess(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2 )
    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,1)
    blur_thresh = cv2.GaussianBlur(thresh,(5,5),5)
    return blur_thresh

# для одинаковых карт (если различий ниту)
img1 = cv2.imread("pictures/card1.jpg")
img2 = cv2.imread("pictures/card1.jpg")
diff = cv2.absdiff(preprocess(img1),preprocess(img2))  
diff = cv2.GaussianBlur(diff,(5,5),5)    
flag, diff = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY) 
print(np.sum(diff))

# # вывод сравнения двух карт
# img = np.concatenate((img1, img2), 1)
# plt.figure(figsize=(15, 15))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.title('Сравнение двух карт')
# plt.imshow(img)
# plt.show()

# # есть ли различия (если картинка чёрная-ниту; если есть чота-есть)
# plt.figure(figsize=(7, 7))
# diff = cv2.cvtColor(diff, cv2.COLOR_BGR2RGB)
# plt.title('Есть ли различия')
# plt.imshow(diff)
# plt.show()

# вывод в одно окно
# №1 (ориг картинка)
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title('Дефолт картинка')
# №2
plt.subplot(2, 2, 2)
print("Cadrs found: {0}".format(total))
cv2.imwrite("output.jpg", image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(15, 15))
plt.title('Нашли карту без цвета')
plt.imshow(image)
# №3
plt.subplot(2, 2, 3) 
plt.imshow(image_with_found_card)
plt.title('Ориг картинка с распознанной картой')
# №4
plt.subplot(2, 2, 4)
plt.imshow(warp)
plt.title('Распознанная карта с контуром')

plt.show()

# # второе окно
# # №5
# plt.subplot(2, 2, 1)
# plt.imshow(figures)

# # №6
# plt.subplot(2, 2, 2)
# plt.imshow(edged)

# # №7
# plt.subplot(2, 2, 3) 
# plt.imshow(gray)

# # №8
# plt.subplot(2, 2, 4)
# plt.imshow(closed)

# plt.show()






















































