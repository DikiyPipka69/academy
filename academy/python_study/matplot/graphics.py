import numpy as np
import matplotlib.pyplot as plt
import random

# # 1. создаем массив значений X
# x = np.linspace(-10, 10, 400) # от -10 до 100, 400 точек

# # 2. задаем уравнение для Y
# y = x**2  # Например, простая парабола y = x^2

# # 3. Создаем график
# plt.figure(figsize=(8, 6)) # задаем размер рисунка
# plt.plot(x, y, label='y = x^2', color='blue', linewidth=2)

# # 4. Настраиваем внешний вид
# plt.title('График функции y = x^2')   # Заголовок
# plt.xlabel('ось X')           # подпись оси X
# plt.ylabel('ось Y')           # подпись оси Y
# plt.grid(True, alpha=0.3)     # включаем сетку
# plt.legend()                  # показываем легенду
# plt.axhline(y=0, color='k', linewidth=0.5) # ось X
# plt.axvline(x=0, color='k', linewidth=0.5) # ось Y

# # 5. выводим график
# plt.show()



# 1. создаем массив значений X
x = np.linspace(-10, 10, 400) # от -10 до 100, 400 точек
a = random.randint(1,10)
b = random.randint(1,10)

# 2. задаем уравнение для Y
y = (a*x)**3 + (b*x)**2  # Например, простая парабола y = x^2
y1 = x**2  # Например, простая парабола y = x^2

# 3. Создаем график
plt.figure(figsize=(8, 6)) # задаем размер рисунка
plt.plot(x, y, label='y = (a*x)**3 + (b*x)**2', color='blue', linewidth=2)
plt.plot(x, y1, label='y = (a*x)**3 + (b*x)**2', color='purple', linewidth=2)

# 4. Настраиваем внешний вид
plt.title('График функции y = (a*x)^3 + (b*x)^2')   # Заголовок
plt.xlabel('ось X')           # подпись оси X
plt.ylabel('ось Y')           # подпись оси Y
plt.grid(True, alpha=0.3)     # включаем сетку
plt.legend()                  # показываем легенду
plt.axhline(y=0, color='k', linewidth=0.5) # ось X
plt.axvline(x=0, color='k', linewidth=0.5) # ось Y

# 5. выводим график
plt.show()








































