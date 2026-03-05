import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
import pytesseract 
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\tesseract\tesseract.exe'

image = cv2.imread("messi.jpg")
I = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(I)
plt.show()
string = pytesseract.image_to_string(image, lang='rus+eng')


img = image.copy()

# получить изображение в оттенках серого
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
# удаление шума
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
# удаление шума
def thresholding(image):
    # устанавливаем для всех пикселей переднего плана значение
    # 255 и все фоновые пиксели на 0
    return cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# удаление шума
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
# удаление шума
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

# удаление шума
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# обнаружение контуров
def canny(image):
    return cv2.Canny(image, 100, 200)

# коррекция наклона
def deskew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)    
    return rotated

# сопоставление шаблонов
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


deskew = deskew(image)
gray = get_grayscale(deskew)
thresh = thresholding(gray)
rnoise = remove_noise(gray)
dilate = dilate(gray)
erode = erode(gray)
opening = opening(gray)
canny = canny(gray)

cv2.imwrite('thresh_messi.jpg', thresh)

images = [gray,rnoise,dilate,erode,thresh,deskew,opening,canny]

# def show_images(images, cols = 1, titles = None):
#     assert((titles is None) or (len(images) == len(titles)))
#     n_images = len(images)
#     if titles is None: titles = ['Image (%d)' % i for i in range(1,n_images + 1)]
#     fig = plt.figure()
#     for n, (image, title) in enumerate(zip(images, titles)):
#         a = int(fig.add_subplot(cols, np.ceil(n_images/float(cols)), n + 1))
#         if image.ndim == 2:
#             plt.gray()
#         plt.imshow(image)
#         a.set_title(title)
#     fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
#     plt.show()
    
# show_images(images, 2, ["gray","rnoise","dilate","erode","thresh","deskew","opening","canny"])

h, w, c = image.shape
boxes = pytesseract.image_to_boxes(image) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

I = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(I)
plt.show()

cv2.imwrite('thresh_messi.jpg', thresh)
thresh = cv2.imread("thresh_messi.jpg")

h, w, c = thresh.shape
boxes = pytesseract.image_to_boxes(thresh) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(thresh, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

I = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(I)
plt.show()

img = cv2.imread("thresh_messi.jpg")

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 50:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

if string == '':
    print(f'Текст не найден')
else:
    print(f'Найденый текст: {string}')
    
I = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(I)
plt.show()






































