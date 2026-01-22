# # task 1
# a = int(input('Введите число a > '))
# b = int(input('Введите число b > '))
# def multiply(a, b):  
#     return a*b
# print(multiply(a, b))



# # task 2
# a = int(input('Введите число a > '))
# b = int(input('Введите число b > '))
# c = int(input('Введите число c > '))
# def multiply(a, b, c):  
#     return a*b*c
# print(multiply(a, b, c))



# # task 3        ***
# numbers = str(input('Введите числа > '))
# list = numbers.split()

# def printer(*numbers):
#     print(numbers)

# print(printer)

# def multiply(a, b, c):  
#     return a*b*c
# print(multiply(a, b, c))



# # task 4
# operation = input('Введите операцию (+, -, *, /) > ')
# a = int(input('Введите число a > '))
# b = int(input('Введите число b > '))
# sub = a-b
# add = a+b
# mult = a*b
# div = a/b

# def subtraction(a, b):
#     return a-b
# def addition(a, b):
#     return a+b
# def multiply(a, b):
#     return a*b
# def division(a, b):
#     return a/b

# if operation == '-':
#     print(subtraction(a, b))
# elif operation == '+':
#     print(addition(a, b))
# elif operation == '*':
#     print(multiply(a, b))
# elif operation == '/':
#     print(division(a, b))
# else:
#     print('Error')



# Пользователь вводит координаты точек (x, y)
# Программа вычисляет расстояние между точками
# Это всё происходит на двух осях x и y
# task from desk

# while False:
# print('Введите координаты на оси x:')
# x_on_x = int(input('x > '))
# y_on_x = int(input('y > '))
# print('Введите координаты на оси y:')
# x_on_y = int(input('x > '))
# y_on_y = int(input('y > '))

# distance_gorisontal = x_on_x+y_on_x+1
# distance_vertical = x_on_y+y_on_y

# print('horizontal dist -', distance_gorisontal)
# print('vertical dist -', distance_vertical)
# Вывод: (4, 2); (-3, 2)

# ДЗ:
# x1 + x2 * x3
# умножение и + это любые знаки
# решение по правилам математики
# def spliting(example, delimers):
#     result = None
#     current = ""

#     for char in example:
#         if char in delimers:
#             if current:
#                 result.append(current)
#                 current = ""
#             result.append(char)
#         else:
#             current += char
#     if current:
#         result.append(current)
#     return result

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

print('Введите пример:')
example = str(input('> '))
print(list(example))

num1 = list(example[0])
num2 = list(example[2])
num3 = list(example[4])
num4 = list(example[6])
nums = [num1, num2, num3, num4]
operation1 = list(example[1])
operation2 = list(example[3])
operation3 = list(example[5])
operations = [operation1, operation2, operation3]

print(operation1)
print(operation1)
print(operation1)
print(f'изаначальный пример: {example}')

i = 0
while i < len(operations):
    if operations[i] in ['*', '/']:
        result = calculate(nums[i], nums[i+1], operations[i])
        nums[i] = result
        nums.pop(i+1)
        operations.pop(i)
    else:
        i += 1

while len(operations) > 0:
    result = calculate(nums[0], nums[1], operations[0])
    nums[0] = result
    nums.pop(1)
    operations.pop(0)
final_result = nums[0]

print(f'Ваше выражение: {num1}{operation1}{num2}{operation2}{num3}={final_result}')

# if operation1 in ['*', '/']:
#     temp = calculate(num1, num2, operation1)
#     result = calculate(num3, temp, operation1)
# elif operation3 in ['*', '/'] and operation2 in ['+', '-']:
#     temp = calculate(num1, num2, operation1)
#     result = calculate(temp, num3, operation2)
# else:
#     temp = calculate(num1, num2, operation1)
#     result = calculate(temp, num3, operation2)
# print(f'Ваше выражение: {num1}{operation1}{num2}{operation2}{num3}={result}')


























































































