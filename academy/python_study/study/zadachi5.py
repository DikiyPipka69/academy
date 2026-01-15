# # задание 1
# nums = input('Введите числа: ').split()
# nums = [int(num) for num in nums]
# squares = list(map(lambda x: x**2, nums))  
# print(squares)

# задание 2
# def filter_even(numbers):
#     even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#     print("четные числа:", even_numbers)
# user_input = input("введите числа: ")
# numbers_list = list(map(int, user_input.split()))
# print(filter_even(numbers_list))

# # 3
# from functools import reduce
# numbers = input('введите числа: ').split()
# def sum_list(numbers):
#     return reduce(lambda x,y : x+y , numbers)
# print(numbers.sum_list(numbers))

# # 4       ---
# words = (input('введите слова: '))
# def words_upper(words):
#     return list(map(lambda x: x.upper(), words))
# total = words_upper(words)
# print(words_upper)

# 5
# def super_kvadrat(spisok):
#     obratno = list(map(lambda x: x**2, reversed(spisok)))
#     return [spisok[i] * obratno[i] for i in range(len(spisok))]
# print(super_kvadrat())


































































































