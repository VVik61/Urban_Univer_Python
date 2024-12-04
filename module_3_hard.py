"""
Должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Вызов
result = calculate_structure_sum(data_structure)
print(result)

Результат
Выходные данные (консоль):
99
"""

def calculate_structure_sum(value):
    sum = 0
    if isinstance(value, int):  # Проверяем есть ли в value типы int
        sum += value  # если есть, то суммируем все числа int
        # print('sum_int=', sum)
    elif isinstance(value, str):  # Проверяем есть ли в value типы str
        sum += len(value)  # если есть, то суммируем кол-во длин всех строк str
        # print('sum_str=', sum)
    elif isinstance(value, list):  # Проверяем есть ли в value типы list
        for i in value:
            sum += calculate_structure_sum(i)  # если есть, то суммируем
            # кол-во длин всех строк list
            # print('sum_list=', sum)
    elif isinstance(value, tuple):      # Проверяем есть ли в value типы tuple
        for i in value:
            sum += calculate_structure_sum(i)  # если есть, то суммируем кол-во
            # длин всех строк tuple
            # print('sum_tuple=', sum)
    elif isinstance(value, set):        # Проверяем, есть ли в value типы set
        for i in value:
            sum += calculate_structure_sum(i)  # если есть, то суммируем
            # кол-во длин всех строк set
            # print('sum_set=', sum)
    elif isinstance(value, dict): # Проверяем есть ли в value типы dict
        for key, value in value.items():
            sum += calculate_structure_sum(key)  # если есть, то суммир.
            # кол-во длин всех строк и ключей
            sum += calculate_structure_sum(value)  # если содержаться, то суммируем количество длин всех строк значений
            # print('sum_dict=', sum)
    return sum  # Возвращаем сумму return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)