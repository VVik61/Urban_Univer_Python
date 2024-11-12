"""
# Был найден код в интернете и адаптирован под задание
n = 3         # количество элементов списков в Большом (matrix) списке
m = 2         # количество элементов в каждом списке, входящем в matrix
value = 5     # значение

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(value)
    matrix.append(row)

print(matrix)

Результат
[[5, 5], [5, 5], [5, 5]]
"""

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
