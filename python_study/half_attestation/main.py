import random
import pandas as pd
from datetime import datetime

class Magic:
    def __init__(self):
        self.list_in = None
        self.dict_in = None
        self.set_in = None
        self.tuple_in = None
        self.bob_responses = [''] * 20
        self.bob_ratings = []
        self.matrix_in = []

    def save_info_to_csv(self, filename="information_test.csv"):
        try:
            data = {
                'variable': ['list_in', 'dict_in', 'set_in', 'tuple_in', 
                            'bob_responses', 'bob_ratings', 'matrix_in'],
                'type': [type(x).__name__ for x in [self.list_in, self.dict_in, self.set_in, 
                                                   self.tuple_in, self.bob_responses, 
                                                   self.bob_ratings, self.matrix_in]],
                'value': [str(x) for x in [self.list_in, self.dict_in, self.set_in, 
                                          self.tuple_in, self.bob_responses, 
                                          self.bob_ratings, self.matrix_in]],
                'length': [len(x) if hasattr(x, '__len__') else 0 
                          for x in [self.list_in, self.dict_in, self.set_in, 
                                   self.tuple_in, self.bob_responses, 
                                   self.bob_ratings, self.matrix_in]],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False, encoding='utf-8')
            print(f"Данные сохранены в {filename}") # сохранение файла в 
            return True
            
        except Exception as e:
            print(f"Ошибка: {e}")
            return False

    def init_str(self, *args):
        '''
        проверка введённых данных
        '''
        if not args:
            print('данных нету')
            return
        self.list_in = []
        for i in args:
            try:
                self.list_in.append(int(i)) # проверка ввода пользователя, если ввёл не целое число, ввёл строку и тд, то идём дальше 
            except ValueError:
                try:
                    self.list_in.append(float(i)) # проверка пользователя, если ввёл дробное число, то идём дальше
                except ValueError:
                    self.list_in.append(i) # проверка ввода пользователя, если ввёл какую то фигню, то бог с ним.
                                            # Пусть остаётся так как есть и идём дальше
        self.dict_in = {i:val for i,val in enumerate(self.list_in)}
        self.set_in = set(args)
        self.tuple_in = args

    def bob(self):
        question = input('задай вопрос бобу: ') # пользователь вводит вопрос бобу
        response = random.choice(self.bob_responses) # боб отвечает пользователю что то
        print(f'боб отвечает: {response}')
        while True: # бесконечнй цикл
            try:
                rating = int(input('оцените ответ боба от 1 до 10: ')) # пользователь вводит число от 1 до 10
                if 1 <= rating <= 10: # если пользователь ввёл число от 1 до 10
                    self.bob_ratings.append(rating) # то кладём эту оценку в список рейитнга боба
                    break # и заканчивает цикл
                else: # если ввёл числа не от 1 до 10, мягко говорим ему что он duraley
                    print('введите число от 1 до 10!!!')
            except ValueError: # если он ввёл вообще не числа, то так прямо и говорим:
                print('duraley, введены неккоректные значения!!!')
        average_rating = sum(self.bob_ratings)/len(self.bob_ratings) # поулчаем одекватность боба
        print(f'адекватность боба: {average_rating:.2f}') # выводим адекватность боба

if __name__ == "__main__": # тестируем код
    magic = Magic()
    magic.init_str(1, 2.5, "hello", 3, 4)
    magic.bob_ratings = [5, 7, 8]
    
    # сохранение переменных в csv
    magic.save_info_to_csv()

df = pd.read_csv('information_test.csv')
print(df)