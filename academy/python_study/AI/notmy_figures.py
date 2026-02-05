import cv2
import math
import imutils
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('pictures\Figures.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("figure/gray.jpg", gray)
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("figure/edged.jpg", edged)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("figure/closed.jpg", closed)
# найти контуры в изображении и подсчитайте количество 
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]  # Совместимость с разными версиями OpenCV
total = 0

# Создаем копию изображения для рисования
output_image = closed.copy()

# Определяем цвета для разных фигур (для наглядности)
colors = {
    "triangle": (0, 255, 0),      # Зеленый
    "square": (255, 0, 0),        # Синий
    "rectangle": (0, 165, 255),   # Оранжевый
    "pentagon": (255, 255, 0),    # Голубой
    "hexagon": (255, 0, 255),     # Розовый
    "circle": (0, 255, 255),      # Желтый
    "undefined": (128, 128, 128)  # Серый
}

# цикл по контурам
for i, c in enumerate(cnts):
    # аппроксимируем (сглаживаем) контур
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
    # Вычисляем центр фигуры
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    
    # Определяем тип фигуры по количеству вершин
    shape_name = "undefined"
    vertices = len(approx)
    
    if vertices == 3:
        shape_name = "triangle"
        total += 1
    elif vertices == 4:
        # Проверяем, является ли фигура квадратом или прямоугольником
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        
        if 0.9 <= aspect_ratio <= 1.1:
            shape_name = "square"
        else:
            shape_name = "rectangle"
        total += 1
    elif vertices == 5:
        shape_name = "pentagon"
        total += 1
    elif vertices == 6:
        shape_name = "hexagon"
        total += 1
    elif vertices == 7:
        shape_name = "heptagon"
        total += 1
    elif vertices == 8:
        shape_name = "octagon"
        total += 1
    else:
        # Проверяем, является ли фигура кругом
        area = cv2.contourArea(c)
        if peri > 0:  # Избегаем деления на ноль
            circularity = 4 * math.pi * area / (peri * peri)
            if circularity > 0.8:
                shape_name = "circle"
                total += 1
    
    # Получаем цвет для фигуры
    color = colors.get(shape_name, colors["undefined"])
    
    # Рисуем контур фигуры
    if shape_name == "circle":
        cv2.drawContours(output_image, [c], -1, color, 3)
    else:
        cv2.drawContours(output_image, [approx], -1, color, 3)
    
    # Добавляем текст с названием фигуры
    if shape_name != "undefined":
        # Создаем текст с названием фигуры и номером
        label = f"{shape_name} #{i+1}"
        
        # Вычисляем размер текста
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_thickness = 2
        text_size = cv2.getTextSize(label, font, font_scale, font_thickness)[0]
        
        # Вычисляем координаты для текста (центрируем)
        text_x = cX - text_size[0] // 2
        text_y = cY + text_size[1] // 2
        
        # Рисуем фон для текста для лучшей читаемости
        cv2.rectangle(output_image, 
                     (text_x - 5, text_y - text_size[1] - 5),
                     (text_x + text_size[0] + 5, text_y + 5),
                     (255, 255, 255), -1)
        
        # Добавляем текст
        cv2.putText(output_image, label, (text_x, text_y), 
                    font, font_scale, (0, 0, 0), font_thickness)
        
        # Рисуем точку в центре фигуры
        cv2.circle(output_image, (cX, cY), 4, color, -1)
        cv2.circle(output_image, (cX, cY), 6, (255, 255, 255), 1)

# Добавляем заголовок с количеством найденных фигур
header_text = f"Found {total} shapes"
header_font_scale = 0.7
header_thickness = 2
header_size = cv2.getTextSize(header_text, cv2.FONT_HERSHEY_SIMPLEX, 
                              header_font_scale, header_thickness)[0]

# Рисуем фон для заголовка
cv2.rectangle(output_image, 
              (10, 10),
              (20 + header_size[0], 40 + header_size[1]),
              (0, 0, 0), -1)

# Добавляем заголовок
cv2.putText(output_image, header_text, (20, 40), 
            cv2.FONT_HERSHEY_SIMPLEX, header_font_scale, 
            (255, 255, 255), header_thickness)

# Добавляем легенду (опционально, если места достаточно)
legend_y = 70
for shape, color in colors.items():
    if shape != "undefined":
        cv2.putText(output_image, f"{shape}:", (20, legend_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        legend_y += 20

print(f"Всего найдено фигур: {total}")

# Показываем результаты
cv2.imshow("Original Image", image)
cv2.imshow("Detected Shapes", output_image)

# Сохраняем результат (опционально)
cv2.imwrite("detected_shapes.jpg", output_image)

# Ожидаем нажатия клавиши
print("Press any key to continue...")
cv2.waitKey(0)
cv2.destroyAllWindows()

# Альтернативный вариант с использованием matplotlib для лучшего отображения
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Конвертируем BGR в RGB для matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
output_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

# Отображаем изображения
axes[0].imshow(image_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(output_rgb)
axes[1].set_title(f'Detected Shapes ({total} found)')
axes[1].axis('off')

plt.tight_layout()
plt.show()

# Вывод информации о найденных фигурах в консоль
print("\n=== Detected Shapes Summary ===")
print(f"Total shapes detected: {total}")
print("Shapes are labeled with numbers for identification")