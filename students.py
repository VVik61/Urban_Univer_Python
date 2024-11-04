# Дополнительное практическое задание по Модуль 1. Практика GIT. Базовые структуры данных
# исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


# ПОЭТАПНОЕ РЕШЕНИЕ с выводом на экран консоли промежуточных результатов
# надо извлечь из students данные и отсортировать из в алфавитном порядке
# stud_list = sorted(students)
# print(stud_list)

# Соединить данные из grades и stud_list, имеющие одинаковые индексы 0, 1 и т.д
# print(stud_list[0], grades[0])
# print(stud_list[1], grades[1])

# Получение средней оценки ученика
# print(sum(grades[0]) / float(len(grades[0])))  # для Python v.3 и более  float()  можно не использовать
# print(sum(grades[4]) / float(len(grades[1])))

# sum(grades[0]) / float(len(grades[0]))

# создание нового списка, содержащего средние баллы учеников
# grades_sredn = [sum(grades[0]) / float(len(grades[0])), sum(grades[1]) / float(len(grades[1])),\
#                 sum(grades[2]) / float(len(grades[2])), sum(grades[3]) / float(len(grades[3])),\
#                 sum(grades[4]) / float(len(grades[4]))]
#
# print(grades_sredn)
# print('*' * 10)
# Примечание - это обычно решается с помощью циклов, где индекс является переменной от  0 до всего_элементов_в_последовательности - 1

# или для Python
# i = 0
# grades_sredn = []
# for i in range(len(grades)):
#     grades_sredn = grades_sredn + [sum(grades[i]) / float(len(grades[i]))]
#     i += 1
#     if i > 5: break
# print(grades_sredn)

# получить из stud_list строки
# print(stud_list, grades_sredn)

# Наконец, требуемый словарь
# slovar_ocenki = dict(zip(stud_list, grades_sredn))

# print(slovar_ocenki)
# -----------------------------------------------------------------------------------

# ИТОГОВОЕ Решение

# надо извлечь из students данные и отсортировать из в алфавитном порядке
stud_list = sorted(students)

# создание нового списка, содержащего средние баллы учеников
i = 0
grades_sredn = []
for i in range(len(grades)):
    grades_sredn = grades_sredn + [sum(grades[i]) / float(len(grades[i]))]
    i += 1
    if i > 5: break
# Наконец, требуемый словарь
slovar_ocenki = dict(zip(stud_list, grades_sredn))

print(slovar_ocenki)

