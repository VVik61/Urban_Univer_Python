def bubble_sort(ls):
    # чтобы цикл сработал хотя бы один раз, задаем значение переменной True
    swap = True
    while swap:
        swap = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                # меняем значение переменной swap для следующего повтора цикла
                swap = True


def selection_sort(ls):
    # i - количество отсортированных элементов
    for i in range(len(ls)):
        # изначально считаем минимальным первый элемент
        low = i
        # цикл для перебора неотсортированных элементов
        for j in range(i+1, len(ls)):
            if ls[j] < ls[low]:
                low = j
        # самый минимальный элемент меняем с первым элементом
        ls[i],  ls[low] = ls[low], ls[i]


def insertion_sort(ls):
    # Начинаем сортировать со второго элемента, т.к. первый элемент считается отсортированным
    for i in range(1, len(ls)):
        item = ls[i]
        # берем элемент для вставки и сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # отсортированный кусок списка двигаем вперед, если он больше элемента для всавки
        while j >= 0 and ls[j] > item:
            ls[j + 1] = ls[j]
            j -= 1
        # вставляем элемент
        ls[j + 1] = item
