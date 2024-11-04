# СЛОВАРЬ
# создаю словарь языков программирования с парами название ЯП: год(ы) создания (с типом - либо целое число, либо строка)
from types import NoneType  # в решении задачи по множеству использовался тип NoneType. PyCharm добавил эту строку автоматом

my_dict = {'Бейсик': 1964, 'Алгол': '1958-1960 годы', 'C': '1969–1973 годы',
     'С++': 'начало 1980-х годов',
     'Паскаль': 1970, 'Delphi ': '12 октября 2004 года', 'С#': '1993–2001 годы',
     'Java': 1995, 'Оберон': 1987,
     'PHP': '8 июня 1995г', 'Swift': 2014,
     'Ruby': 'начал разрабатываться 23 февраля 1993 года, вышел в свет в 1995 году',
     'Kotlin': 2011,
     'Python': 'Начало разработки 1989г. Первая версия -  февраль 1991 года'}

print(my_dict)

# вывод на экран одного значение по существующему ключу
print(my_dict['Python'])

# вывод на экран одного значение по отсутствующему ключу
print(my_dict.get('Фортран', "?"))   # Значение по умолчанию (дефотное)  знак вопроса (?)
# print(my_dict['Фортран'])

# добавление ещё двух произвольные пар того же формата в словарь
my_dict.update({'JavaScript': 1995, 'Go!': 2003})

# Удаление одной из пар в словаре по существующему ключу из словаря и вывод значения из этой пары на экран
print(my_dict.pop('Алгол'))

print(my_dict)

# МНОЖЕСТВО
# создание переменной my_set, присвоение ей множества, состоящее из разных типов данных с повторяющимися значениями
my_set = {5, 'пример строки', True, ('пример строки', 8, 1, 8), -10, 3.14, 9, ('пример строки', 8, 1, 8), True, NoneType}

print(my_set)

# добавление 2 произвольных элементов в множество my_set, которых ещё нет
# my_set.add('добавление')   - пример добавления одного элемента
my_set.update(['добавление', 7])  # добавление двух элементов

# удаление одного элемента из множества my_set
my_set.remove(NoneType)

print(my_set)