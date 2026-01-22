# class Robot:
#     """данный класс позволят создавать роботов"""
# print(Robot)

# class Planet:
#     def __init__(self, name):
#         self.name = name
# earth = Planet("Earth")
# print(earth.name)

# class Planet:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
# earth = Planet("Earth")
# print(earth.name)

# class House:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return f"Color house: {self.name}"
# colors = []
# house_color = [
#     "green", "grey", "black", "pink", 
#     "purple", "red", "blue", "yellow"
# ]
# for name in house_color:
#     house = House(name)
#     colors.append(house)
# print(colors)


# class Human:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return f"Имя: {self.name}"
# humans_names = []
# names = ['Вова', 'Тимофей', 'Виктор', 'Анастасия',
# 'Мария', 'Артур', 'Дмитрий', 'Анна']
# for name in names:
#     human = Human(name)
#     humans_names.append(human)
# print(humans_names)



# class Humans:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return f"Имя: {self.name}"
# humans_names = []
# print('введите имена:')
# names = input('> ').split()
# for name in names:
#     human = Humans(name)
#     humans_names.append(human)
# print(humans_names)



# class Humans:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
#     def __init__(self, age):
#         self.age = age
#     def __str__(self):
#         return self.age
#     def __repr__(self):
#         return f"Имя: {self.name}; Возраст: {self.age}"
# humans_names = []
# print('введите имена:')
# names = input('> ').split()
# humans_ages = []
# print('введите возраст:')
# ages = input('> ').split()
# for name in names:
#     human = Humans(name)
#     humans_names.append(human)
# print(humans_names)


# сколько посещали планету инопланетяне и сколько их там может жить
import random
minerals = random.randint(0, 1000000)
print('введите название планеты:')
planet = str(input('> '))
class Visits:
    '''
    класс для подсчёта посещений инопланетян
    '''
    def __init__(self, visits_value):
        self.visits_value = visits_value
    def __str__(self):
        return self.visits_value
    def __repr__(self):
        return f"кол-во посещений: {self.visits_value}"
class Lives:
    '''
    класс для подсчёта жизней на планете
    '''
    def __init__(self, lives_value):
        self.lives_value = lives_value
    def __str__(self):
        return self.lives_value
    def __repr__(self):
        return f"Имя: {self.lives_value}"
visits = minerals*2
lives = minerals*2-minerals
print(f'Кол-во посещений планеты {planet}: {visits} раз')
print(f'Кол-во населения планеты {planet}: {lives} сущностей')









# class Planet:
#     '''
#     класс для описания планет солнечной системы
#     '''
#     count = 0
#     def __init__(self, name, mass, position, day, population=0):
#         self.name = name
#         self.mass = mass
#         self.position = position
#         self.day = day
#         self.population = population
#         Planet.count += 1
#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return f"Planet {self.name}"
#     def have_life(self):
#         if self.population>0:
#             return 'Жизнь есть'
#         else:
#             return 'Жизни нет'
#     def mass_more_than_other_planet(self, other_name, other_mass):
#         if self.mass < other_mass:
#             return other_name + ' больше ' + self.name
#         else:
#             return self.name + ' больше ' + other_name





















































