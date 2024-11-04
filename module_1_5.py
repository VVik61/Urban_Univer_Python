# кортеж из нескольких элементов разных типов данных
immutable_var = 8, -6, 'привет', 7, 8, [7, 'Python']
print(immutable_var)

# Попытка изменить 2-й элемент кортежа (т.е 'привет')
# immutable_var[2] = 'салют!'
# приведет к ошибке - тип кортеж ('tuple') не поддерживает операцию изменения (присвоения данных)
# для элемента, т.е. изменить значения элементов кортежа (тип которых неизменяемый) нельзя
#
# Traceback (most recent call last):
#   File "E:\Python\lesson0\module_1_5.py", line 5, in <module>
#     immutable_var[2] = 'салют!'
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# создаю список, изменяю его 1-й элемент и вывожу на экран
mutable_list = ['Delphi',  5, 9, 99]
mutable_list[0] = 'Pyton'
print(mutable_list)

