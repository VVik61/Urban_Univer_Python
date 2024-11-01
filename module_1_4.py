# Домашнее задание по теме Организация программ и методы строк

my_string = input("Введите строку: ")

print("Количество символов введённого текста = " + str(len(my_string)))
print("Вывод текста в верхнем регистре = " + str(my_string.upper()))
print("Вывод текста в нижнем регистре = " + str(my_string.lower()))
print("Строка my_string, где удалены все пробелы = " + str(my_string.replace(' ', '')))
print("Первый символ строки my_string = " + my_string[0])
print("Последний символ строки my_string = " + my_string[-1])
