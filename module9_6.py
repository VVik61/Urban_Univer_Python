# -*- coding: utf-8 -*-
"""
Цель: более глубоко понять особенности работы с функциями генераторами
 и оператором yield в Python.
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку
 text и возвращает объект-генератор, при каждой итерации которого будет
  возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
"""

def all_variants(text):
    # создаем генератор от 0(по умолчанию) до числа равного длине text
    # (конечное значение не включается) и шагом 1(по умолчанию)
    for size in range(len(text)):
        for y in range(len(text) - size):
            # получаем срез text от y до y+1+size
            yield text[y: y + size + 1]

a = all_variants("abc")
for i in a:
    print(i)