# # task 1
# form = input('Введите фигуру > ')

# if form == 'т':
#     a_triang = float(input('Введите a > '))
#     b_triang = float(input('Введите b > '))
#     c_triang = float(input('Введите c > '))
#     half_triang = p = (a_triang + b_triang + c_triang) / 2
#     area = (p * (p - a_triang) * (p - b_triang) * (p - c_triang)) ** 0.5
    
# elif form == 'п':
#     a_rectangle = float(input('Введите a > '))
#     b_rectangle = float(input('Введите b > '))
#     area = a_rectangle * b_rectangle

# elif form == 'к':
#     radius = float(input('Введите радиус > '))
#     area = 3.14 * radius ** 2
# print(area)


# # task 2
# quantity = int(input('Введите кол-во ступенек > '))

# for i in range(1, quantity + 1):
#     s = ' ' * (quantity - i)
#     h = '#' * i
#     print(s + h)


# # task 3
# quantity = int(input('Введите кол-во ступенек > '))

# for i in range(1, quantity + 1):
#     h = '#' * i
#     s = ' ' * (quantity - i)
#     print(h + s)


# # task 4              ***
# n = int(input('Введите число n > '))
# spisok = []
# number = 1

# while len(spisok) < n:
#     for i in range(number):
#         spisok.append(number)
#         if len(spisok) == n:
#             break
#     number + 1
# print(' '.join(map(str, spisok)))

# task 5
# numbers_str = input('Введите числа > ')
# numbers_list = numbers_str.split()
# result = sum(map(int, numbers_list))

# print(result)


# # task 6                ***
# numbers = input('Введите числа > ')
# spisok = numbers.split()
# result = sum(map(int, spisok))

# print(result)


# task 7
text = input().lower()
words = text.split()
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

for word, count in words_count.items():
    print(word, '-', count)














































































