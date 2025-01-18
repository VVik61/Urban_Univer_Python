# -*- coding: utf-8 -*-
"""
Домашнее задание по теме "Создание потоков"
Задача "Потоковая запись в файлы":
Необходимо создать функцию wite_words(word_count, file_name), где
 word_count - количество записываемых слов,
  file_name - название файла, куда будут записываться слова.

Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
 в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.

Сделать паузу можно при помощи функции sleep из модуля time, предварительно
 импортировав её: from time import sleep.

В конце работы функции вывести строку
 "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию wite_words, передав в
 неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции
 со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку
 основного потока при помощи join.

Также измерьте время затраченное на выполнение функций и потоков.
 Как это сделать рассказано в лекции к домашнему заданию.
"""
# !!!! Получившиеся результаты - файлы с example1.txt до example8.txt
# в Github не добавляю, чтобы уменьшить размер коммита

# Импорты необходимых модулей и функций
import threading
import time

# Объявление функции write_words
def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {(i + 1)}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

# Запуск функций с аргументами из задачи
time_n = time.time() # Время начала записи в ф-лы
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_z = time.time() # Время окончания записи в ф-лы
print('Работа потоков', round(time_z - time_n, 6), 'сек.')

# Создание и запуск потоков с аргументами из задачи
time_n = time.time() # Время начала записи в ф-лы в потоках
print('*' * 100) # чтобы отделить в консоли работу с 1 потоком и другими
                 # потоками
# Создание потоков
thread1 = threading.Thread(target=wite_words, args = (10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words, args = (30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words, args = (200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words, args = (100, 'example8.txt'))

# Запуск потоков
try:
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
except:
    print('Ошибка! Какой-то поток не запустился')
# рабочий код, применявшийся при отладке
# if not thread1.is_alive():
#     thread1.start()
#     print(thread1.is_alive())
# if not thread2.is_alive():
#     thread2.start()
# if not thread3.is_alive():
#     thread3.start()
# if not thread4.is_alive():
#     thread4.start()

# print('1=', thread1.is_alive(),
#         '2=', thread2.is_alive(),
#         '3=', thread3.is_alive(),
#         '4=', thread4.is_alive())

# Приостановка потоков
try:
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
except:
    print('Ошибка! Какой-то поток не остановлен')

time_z = time.time() # Время окончания записи в потоках
print('Работа потоков', round(time_z - time_n, 6), 'сек.')
