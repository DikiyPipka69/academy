import numpy as np
import matplotlib.pyplot as plt

# # задание 1
# a = np.arange(0, 10)
# b = np.arange(10, 20)
# # a)
# # сложение
# ad = np.add(a, b)
# # то же самое, что
# print("a + b:", ad)
# # вычитание
# sub = np.subtract(a, b)
# print("a - b:", sub)
# # умножение
# mult = np.multiply(a, b)
# print("a * b:", mult)
# # деление
# div = np.divide(a, b)
# print("a / b:", div)
# # б)
# # возведение в степень
# step = np.power(a, 2)
# print("a ** 2:", step)
# step = np.power(b, 2)
# print("b ** 2:", step)

# # задание 2
# c = np.arange(1,101).reshape
# center3x3 = c[3:6, 3:6]
# last_col = c[:, -1].copy()
# c[2::3,:]=0
# print(c)


# # задание 3
# d = np.random.randint(-50, 50, size = 100) # изначальный массив
# positive = d[d>0] # положительныые числа
# div_on_5 = positive[positive%5==0] # числа кратны 5ти
# count=d.size # размер списка

# print(f'положительные числа: {positive}')
# print(f'кратно 5ти: {div_on_5}')
# print(f'размер массива: {count}')


# # задание 4
# randoms = np.random.randint(0, 20, size=(4, 5))
# value = [0,1,2,3,4]
# broadcastain = [arr_val + value for arr_val in randoms] # -
# tuda = np.arange(0, 20)
# obratno = np.random.randint(0, 20, size=(5, 4)) # -

# print('рандомни',randoms)
# print('broadcasting',broadcastain)
# print('туда',tuda)
# print('абратна',obratno)


# # задание 5
# A = np.random.randint(1, 11, size=(3, 3))
# B = np.random.randint(1, 11, size=(3, 3))

# # матричное умножение
# C = np.dot(A, B)  # тоже самое, что A @ B
# # определитель
# detA = np.linalg.det(A)
# # обратная матрица (если det ≠ 0)
# invA = np.linalg.inv(A) if detA != 0 else None
# # собственные значения и векторы
# eigenvals, eigenvecs = np.linalg.eig(A)

# print("A·B =", C)
# print("Определитель det(A) =", detA)
# print("Обратная матрица A^-1 =", invA)
# print("Собственные значения Eigenvalues:", eigenvals)


# задание 6
g = np.array([3.2, 7.1, np.nan, 5.5, np.nan, 2.2])
middle = np.nanmean(g)
num = np.nan_to_num(middle)
print(middle)


# Анализ температурных аномалий
city1 = np.random.randint(-30, 30, size=365).astype(float) # генерация рандома
city2 = np.random.randint(-30, 30, size=365).astype(float) # генерация рандома
num_anomaly = 17
anom_days_1 = np.random.choice([-35, -40, 50, 80], size=num_anomaly)
anom_days_2 = np.random.choice([-35, -40, 50, 80], size=num_anomaly)

mean1, std1 = np.mean(city1), np.std(city1)
mean2, std2 = np.mean(city2), np.std(city2)

norm1 = (city1-mean1)/std1
norm2 = (city2-mean2)/std2

anomaly1 = np.abs(norm1)>2
print(anomaly1)
anomaly2 = np.abs(norm2)>2
print(anomaly2)
common_anomaly = anomaly1 & anomaly2
common_anomaly























































