# Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


# вызов print_params c параметрами разных типов или с неполным кол-вом парам.
print_params()
print_params('3', True)
print_params(False, None)
# print_params(-8, 9.99, False, 1) - выдаёт ошибку, т.к. передано 4
# параметра, а надо не больше 3
print_params(b = 25)
print_params(c = [1,2,3])

# список values_list с тремя элементами разных типов.
values_list = [True, 'Pyton', -10] # список с элементами разных типов
print(*values_list)

# словарь values_dict с тремя ключами, соответствующими параметрам функции\
# print_params, и значениями разных типов
values_dict = {'a': False, 'b': -9, 'c': 'проба'}
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
