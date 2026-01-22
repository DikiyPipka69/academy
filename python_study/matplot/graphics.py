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


# несколько графиков в одном окне

# # 1. создаем массив значений X
# x = np.linspace(-10, 10, 400) # от -10 до 100, 400 точек
# x1 = np.linspace(-10, 10, 400) # от -10 до 100, 400 точек
# a = random.randint(1,10)
# b = random.randint(1,10)

# # 2. задаем уравнение для Y
# y = (a*x)**3 + (b*x)**2  # парабола y = (a*x)^3 + (b*x)^2
# y1 = x**2  # парабола y = x^2

# # 3. Создаем график
# plt.figure(figsize=(8, 6)) # задаем размер рисунка
# plt.plot(x, y, label='y = (a*x)^3 + (b*x)^2', color='blue', linewidth=2)
# plt.plot(x1, y1, label='y = x^2', color='purple', linewidth=2)


# # 4. Настраиваем внешний вид
# plt.title('График трёх разных функций')   # Заголовок
# plt.xlabel('ось X')           # подпись оси X
# plt.ylabel('ось Y')           # подпись оси Y
# plt.grid(True, alpha=0.3)     # включаем сетку
# plt.legend()                  # показываем легенду
# plt.axhline(y=0, color='k', linewidth=0.5) # ось X
# plt.axvline(x=0, color='k', linewidth=0.5) # ось Y

# # 5. выводим график
# plt.show()



a = random.randint(1,10)
b = random.randint(1,10)
x = np.linspace(-10, 10, 400) # от -10 до 100, 400 точек

y = x**2
y1 = a

fig, axs = plt.subplots(2, 2)
data = np.random.randn(1000)


plt.title('y = x^2')

axs[0, 0].plot(x, y, label='y = (a*x)**3 + (b*x)**2', color='blue', linewidth=2)
axs[0, 1].scatter(x, y, label='y = (a*x)**3 + (b*x)**2', color='blue', linewidth=2)
# axs[1, 0].bar([1,2,3], [3,2,5])
plt.plot(x, y, label='y = (a*x)**3 + (b*x)**2', color='blue', linewidth=2)
plt.plot(x, y, label='y = x^2', color='blue', linewidth=2)

plt.tight_layout()
plt.show()


# задачка с телом

# # 1. создаем массив значений X
# x = np.linspace(-10, 10, 400) # от -10 до 100, 400 точек
# a = random.randint(1,10)
# b = random.randint(1,10)
# v = 20 # м/с
# g = 9.81 # м/с²
# o = 45 # °(градусов)

# # 2. задаем уравнение для Y
# x(t) = v * cos(o) * t
# y(t) = v * sin(o) * t - (g * t²)/2

# # 3. Создаем график
# plt.figure(figsize=(8, 6)) # задаем размер рисунка
# plt.plot(x, y, label='y = (a*x)**3 + (b*x)**2', color='blue', linewidth=2)

# # 4. Настраиваем внешний вид
# plt.title('График функции y = (a*x)^3 + (b*x)^2')   # Заголовок
# plt.xlabel('ось X')           # подпись оси X
# plt.ylabel('ось Y')           # подпись оси Y
# plt.grid(True, alpha=0.3)     # включаем сетку
# plt.legend()                  # показываем легенду
# plt.axhline(y=0, color='k', linewidth=0.5) # ось X
# plt.axvline(x=0, color='k', linewidth=0.5) # ось Y

# # 5. выводим график
# plt.show()



































