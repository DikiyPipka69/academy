import re
# date search
# def find_date(strr):
#     d = re.findall(r'\d{2}.\d{2}.\d{4}', strr)
#     return d
# text = "Учеба началась 01.09.2020, а Новый год был 31.12.2020 и 01.01.2021, а закончится учеба 31.05.2021"
# print(find_date(text))

# 1.
# def find_numbers(text):
#     pattern=r"\d+"
#     return re.findall(pattern,text)
# text = 'abc123def456 xtet798 09 43'
# print(find_numbers(text))

# 2.
# def find_upper(text):
#     pattern=r'[A-ZА-ЯЁ]+'
#     return re.findall(pattern,text)
# text = 'аааааа ЕУП ЛНГОР АлА укпу'
# print(find_upper(text))

# 3.
# def find_russian(text):
#     pattern=r'\b\w*[а-яёА-ЯЁ]\w*\d\w*\b'
#     return re.findall(pattern,text)
# text='bob5 is хлопушки67 and n0t лабуба1488'
# print(find_russian(text))

# 4. /
# def find_smth(text):
#     pattern='\b[А-ЯЁA-Z][а-яёa-z]*\b'
#     return re.findall(pattern,text)
# text = 'текст'
# print(find_smth(text))

# 5. /
# def find_lalala(text):
#     pattern=r'\b[А-ЯЁA-Z][а-яёa-z]*\b'
#     pattern=r'\b[аеёиоуыэюяaeiou][а-яёa-z]*\b'
#     return re.findall(pattern,text)
# text = 'текст'
# print(find_lalala(text))

# 6. -
# def find_six(text):
#     pattern=r'(?<\w)\d+(?<\w)'
#     return re.findall(pattern,text)
# text = 'сло18во ляляля тру99ляля 1'
# print(find_six(text))

# 7. +
# def find_star(text):
#     pattern=r'\*'
#     return re.findall(pattern,text)
# text = 'слово*. *ляляля** * 45.'
# print(find_star(text))

# 8. -
# def find_brackets(text):
#     pattern=r' ^\s*$'
#     return re.findall(pattern,text)
# text = 'слово*. *ляляля** * 45.'
# print(find_brackets(text))

# 9. 
# def find_empty_str(text1):
#     pattern=r'\*'
#     return re.findall(pattern,text1)
#     return re.findall(pattern,text2)
# text1 = 'слово*. *ляляля** * 45.'
# text2 = 'слово*. *'
# print(find_empty_str(text1))
# print(find_empty_str(text2))

















