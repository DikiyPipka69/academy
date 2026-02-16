import cv2
from matplotlib import pyplot as plt

# распознование лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# чекаем загрузился ли каскад
if face_cascade.empty():
    print("ОШИБКА: Не удалось загрузить каскад")
    # выдаём ошибку если каскад не найден
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        print("Каскад не найден! Скачайте его или проверьте путь.")
        exit()
# загружаем изображения
img1_path = 'pictures/group1.png'  # убедитесь, что файл существует
img1 = cv2.imread(img1_path)
img2_path = 'pictures/students.jpg'  # убедитесь, что файл существует
img2 = cv2.imread(img2_path)
# оригиналные изображения
img1_original_path = 'pictures/group1.png'  # убедитесь, что файл существует
img1_original = cv2.imread(img1_original_path)
img2_original_path = 'pictures/students.jpg'  # убедитесь, что файл существует
img2_original = cv2.imread(img2_original_path)
# выдаём ошибку если изображение 1 не найдено
if img1 is None:
    print(f"ОШИБКА: ИЗОБРАЖЕНИЕ 1 НЕ НАЙДЕНО '{img1_path}'")
    print("Проверьте, существует ли файл и правильное ли имя")
    exit()



# инициализируем лица на 1ом изображении
print(f"Размер изображения 1: {img1.shape}")
# конвертируем в оттенки серого
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# 5. Определяем лица с правильными параметрами
faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.3,  # параметр масштабирования
    minNeighbors=3,    # минимальное количество соседей (было 4)
    minSize=(20, 20)   # минимальный размер лица
)
print(f"Найдено лиц: {len(faces)}")
# рисуем прямоугольники вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 3)
    # Добавим текст с координатами для отладки
    cv2.putText(img1, f'Face {w}x{h}', (x, y-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)



# инициализируем лица на 2ом изображении
print(f"Размер изображения 2: {img2.shape}")
# конвертируем в оттенки серого
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# определяем лица с правильными параметрами
faces2 = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.3,  # параметр масштабирования
    minNeighbors=3,    # минимальное количество соседей (было 4)
    minSize=(20, 20)   # минимальный размер лица
)
print(f"Найдено лиц: {len(faces2)}")
# рисуем прямоугольники вокруг лиц
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 3)
    # Добавим текст с координатами для отладки
    cv2.putText(img2, f'Face {w}x{h}', (x, y-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# отображаем результат
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img1_original_rgb = cv2.cvtColor(img1_original, cv2.COLOR_BGR2RGB)
img2_original_rgb = cv2.cvtColor(img2_original, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 15))
plt.axis('off')
plt.title(f'Фотографии')
plt.tight_layout()

plt.subplot(2, 2, 1)
plt.imshow(img1_rgb)
plt.title(f'Найдено лиц: {len(faces)}')

plt.subplot(2, 2, 2)
plt.imshow(img2_rgb)
plt.title(f'Найдено лиц: {len(faces2)}')

plt.subplot(2, 2, 3) 
plt.imshow(img1_original_rgb)
plt.title('Дефолт картинка №1')

plt.subplot(2, 2, 4)
plt.imshow(img2_original_rgb)
plt.title('Дефолт картинка №2')

plt.show()
# сохраняем результат
cv2.imwrite('output_with_faces.jpg', img1)
print("Результат сохранен в 'output_with_faces.jpg'")
cv2.imwrite('output_with_faces2.jpg', img2)
print("Результат сохранен в 'output_with_faces2.jpg'")














































































































