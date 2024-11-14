# Задача "Счётчик вызовов"
calls = 0

def count_calls():
    """
    Функция подсчитывает количество вызовов остальных функций
    :return: int
    """
    global calls
    calls += 1
    return calls


def string_info(str_var):
    """
    Функция принимает аргумент - строку и возвращает кортеж
     из: длины этой строки, строку в верхнем регистре,
         строку в нижнем регистре
    :param str_var: str
    :return: tuple
    """

    count_calls()
    return (len(str_var), str.upper(str_var), str.lower(str_var))


def is_contains(str_search, list_search):
    """
    Функция принимает два аргумента: строку и список, и возвращает True,
     если строка находится в этом списке, False - если отсутствует
    :param str_search: str
    :param list_search: list
    :return: bool
    """
    count_calls()
    result = False
    for i in range(len(list_search)):
        if str.upper(str_search) == str.upper(list_search[i]):
            result = True
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)