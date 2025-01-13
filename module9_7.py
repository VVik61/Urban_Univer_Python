# -*- coding: utf-8 -*-
"""
Задание: Декораторы в Python
Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор
 и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
 если результат 1ой функции будет простым числом и
 "Составное" в противном случае.
"""

def is_prime(func):
# внутренняя функция wrapper в is_prime
    def wrapper(*args, ** kwargs):
        rez = func(*args, ** kwargs)
        sum_ = sum(args)
        k = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                k = k +1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return rez
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)