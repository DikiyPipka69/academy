# 1
# a = 'tututu'
# print(type(a))
# b = 2
# print(type(b))
# c = True
# print(type(c))
# d = 11.5
# print(type(d))



# 2
# a = int(input())
# b = int(input())
# c = int(input())

# x = (c - b) / a
# print(x)



# 3 --

# a = float(input())
# b = float(input())
# c = float(input())

# D = b**2 - 4*a*c

# if D > 0:
#     x1 = (-b + D**0.5) / (2*a)
#     x2 = (-b - D**0.5) / (2*a)
#     print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
# elif D == 0:
#     x = -b / (2*a)
#     print(f"x = {x:.2f}")
# else:
#     print("Нет вещественных корней")



# 4
# a = int(input('введите сторону квадрата > '))

# print((a * a))



# 5
# a = int(input('введите радиус круга > '))

# print((a * 4))



# 6
# import math
# a = int(input('введите a > '))
# b = int(input('введите b > '))
# d = int(input('введите d > '))
# c = int(input('введите c > '))

# frst = a + b
# scnd = d - c
# number = frst / scnd

# if number >= 0:
#     result = math.sqrt(number)
#     print(f"Z равен {number} равен {result}")
# else:
#     print("Ошибка")



# 7
# n = int(input('введите кол-во школьников > '))
# k = int(input('введите кол-во яблок > '))

# ost = n % k
# frst = n // k
# print(f'{frst} яблок достанется каждому школьнику')
# print(f'{ost} яблок останется в корзине')



# 8 --
# rubles_per_pie = int(input())    
# kopeeks_per_pie = int(input())   
# number_of_pies = int(input())   

# total_kopeeks = (rubles_per_pie * 100 + kopeeks_per_pie) * number_of_pies
# final_rubles = total_kopeeks // 100
# final_kopeeks = total_kopeeks % 100

# print(final_rubles, final_kopeeks)



# 9
# number = (input('введите натуральное число > '))

# print(number[-1])



# 10
# number = int(input('введите число > '))
# print(number // 10)



# 11
# a = int(input(' введите 1ое число > '))
# b = int(input(' введите 2ое число > '))

# if a < b:
#     print(f'число {a} меньшее')
# elif a == b:
#     print('числа равны')
# else: print(f'число {b} меньшее')



# 12
# string = str(input('введите строку > '))
# print(len(string))



# 13
# n = int(input())
# result = (-15 < n <= 12) or (14 < n < 17) or (n >= 19)

# print(result)



# 14
# a = int(input())
# b = int(input())
# c = int(input())

# print(a + b + c)



# 15
# s = input()
# total = 0
# for char in s:
#     total += int(char)
# print(total)



# 16
# text = input()
# n = int(input())

# result = text * n
# print(result)



# 17
# minutes_total = int(input())

# hours = minutes_total // 60 % 24
# minutes = minutes_total % 60

# print(hours)
# print(minutes)



# 18
# n = int(input())
# k = int(input())

# each = k // n
# remainder = k % n

# print(each)
# print(remainder)



# 19
# a = int(input()) 
# b = int(input())  
# c = int(input())  

# perimeter = 4 * (a + b + c)          
# surface_area = 2 * (a*b + b*c + a*c)  
# volume = a * b * c

# print(perimeter)
# print(surface_area)
# print(volume)



# 20
# ticket = input()
# first_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# last_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# if first_sum == last_sum:
#     print("Счастливый")
# else:
#     print("Обычный")



# 21
# h = int(input())  
# x = int(input())  
# y = int(input()) 

# days = 0
# current_height = 0

# while True:
#     days += 1
#     current_height += x  
    
#     if current_height >= h:
#         break
    
#     current_height -= y  

# print(days)


































