# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print((9.99 > 9.98) and (1000 != 1000.1))

# 3nd program
"""
print(2 * 2 + 2)   #  2 умноженное на 2 + 2  без приоритета
print(2 * (2 + 2))   #  2 умноженное на 2 + 2  с приоритетом  для сложения
print((2 * 2 + 2) == (2 * (2 + 2)))    # сравнение вывод результата на консоль
"""
print((2 * 2 + 2) == (2 * (2 + 2)))

# 4nd program
"""
float('123.456')            # преобразовать строку в дробное число
float('123.456') * 10       # умножить на 10, чтобы сместить 4 в целую часть
float('123.456') * 10 % 10               # получение числа перед разделительным знаком (т.е. 4 )  как вещественного (float) числа   
int (float('123.456') * 10 % 10)         # приведение результата к целому числу 
print(int (float(123.456) * 10 % 10))    # вывод результата на консоль 
"""
print(int(float(123.456) * 10 % 10))
